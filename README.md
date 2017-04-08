# buildher

This is our project for BuildHer 2017 @Northwestern!

We're both second year computer science majors at UChicago and this weekend we wanted to learn more about JavaScript and data visualizations.


## Purpose
For our hack, we decided to look at the relationship between bike routes, bike racks, income, and obesity across Chicago. Biking is fun and healthy, but lately some cities have faced criticism for only providing bike routes and racks in wealthier areas. Without these features, biking can be dangerous and impractical. We wanted to see if inaccessibility to biking is a problem in our city of Chicago as well.

## Data

We collected census data on income and obesity in zip codes and census blocks within the city of Chicago.
We also collected information on bike routes and bike racks from the Chicago city data portal.
Some of this data was stored in a geojson format, and so it was simple to map onto a map with leaflet.js. Some of it, like the obesity data, was stored in a general json format without the included geographic information. We converted this information into geojson with Python, by mapping the census tracts to the the geographic data from our income dataset. 


## Maps

We were both pretty new to JavaScript and data visualizations. We found out about a great mapping library called Leaflet. We were able to customize our map and place it into an HTML file. Leaflet allowed us to add geojson files to our map. For the heatmaps of income and obesity, we wrote functions to map these values to a color spectrum.
We also added checkboxes to let a user customize the map and see the different combinations of bike and geographic data.


