Detail: Homepage
---
![Homepage](pix/populateHomePage.png)

The homepage is the first page that a user sees when they visit your site. The FDP expects a IRI, which is a bit inaccurate in this context.
A IRI is a unique identifier for a resource, which follows the same format as a URL. The latter is also known as a web address. 
The difference between a URL and a URI is that a URL is a subset of a URI. A URL is a URI that also specifies where the resource is located.

A different distinction is that a URL leads to human readable content, while a URI can also lead to machine readable content.
In the context of the FDP, distinct is a bit more prefered, since downstream (Federated) applications of the FDP will use the FDP to find data resources and 
need machine readable content to do so.

So in this case, while the system asks for a URI, we do not want the identifier to lead to a human readable page, but to a machine readable page, but
the actual pointer to the homepage, aka a URL

