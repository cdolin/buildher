import json

with open('income.geojson') as f:
    data = json.load(f)

geoID = {}

for feature in data['features']:
    idnum = feature['properties']['geoid'].split('US')
    if len(idnum[1]) > 11:
        geoID[idnum[1][0:11]] = feature['geometry']
    else:
        geoID[idnum[1]] = feature['geometry']


fips = {}
csvdata = open('obesitychicago.csv','r').read().split("\n")
csvdata = csvdata[0:len(csvdata)-1]
for data in csvdata:
    row = data.split(',')
    num = row[9]
    if num in geoID:
        fips[num] = row[5]


def geojson_features(fips, geoID):
    features = []
    new_entry = {}
    for key in fips:
        new_entry["type"] = "Feature"
        properties = {}
        properties["geoid"] = key
        properties["obesity percentage"] = fips[key]
        new_entry["properties"] = properties
        new_entry["geometry"] = geoID[key]
        features.append(new_entry)
        new_entry={}
    return features


def obj_geojson(geo_obj):
    geojson = {"type":"FeatureCollection",
                "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }}}
    geojson["features"] = geo_obj
    return geojson

geojson_obj = obj_geojson(geojson_features(fips, geoID))

with open('obesity.geojson', 'w') as f:
    json.dump(geojson_obj, f)
