import json

with open('income.geojson') as f:
    data = json.load(f)

geoID = {}

for feature in data['features']:
    idnum = feature['properties']['geoid'].split('US')
    if len(idnum[1]) > 11:
        geoID.append(idnum[1][0:11])
    else:
        geoID.append(idnum[1])

fips = []
csvdata = open('obesitychicago.csv','r').read().split("\n")
for data in csvdata[0:len(csvdata)-1]:
    row = data.split(',')
    fips.append(row[9])

fips = fips[1:len(fips)]
notfound=0

for num in fips:
    if not num in geoID:
        notfound = num

fips.remove(notfound)

for num in fips:
    if not num in geoID:
        print(num)





"""for i in range(0, len(geoID)):
    if geoID[i] in fips:
        found_indexes.append(i)
    else:
        print("")"""
