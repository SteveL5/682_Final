# Steven Littel, 5 May 2020, GEOG 682 Final
import processing
# Load & Display Data
wards = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/ward_from_2012.shp"
shot_spot = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/Shot_Spotter_Gun_Shots.shp"
crime_2017 = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/Crime_Incidents_in_2017.shp"
iface.addVectorLayer(wards,"Wards","ogr")
iface.addVectorLayer(crime_2017,"Crime_2017","ogr")
iface.addVectorLayer(shot_spot,"Shot_Spotter","ogr")

# Joining the Ward shapefile with the Gun Crime point data.
processing.run("qgis:joinbylocationsummary", 
               {'INPUT':wards,'JOIN':crime_2017,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"})
gun_crime_2017_join = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/gun_crime_join.shp"
gun_crime = iface.addVectorLayer(gun_crime_2017_join,"","ogr")

#Add new field in the joined layer for Gun Crimes per 10,000 people
features = gun_crime.getFeatures()

cape = gun_crime.dataProvider().capabilities()

if cape & QgsVectorDataProvider.AddAttributes:
    res = gun_crime.dataProvider().addAttributes([QgsField("Crimes_Per", QVariant.String)])
    gun_crime.updateFields()
    
#Calculating the new field
target_field = 'Crimes_Per'

def calculate_attributes():
    with edit(gun_crime):
        for feature in gun_crime.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('Crimes_Per'), (feature['CCN_count'] / feature['POP_2010']) * 10000)
            gun_crime.updateFeature(feature)
    print('Gun Crimes per 10,000 People in 2017')

calculate_attributes()

#Displaying data in Python Console
for feature in gun_crime.getFeatures():
    print(feature["Label"], 'Gun Crimes', feature["Crimes_Per"])
    
# Joining the Ward shapefile with the Shot Spotter point data. 
processing.run("qgis:joinbylocationsummary", 
               {'INPUT':wards,'JOIN':shot_spot,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Final/682_final_data/682_final_data/shot_spot_join.shp"})
shot_spot_join = "S:/682/Spring20/slittel/Final/682_final_data/682_final_data/shot_spot_join.shp"
shot_spotter = iface.addVectorLayer(shot_spot_join,"","ogr")

#Add new field in the joined layer for dectections by Shot Spotter per 10,000 people
features = shot_spotter.getFeatures()

cape = shot_spotter.dataProvider().capabilities()

if cape & QgsVectorDataProvider.AddAttributes:
    res = shot_spotter.dataProvider().addAttributes([QgsField("Crimes_Per", QVariant.String)])
    shot_spotter.updateFields()

#Calculating new field
target_field = 'Crimes_Per'

def calculate_attributes():
    with edit(shot_spotter):
        for feature in shot_spotter.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('Crimes_Per'), (feature['ID_count'] / feature['POP_2010']) * 10000)
            shot_spotter.updateFeature(feature)
    print('Shooting Indcidents Detected by Shot Spotter per 10,000 People in 2017')

calculate_attributes()

#Displaying data in Python Console
for feature in shot_spotter.getFeatures():
    print(feature["Label"], 'Incidents Detected', feature["Crimes_Per"])
