## Python for Geo


1. [Arcpy](https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm)
If you use Esri ArcGIS, then you’re probably familiar with the ArcPy library. ArcPy is meant for geoprocessing operations. But it’s not only for spatial analysis, it’s also for data conversion, management, and map production with Esri ArcGIS.
2. [Geopandas](http://geopandas.org/)
is like pandas meet GIS. But instead of straight-forward tabular analysis, the geopandas library adds a geographic component. For overlay operations, Geopandas uses Fiona and Shapely, which are Python libraries of their own.
3. [GDAL/OGR](https://gdal.org/)
is used for translating between GIS formats and extensions. QGIS, ArcGIS, ERDAS, ENVI, and GRASS GIS and almost all GIS software use it for translation in some way. At this time, GDAL/OGR supports 97 vector and 162 raster drivers.
4. [RSGISLib](https://www.rsgislib.org/)
is a set of remote sensing tools for raster processing and analysis. To name a few, it classifies, filters, and performs statistics on imagery. My personal favorite is the module for object-based segmentation and classification (GEOBIA).
5. [PyProj](https://pypi.org/project/pyproj/)
The main purpose of the PyProj library is how it works with spatial referencing systems. It can project and transform coordinates with a range of geographic reference systems. PyProj can also perform geodetic calculations and distances for any given datum.
6. [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet)
If you want to create interactive maps, ipyleaflet is a fusion of Jupyter notebook and Leaflet. You can control an assortment of customizations like loading basemaps, geojson, and widgets. It also gives a wide range of map types to pick from including choropleth, velocity data, and side-by-side views.
7. [Folium](https://python-visualization.github.io/folium/quickstart.html)
Just like ipyleaflet, Folium allows you to leverage leaflet to build interactive web maps. It gives you the power to manipulate your data in Python, then you can visualize it with the leading open-source JavaScript library.
8. [Geemap](https://github.com/giswqs/geemap)
Geemap is intended more for science and data analysis using Google Earth Engine (GEE). Although anyone can use this Python library, scientists and researchers specifically use it to explore the multi-petabyte catalog of satellite imagery in GEE for their specific applications and uses with remote sensing data.
9. [LiDAR](https://github.com/giswqs/lidar)
Simply named the LiDAR Python Package, the purpose is to process and visualize Light Detection and Ranging (LiDAR) data. For example, it includes tools to smooth, filter, and extract topological properties from digital elevation models (DEMs) data. Althought I don’t see integration with raw LAS files, it serves its purpose for terrain and hydrological analysis.

10. [Rasterio](https://mapbox.github.io/rasterio/intro.html)
is the go-to library for raster data handling. It lets you read/write raster files to/from numpy arrays (the de-facto standard for Python array operations), offers many convenient ways to manipulate these array (e.g. masking, vectorizing etc.) and can handle transformations of coordinate
reference systems. Just like any other numpy array, the data can also be easily plotted, e.g. using the matplotlib library.

11. [PySAL](https://pysal.readthedocs.io/en/latest/)
The Python Spatial Analysis Library contains a multitude of functions for spatial analysis, statistical modeling and plotting.

1. PyViz/HoloViz Suite ([Geoviews](https://geoviews.org/), [Datashader](https://datashader.org/), [Panel](https://panel.holoviz.org/))
Holoviz maintained libraries have all data visualisations you might need, including dashboards and interactive visualisation. Geoviews, in particular, with its dedicated Geospatial data visualisation library, provides an easy to use and convenient geospatial data. Datashader is also another must-have data visualisation library for Geospatial data scientists who deal with big data. It breaks the process into multiple steps and runs parallel to create a visualisation for large datasets quickly. Finally, Panel, a high-level app and dashboarding solution for Python provide an easy to use interface on creating interactive web apps and dashboards using Jupyter notebooks.

2. [Folium](http://python-visualization.github.io/folium/)
is widely used in geospatial data visualisation. It is built on top of Leaflet.js and can cover most of your mapping needs in Python with its great plugins. Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in a Leaflet map via folium.

3. [Plotly/Plotly Express](https://plotly.com/python/maps/)
Plotly and its high-level API library Plotly Express have an extensive geospatial data visualisation capabilities. Although there is some missing native support for Geopandas GeoDataFrame, the library boasts many mapping types with an easy to use API. With the introduction of Plotly Express in 2019, creating geospatial visualisations with Plotly has become more accessible. With Dash, a widely used and most download web app in data science, Plotly offers a complete solution to deploying web apps. With Plotly Express intuitive API and Dash Plotly, you can take your geospatial web applications and visualisations to the next level.

4. [KeplerGL](https://kepler.gl)
[kepler.gl for Jupyter](https://github.com/keplergl/kepler.gl/blob/master/docs/keplergl-jupyter/README.md) is an excellent tool for big Geospatial data visualisation. It combines a world-class visualisation tool, an easy to use [User interface (UI)](https://towardsdatascience.com/kepler-gl-jupyter-notebooks-geospatial-data-visualization-with-ubers-opensource-kepler-gl-b1c2423d066f), and flexibility of python and Jupyter notebooks.
With just a few lines of code and easy to use interface within Jupyter notebooks, you can create aesthetically pleasing geospatial data visualisation with Kepler GL for Jupyter Python library. The following GIF showcases some of the 3D mapping possibilities with Kepler GL in Python. Handle large dataset with [deck.gl](http://deck.gl). 
[Visualization Tutorial](https://www.analyticsvidhya.com/blog/2020/06/learn-visualize-geospatial-data-jupyter-kepler/).

[QGIS](https://qgis.org/pyqgis/3.0/)
Python can be used in QGIS though a python console and API.  See the PyQGIS Developer Codebook for more information.

[GeoPandas](https://geopandas.org/) may be the most important library for working with vector based geospatial data in Python.  It builds on the geometric operations in Shapely and the datatypes in Pandas.

[GDAL](https://pypi.org/project/GDAL/) is a translator library for a wide variety of raster and vector data formats. 

[PyProj](https://pypi.org/project/pyproj/) is the Python interface to the PROJ cartographic projections and coordinate transformations library.

[PySAL](https://pysal.org/) The Python Spatial Analysis library provides tools for spatial data analysis including cluster analysis,  spatial regression, spatial econometrics as well as exploratory analysis and visualization. 

[RSGISLib](https://www.rsgislib.org/) is the Remote Sensing and GIS Software library for working with remote sensing and imagery data. Variety of raster based tools including image calibration and classification. 

[Geopy](https://github.com/geopy/geopy) - geocoding client for several popular geocoding web services including Nominatim and Google.


[List of resources: python-geospatial](https://github.com/giswqs/python-geospatial)

[Visualizing Geospatial Data in Python - IBM](https://community.ibm.com/community/user/datascience/blogs/paco-nathan/2020/05/17/viz-geo-data-py)

[Automating GIS-processes 2019 - University of Helsinki](https://automating-gis-processes.github.io/site/index.html)

---

- [15 Python Libraries for GIS and Mapping](https://gisgeography.com/python-libraries-gis-mapping/)
- [Essential geospatial Python libraries](https://chrieke.medium.com/essential-geospatial-python-libraries-5d82fcc38731)
- [GIS, Cartographic and Spatial Analysis Tools: Python - Columbia University Library](https://guides.library.columbia.edu/geotools/Python)
- [Open Street Map Visualization](http://projects.mocnik-science.net/osm-vis/)

---

- [Mapscaping project](https://mapscaping.com)
- [Interactive GIS in Jupyter](https://blog.jupyter.org/interactive-gis-in-jupyter-with-ipyleaflet-52f9657fa7a) 
- [Geospatial Analysis Kaggle Tutorial](https://www.kaggle.com/learn/geospatial-analysi)
- [Spatial Analysis Online](https://www.spatialanalysisonline.com/HTML/index.html)