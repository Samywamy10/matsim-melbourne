# File Format Details

## About this Data File
This file has been extracted from the ABS Table Builder Tool using the `2011 Census of Population and Housing` 
directory in the catalogue. 

The database - `2011 Census - Counting of Employed Persons, Place of Work`  has been used to extract 
details about the working population and the place they work. 

For a general introduction about this database, please refer to [2011 Census - Counting of Employed Persons, Place of
 Work - Introduction](<http://www.abs.gov.au/ausstats/abs@.nsf/Previousproducts/2901.0Main%20Features12011?opendocument&tabname=Summary&prodno=2901.0&issue=2011&num=&view=>)

## About the Fields
Each file contains details about the journey-work trips for people based on certain characteristics, belonging to a 
particular SA2 residence location. The column fields used based on their order in the file are - `SA2, SEXP Sex, AGEP 
Age, RLHP Relationship in Household, LFSP Labour Force Status, Main Statistical Area Structure (Main ASGS) (POW) and MTWP Method of Travel to Work`  

#### SA2 Residence (SA2)
The following SA2 residence locations (under Geographical Areas (Usual Residence) - Main Statistical Area (Main ASGS)) 
are covered in the 
Darebin-Banyule 
extents and will
 be used, 

* Viewbank - Yallambie
* Greensborough
* Preston
* Reservoir - West
* Reservoir - East
* Ivanhoe
* Ivanhoe East - Eaglemont
* Kingsbury
* Heidelberg - Rosanna
* Heidelberg West
* Thornbury
* Bundoora - East
* Alphington - Fairfield
* Watsonia
* Montmorency - Briar Hill
* Northcote

#### Gender (SEXP Sex) 
The Gender covered under the `SEXP` fields include: 

* Male
* Female

#### Age (AGEP Age)
Custom age-ranges are used and are listed below:

* 15-24
* 25-39
* 40-54
* 55-69
* 70-84
* 85-99
* 100 years and over

#### Relationships (RLHP Relationship in Household)
The Relationships and custom groupings using them are covered under `RLHP Relationship in Household` 
are described in the document [Custom Relationship Categories](../Custom%20Individual%20Relationship%20Categories.pdf)                     

#### Employment Status (LFSP Labour Force Status)
The employment status categories used, include:

* Employed, working full-time
* Employed, working part-time

Other fields not being used but also listed in the file include:

* Employed, away from work
* Unemployed-NA (Custom Grouping)
  * Unemployed, looking for full-time work
  * Unemployed, looking for part-time work
  * Not in the labour force
  * Not stated

#### SA2 Place of Work (Main Statistical Area Structure (Main ASGS) (POW))
All Victorian SA2 Place of work locations are used

#### Method of Travel to Work (MTWP Method of Travel to Work)
Single legged modes of transport have been covered. The modes include:

* Train
* Tram
* Truck
* Bus
* Ferry
* Taxi
* Car, as driver
* Car, as passenger
* Bicycle
* Motorbike/scooter
* Multi-mode
* TotalMode 
       	
**NOTE:\
i) The multi-legged modes of transport have all been grouped into a custom category called - `Multi-mode`\
ii)The `TotalMode` field covers all the modes available under the ABS Table builder options\_**    
   	
