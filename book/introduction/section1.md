What is a Fair Data Point (FDP)?
===============================
A Fair Data Point (FDP) is an online resource that provides metadata on a collection of (related) datasources.
For an extensive description of the FDP concept, see the [FDP specification](https://specs.fairdatapoint.org/).

There are many ways to create a FDP. In this tutorial we use a FAIR Data Point, that has been setup using
[the reference implementation of the FDP specification](https://fairdatapoint.readthedocs.io/en/latest/)

However, the reference implementation is not the only way to create a FDP. For example, various data pipelines are able to
publish their metadata as a FDP directly from their local pipelines and infrastructures. Currently, this is out of scope
for this tutorial, but future versions of this tutorial will include this.

# FDP index
A FDP index is a FDP that provides metadata on a collection of FDPs. The FDP index is the entry point for the FDP ecosystem.
It is the place where you can find all FDPs that are available in the FDP ecosystem.
This tutorial also contains a few chapters that are built using FDP indexes.