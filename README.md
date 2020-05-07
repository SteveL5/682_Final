# Comparitive Analysis of Washingtion D.C. Gun Crime Occurnace and Shot Spotter Detection in 2017.
## 07 May 2020, Steven Littel

## Introduction
  Overview of the project
  
## Analysis
  ### Data:
  For this project I used 3 datasets. First, the Washington D.C. Ward shapefile and its accompaning information containing in the .dbf located online at http://opendata.dc.gov. Second, 
  
  ### Map Creation:
  In order to create the two maps seen below, I used QGIS 3.4.9 and the aformentioned data sets. After loading all 3 files into the program I used the function Join by Location with the Ward shapefile. Next, in both newly joined files I created a new field titled Crimes_Per for the calcualtions. Using the Field Calculator, for the Gun Crime data set I used the following syntax: (Gun Crime Incidents by Ward / Population 2010) * 10,000. For the shot spotter, I used (Shot Spotter Detections by Ward / Population 2010) * 10,000.Once calcualted I editied the symbology of the map to depcited which wards had the highest final count.
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Gun%20Crime%20Image.png)
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Shot%20Spotter%20Image.png)
  
  
  
  
## Automation

## Results
