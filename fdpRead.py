import rdflib
import pandas as pd
import requests
import yaml
import matplotlib.pyplot as plt
from IPython.display import display, Markdown
import pandas as pd

# Path: fdpRead.py

def FdpRead(url, as_df=True):
    """
    Get the FDP metadata from the given URL.
    """
    r = requests.get(url)
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if as_df:
        return pd.DataFrame(response.json())
    else:
        return response.json()

df = FdpRead("https://w3id.org/duchenne-fdp")
fetched_urls = set()

def parse_graph(graph, fdp, url):
    try:
        graph.parse(url, format="ttl")
        uris[fdp]["resolve"].append(url)
        fetched_urls.add(url)
        return True
    except Exception as e:
        print("Could not parse: " + url)
        uris[fdp]["not_resolve"].append(url)
        print(e)
        return False

def fetchMetaData(graph, fdp, url):
    if parse_graph(graph, fdp, url):
        query = """
        PREFIX ldp: <http://www.w3.org/ns/ldp#>
        SELECT ?o WHERE {
            ?s ldp:contains ?o .
        }
        """
        results = graph.query(query)
        for row in results:
            resolve_url(graph, fdp, str(row["o"]) + "?format=ttl")

def resolve_url(graph, fdp, url):
    if parse_graph(graph, fdp, url):
        query = """
        PREFIX ldp: <http://www.w3.org/ns/ldp#>
        SELECT ?o WHERE {
            ?s ldp:contains ?o .
        }
        """

        datasetsgraph = rdflib.Graph()
        if parse_graph(datasetsgraph, fdp, url):
            datasetsgraph.parse(url, format="ttl")
            datasetsTempResults = datasetsgraph.query(query)
            for row in datasetsTempResults:
                resolve_url(datasetsgraph, fdp, str(row["o"]) + "?format=ttl")
uris = {}
fdpgraph = dict()

for index, row in df.iterrows():
    if not row['clientUrl'].endswith('/'):
        row['clientUrl'] = row['clientUrl'] + '/'
    fdpgraph[row['clientUrl']] = rdflib.Graph()
    uris[row['clientUrl']] = {"resolve": [], "not_resolve": []}
    fetchMetaData(fdpgraph[row['clientUrl']], row['clientUrl'], row['clientUrl'] + "?format=ttl")

# print("Fetching linked data from the web")
for fdp in fdpgraph.keys():
    # print(fdp)
    for node in fdpgraph[fdp].all_nodes():
        if isinstance(node, rdflib.URIRef):
            url = str(node)
            if url not in fetched_urls:
                try:
                    # print("Fetching: " + url)
                    fdpgraph[str(fdp)].parse(url)
                    uris[fdp]["resolve"].append(url)
                    fetched_urls.add(url)
                except:
                    uris[str(fdp)]["not_resolve"].append(url)
                    # print("Could not parse: " + url)
                    continue

def save_dict_to_yaml(dictionary, filepath):
    with open(filepath, 'w') as file:
        yaml.dump(dictionary, file)

# Save dictionary as YAML
save_dict_to_yaml(uris, 'uriLogs2.yaml')