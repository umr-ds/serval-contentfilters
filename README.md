# Serval contentfilters

In the [nicer-filters fork](https://github.com/umr-ds/serval-dna/tree/nicer-filters) pre-, post- and contentfilters are implemented. [Serval-Filter-Specifications.md](https://github.com/umr-ds/serval-dna/blob/nicer-filters/doc/Serval-Filter-Specifications.md) gives a definition of how these filters work and how to configure.

This repository contains a example set of contentfilter binaries to use with the contentfilters:

* **copy2desktop** - copies every new file to the users desktop
* **debug.py** - writes a file relative to the scripts location, containing all calling parameters
* **has-hello.py** - reads a file line-by-line, if a line contains the word "hello" it is set inactive in rhizome store
* **imageStoreJpg.py** - shrinks a given image; if smaller than 80% of the original filesize the old image is set inactive and the new one is inserted.