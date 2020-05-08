# Comparitive Analysis of Washingtion D.C. Gun Crime Occurnace and Shot Spotter Detection in 2017.
## 07 May 2020, Steven Littel

## Introduction
  Overview of the project
  
## Analysis
  ### Data:
  For this project I used 3 datasets downlaoded from http://opendata.dc.gov. First, the Washington D.C. Ward shapefile and its accompaning information. Second, a point layer for gun crimes committed in Washington D.C. for 2017. Finally, another point layer of gunshots detected by Shot Spotter.
  
  ### Map Creation:
  In order to create the two maps displayed below, I used QGIS 3.4.9 and the aformentioned data sets. After loading all 3 files into the program I used the function Join by Location with the Ward shapefile. Next, in both newly joined files I created a new field titled Crimes_Per for the calcualtions. Using the Field Calculator, for the Gun Crime data set I used the following formula: (Gun Crime Incidents by Ward / Population 2010) * 10,000. For the Shot Spotter, I used (Shot Spotter Detections by Ward / Population 2010) * 10,000.Once calcualted I editied the symbology of the map to depcited which wards had the highest final count.
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Gun%20Crime%20Image.png)
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Shot%20Spotter%20Image.png)
  
  
  
  
## Automation
The python code used to automate this analysis.....

### Joining the Data:

To automate joining the layers by location, I used ```qgis:joinbylocationsummary``` 
```
processing.run("qgis:joinbylocationsummary",                  {'INPUT':wards,'JOIN':crime_2017,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"})
gun_crime_2017_join = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"
gun_crime = iface.addVectorLayer(gun_crime_2017_join,"","ogr")
```



## Results

My reccomendation is to expand the Shot Spotter Detection network in Washington D.C. wards 1, 2, & 3. 



