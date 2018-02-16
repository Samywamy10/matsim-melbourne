# Data directory
---
Contains data coming from the census, or derived (such as the so-called "latch" data)


## Census data directory
---
Contains information about the data files extracted either from the ABS (Australian Bureau of Statistics) Table Builder
website or population files created using the LATCH alogrithm

### 2006 Census Shape file data
* URL: http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&CD06aVIC.zip&1259.0.30.002&Data%20Cubes&2C1A08873FA0127ECA2571BF007E221F&0&2006&04.08.2006&Previous
* Last accessed: January 2018
* Saved in `census/2006/`

### 2011 Census correspondence data
* Correspondence information for SA1 codes to statistical area and state codes and names in Australia(viz. SA2, SA3,
  SA4, Greater Capital States and Areas (GCSA), States)
* URL: http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&1270055001_sa1_2011_aust_csv.zip&1270.0.55.001&Data%20Cubes&5AD36D669F284E70CA257801000C69BE&0&July%202011&23.12.2010&Latest
* Last accessed: January 2018
* Saved in `census/2011/`

### 2011 Census latch data
#### 2017-11-30-files-from-bhagya
   * Synthetic population and household files generated on 30-11-2017
     * AllAgents - Population personal characteristics
     * AllFamilies - Population family members and associated household
     * AllHouseholds - Household region and associated families and members
     * Hh-mapped-address - Household features and location data

#### 2018-02-01-files-from-bhagya
   * Synthetic population and household files generated on 30-11-2017
     * AllAgents - Population personal characteristics
     * AllFamilies - Population family members and associated household
     * AllHouseholds - Household region and associated families and members
     * Hh-mapped-address - Household features and location data
     * BuildingsCumSA1andDwellingProperties.json.gz -

* Last accessed: February 2018
* Saved in `census/2011/`

### 2011 Census mtwp data
#### 2017-11-24-Victoria
   * UR and POW by MTWP.csv - Used by the java file - 'AddWorkPlacesToPopulation' to decide the number of trips from an
     SA2 residence to SA2 workplace (categorised by transport mode). The file doesn't categorise people based on their
     characteristics.

#### 2018-01-15-Victoria
   * Victoria_SA2_UR_by_SA2_POW.csv - This files is un-used. There was a deliberation to use the file below for
     extracting the destination and transport mode trips but the file remains un-used (consider deleting).

#### 2018-02-16-mtwp-files
   * The files under this directory contain journey-to-work information for a specific SA2 usual residence location.
     The information is grouped by person characteristics (i.e gender(M/F), age-range(15-24,25-39,40-54,55-69,70-84,
     85-99, 100 years and above), Relationship Status (Lone Parent, Group house hold, Lone Person, Married, Over 15
     Child, Relative, Student, Under 15 Child), LFSP Labour Force Status, Main Statistical Area Structure (Main ASGS)
     Place of Work (POW), MTWP Method of travel to Work.

   ``NOTE - For more information regarding the type of individuals used in creating the above categorical groupings
     refer to the file `data\census\2011\mtwp\2018-02-16-mtwp-files\Custom Individual Relationship Categories.pdf` ``

* Last accessed: February 2018
* Saved in `census/2011/`

### 2011 Census population file
  * VIC - SEXP_AGE5P_LFSP_UR_2011.csv - File used to estimate the part-time and full-time workforce numbers for SA2
    usual residence locations in Victoria. These numbers are used to decide the proportion of working people to be
    assigned destination and transport mode trips
* Last accessed: February 2018
* Saved in `census/2011/`

### 2011 Census shape file data
* Last accessed: January 2018
* Saved in `census/2011/`
  
### 2016 Census correspondence data
* URL:
* Last accessed: January 2018
* Saved in `census/2011/`

### 2016 Census mtwp data
  * Last accessed: January 2018
  * Saved in `census/2011/`

### 2016 Census shape file data
  * Last accessed: January 2018
  * Saved in `census/2011/`
  
## osm directory
---
Contains data from OpenStreetMap, or derived from there

  * Latest OpenStreetMap Data for Australia
  * URL: http://download.gisgraphy.com/openstreetmap/pbf/AU.tar.bz2
  * Last accessed: some time in April 2017 
  * Saved in `data/osm/`
  
## vista directory
---
Contains data used in generating trips from the VISTA data

  * 2009 Victorian Integrated Survey of Travel and Activity (VISTA) Data
  * URL: http://economicdevelopment.vic.gov.au/transport/research-and-data/vista/vista-online-site-has-been-permanently-removed
  * Last accessed: 1 Nov 2017
  * Saved in `data/vista/`
