# Map Data Mining
---

## Project 1 - Auto-georeference Historical City Maps

1. Setting Project Goal (20210804)<br>
To build a tool that automatically geo-references historical maps (like [bromley](http://maps.nypl.org/warper/layers/1403) / [sanborn](http://maps.nypl.org/warper/maps/19243) map) by matching historical building footprints to [modern planimetrics](https://www1.nyc.gov/site/doitt/residents/gis-2d-data.page). ArcGIS has an [auto-georeference functionality](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/georeferencing-a-raster-automatically-to-another-raster.htm), but it is mainly used for matching two satellite images. <br>
Such a tool may help validate and improve the geo-referenced historical maps, which lends to more accurate and consistent mapping of historical geospatial data. 

2. Data Preparation (20210805)<br>
NYPL's New York City atlases collected for multiple time points, warped GeoTIFF ready in Google Drive folders. This is the outcome of on-going data collection infrastructure build-up since last fall of 2020.

3. Find and Familiarize with GIS Tool (20210805)<br>
For easier integration with computer vision (image processing) tools in the Python ecosystem, I chose to familiarize with GIS tools in Python instead of softwares like QGIS/ArcGIS. Ideally, once this tool is well-tested, it can be packaged into a Plugin to such software.

**Rasterio**




**Additional Resources**: 

- Annotation tool suggested by NYU Librarian [Andrew Battista](https://library.nyu.edu/people/andrew-battista/): [Allmaps](https://observablehq.com/@bertspaan/using-allmaps-to-draw-geojson-on-a-iiif-image).



