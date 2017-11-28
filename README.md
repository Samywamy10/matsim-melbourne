# MATSim-Melbourne

* [About this project](#about-this-project)
* [Getting started](#getting-started)
* [Input Data](#input-data)
* [Contributors](#contributors)
* [License](#license)


## About this project

This repository will provide an open and validated MATSim traffic model for the greater Melbourne area. The project is a collaborative effort between individuals and groups from [RMIT University](http://www.rmit.edu.au), [University of Melbourne](http://www.unimelb.edu.au/), [CSIRO Data61](http://data61.csiro.au/), [Swinburne University](http://www.swinburne.edu.au/), [KPMG Australia](https://home.kpmg.com/au/en/home.html), and others.

The first release of the model is expected to be made in Jan 2018.


## Getting started

### Support for large files

Given that the model will invariably be using large data files from various sources, we will use [Git LFS support](https://help.github.com/articles/versioning-large-files/) in GitHub for storing these. The idea is to keep all such files in the `./data` directory. LFS is already set up to track any file in this directory, so there is nothing special 
you have to do. Other than ensuring that you [install Git LFS](https://help.github.com/articles/installing-git-large-file-storage/), otherwise when you clone the repository you only receive the *pointers* to the large files and not the actual data.


## Input Data

* Latest OpenStreetMap Data for Australia  
  * URL: http://download.gisgraphy.com/openstreetmap/pbf/AU.tar.bz2
  * Last accessed: some time in April 2017 
  * Saved in `data/osm/`


* 2009 Victorian Integrated Survey of Travel and Activity (VISTA) Data
  * URL: http://economicdevelopment.vic.gov.au/transport/research-and-data/vista/vista-online-site-has-been-permanently-removed
  * Last accessed: 1 Nov 2017
  * Saved in `data/vista/`

## How to build and run

To build the project, do:
```concept
mvn clean install
```

To create the MATSim activity plans for the population, using the VISTA 2009 data only (i.e., a small 
subset of the full Melbourne population), do something like what is below. This will extract the VISTA CSV files, 
and run the demand generation routine. The output population files will be saved under `scenarios/devel/pop*.xml.gz`. 
**Note: pre-generated population files are already checked in, so unless you are looking to regenerate the 
files, you can probably skip this step.**

```concept
cd data && unzip VISTA_v3_Online_Data_CSV_2009.zip && cd -
mvn exec:java -Dexec.mainClass="au.edu.unimelb.imod.demand.KaiCreateDemand"
```

Then to run the simulation with the generated MATSim population, do:
```concept
mvn exec:java -Dexec.mainClass="org.matsim.run.RunMelbourne"
```

## Contributors

* Claire Boulange, RMIT University
* Dhirendra Singh, RMIT University
* Jonathan Arundel, RMIT University
* Kai Nagel, TU Berlin
* Leorey Marquez, Data61/CSIRO
* Lin Padgham, RMIT University
* Nicole Ronald, Swinburne University
* Renan Grace, KPMG 
* Roberto Sabatini, RMIT University 
* Sara Moridpour, RMIT University 
* Stephan Winter, University of Melbourne 
* Zahra Navidi, University of Melbourne

## License

Open source license still to be agreed.

