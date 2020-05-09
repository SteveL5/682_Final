# Comparative Analysis of Washington D.C. Gun Crime Occurrence and ShotSpotter Detection in 2017
## 07 May 2020, Steven Littel

## Introduction
  In 2006 the Metropolitan Police Department of Washington D.C. implemented the ShotSpotter gunshot detection system in areas of the city with "high population density areas with frequent sounds of gunshots incidents" (http://opendata.dc.gov). While new sensors were installed since then and updates have been made, sections of the city still remain uncovered. This analysis will review the ShotSpotter data from 2017 as well as reported gun crime incidents in the same year in order to identify which D.C. wards are the best candidates for expanded ShotSpotter networks.
  
## Analysis
  ### Data
  For this project I used 3 datasets from http://opendata.dc.gov. First, the Washington D.C. Ward polygon shapefile and its accompanying information. Second, a point layer for gun crimes committed in the city for 2017. Finally, another point layer of gunshots detected by ShotSpotter.
  
  ### Map Creation
  In order to create the two maps displayed below, I used QGIS 3.4.9 and the aforementioned data sets. After loading all 3 files into the program I used the data management function *Join by Location*. I create two separate layers, one with the ShotSpotter and ward layer and a second with the gun crimes and ward layer. Next, in both newly joined files I created a new field titled *Crimes_Per* that will be used for the calculations. Using the Field Calculator, for the gun crime dataset I used the following formula: (Gun Crime Incidents by Ward / Population 2010) * 10,000. For the ShotSpotter, I used (Shot Spotter Detections by Ward / Population 2010) * 10,000. Once calculated I edited the symbology of the map to depict which wards had the highest final count.
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Gun%20Crime%20Image.png)
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Shot%20Spotter%20Image.png)
  
  
  
  
## Automation
  The automation of the analysis begins with loading and displaying the datasets using ```iface.addVectorlayers```.

### Joining the Data
  Once the datasets are loaded the script then joins the D.C. Wards polygon layer and the Gun Crime point data using the function ```qgis:joinbylocationsummary```. The algorithm combines the vector layers via their location and combines the attribute table of the 'JOIN' layer to the 'INPUT' layer. In the example below we see that a new layer was created with the total number of crimes by Ward being added to the existing attribute table of the wards layer. This process sets the stage for calculations to be completed on this problem set. Once finished the result is added to the map.
```
processing.run("qgis:joinbylocationsummary",       
{'INPUT':wards,'JOIN':crime_2017,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"})
gun_crime_2017_join = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"
gun_crime = iface.addVectorLayer(gun_crime_2017_join,"","ogr")
```
### Adding a New Field
  Once the join layer is added to the map, the script will add a blank field onto the attribute table. Doing this allows for a space where the crimes per 10,000 people number can be calculated. To do this the script will check to see if the data is capable of adding or deleting fields using ```dataProvider().capabilities()```. Next, the script runs the algorithm ```QgsVectorDataProvider.AddAttributes``` and ```dataProvider().addAttributes``` to add the desired field names "Crimes_Per". Finally the dataset is updated with the new field.
```
features = gun_crime.getFeatures()
cape = gun_crime.dataProvider().capabilities()
if cape & QgsVectorDataProvider.AddAttributes:
    res = gun_crime.dataProvider().addAttributes([QgsField("Crimes_Per", QVariant.String)])
    gun_crime.updateFields()
```
### Calculating the New Field
  Once the field for crimes per 10,000 people is ready and NULL the script runs a formula using two other columns from the attribute table. The algorithm for this is ```def calculate_attributes():``` along with the function ```feature.setAttribute``` to specify the formula and the desired field. Finally, the script updates the feature and calculates the attributes.
```
target_field = 'Crimes_Per'

def calculate_attributes():
    with edit(gun_crime):
        for feature in gun_crime.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('Crimes_Per'), (feature['CCN_count'] / feature['POP_2010']) * 10000)
            gun_crime.updateFeature(feature)
    print('Gun Crimes per 10,000 People in 2017')

calculate_attributes()
```
### Round 2 and Results
  Once the scripts completes the process for 2017 Gun Crimes it will run the same code with small changes for the Shot Spotter. Full results of both layers are printed in the Python console. This is the code to print the Shot Spotter Detections:
```
for feature in shot_spotter.getFeatures():
    print(feature["Label"], 'Incidents Detected', feature["Crimes_Per"])
```

The full python code used to automate this analysis can be found in the GitHub Respository under [Final_Code.py](https://github.com/SteveL5/682_Final/blob/master/Final_Code.py).

## Results
  My recommendation is to expand the Shot Spotter detection systems in Washington D.C. wards 1, 2, and 6. The ShotSpotter detected only 210, 7, and 299 gunshots per 10,000 in 2017, respectively. In the same wards there were 620, 776, and 724 gun crimes reported. This signifies an opportunity for increased detection and real time reporting on gun crime incidents. 

### Limitations
  A limitation to this analysis is the error rate for the ShotSpotter. While is is a very refined system, it may make mistakes that could change altered. Another limitation is the ShotSpotter categorization of multiple gunshots. As stated on D.C.'s open data website, "A ShotSpotter incident may involve one gunshot or multiple gunshots depending on the time elapsed between each shot." This may cause a discrepancy from actual numbers if the ShotSpotter picked up multiple gun shots, categorized them under the same serial number, when in reality it was two different instances.

## Sources
1. *opendata.dc.gov*
2. *https://opendata.dc.gov/datasets/89bfd2aed9a142249225a638448a5276_29*



