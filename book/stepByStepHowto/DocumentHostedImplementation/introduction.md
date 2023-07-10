Document-hosted FDP implementation
==============================
contributed by [Rajaram Kaliyaperumal](https://orcid.org/0000-0002-1215-167X), [Egon Willighagen](https://orcid.org/0000-0001-7542-0286) and [Andra Waagmeester](https://orcid.org/0000-0001-9773-4008)
## Introduction
In this chapter we will describe how to provide metadata through a FAIR Data Point (FDP) using a document-hosted implementation. 
The next chapter will describe how to provide metadata through a FDP using a software-hosted implementation, also known as the FDP reference implementation.

We will use the [WikiPathways FDP](https://fdp.wikipathways.org/) as an example.The FDP describes the monthly release as a dcat:Dataset with currently two distributions, one being the download file with Graphical Pathway Markup Language (GPML) files and the second being the download file GMT files, with the genes per pathway.

The WikiPathways FDP has been registered with the [EJP-RD index](https://index.vp.ejprarediseases.org/). This index needs to be routinely sent a message (a “ping”) to signal the FDP is still online. This has been set up with a GitHub Action that is routinely run using a crontab approach. The pinging is done with a Python script written by Rajaram Kaliyaperumal ([ping.py](https://github.com/wikipathways/fdp/blob/main/script/ping.py)). The full source code is [available](https://github.com/wikipathways/fdp).

Limitations of the current approach is that the Turtle files of the FDP are served as HTML pages, and neither have the expected Turtle MIME type nor the common file extension for Turtle files. Second, the current files will need to get automatically generated from the WikiPathways VoID header fies, which is currently still done manually.


