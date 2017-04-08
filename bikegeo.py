import json

csvdata = open('Bike_Racks.csv','r').read().split("\n")
csvdata = csvdata[1:len(csvdata)]

racks = []

for row in csvdata:
    rack = row.split(',')
    racks.append(rack[0:8])


racks = racks[0:len(racks)-1]
for row in racks:
    print(row)

def geojson_features(racks):
    features = []
    new_entry = {}
    for rack in racks:
        new_entry["type"] = "Feature"
        properties = {}
        properties["rackID"] = rack[0]
        properties["address"] = rack[1]
        properties["neighborhood name"] = rack[4]
        properties["racks"] = rack[5]
        new_entry["properties"] = properties
        geometry = {}
        geometry["type"] = "Point"
        geometry["coordinates"] = [float(rack[6]), float(rack[7])]
        new_entry["geometry"] = geometry
        features.append(new_entry)
    return features



geofeatures = geojson_features(racks)

def geojson_obj(features):
    geojson = {"type": "FeatureCollection"}
    geojson["features"] = features
    return geojson

bikerack_geojson = geojson_obj(geofeatures)

with open('bikeracks.geojson','w') as f:
    json.dump(bikerack_geojson, f)
