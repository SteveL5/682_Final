# Comparitive Analysis of Washingtion D.C. Gun Crime Occurnace and Shot Spotter Detection in 2017.
## 07 May 2020, Steven Littel

## Introduction
  Overview of the project
  
## Analysis
  ### Data
  For this project I used 3 datasets downlaoded from http://opendata.dc.gov. First, the Washington D.C. Ward shapefile and its accompaning information. Second, a point layer for gun crimes committed in Washington D.C. for 2017. Finally, another point layer of gunshots detected by Shot Spotter.
  
  ### Map Creation
  In order to create the two maps displayed below, I used QGIS 3.4.9 and the aformentioned data sets. After loading all 3 files into the program I used the function Join by Location with the Ward shapefile. Next, in both newly joined files I created a new field titled Crimes_Per for the calcualtions. Using the Field Calculator, for the Gun Crime data set I used the following formula: (Gun Crime Incidents by Ward / Population 2010) * 10,000. For the Shot Spotter, I used (Shot Spotter Detections by Ward / Population 2010) * 10,000.Once calcualted I editied the symbology of the map to depcited which wards had the highest final count.
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Gun%20Crime%20Image.png)
  
  ![alt text](https://github.com/SteveL5/682_Final/blob/master/Shot%20Spotter%20Image.png)
  
  
  
  
## Automation
The automation of the analysis begins with loading and displaying the datasets using ```iface.addVectorlayers```.

### Joining the Data
Once the datasets are loaded the script then joins the D.C. Wards polygon layer and the Gun Crime point data using the function ```qgis:joinbylocationsummary```. The algortihm combines the vector layers by their location and combines the attribute table of the 'JOIN' layer to the 'INPUT' layer. In the example below we see that a new layer was created with the total number of crimes by Ward being added to the exsiitng arritbute table of the *wards* layer. The processes sets the satge for calculations to be complete on this problem set. Once complete the result is added to the map.
```
processing.run("qgis:joinbylocationsummary",       
{'INPUT':wards,'JOIN':crime_2017,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"})
gun_crime_2017_join = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"
gun_crime = iface.addVectorLayer(gun_crime_2017_join,"","ogr")
```
### Adding a New Field

```
features = gun_crime.getFeatures()

cape = gun_crime.dataProvider().capabilities()

if cape & QgsVectorDataProvider.AddAttributes:
    res = gun_crime.dataProvider().addAttributes([QgsField("Crimes_Per", QVariant.String)])
    gun_crime.updateFields()
```

### Calculating the New Field

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

The full python code used to automate this analysis can be found in the GitHub Respository under [Final_Code.py](https://github.com/SteveL5/682_Final/blob/master/Final_Code.py).

## Results

My reccomendation is to expand the Shot Spotter Detection network in Washington D.C. wards 1, 2, & 3. 



