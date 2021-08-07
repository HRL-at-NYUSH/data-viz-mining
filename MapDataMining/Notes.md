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

4. Experiment Morphology Operation Approach (20210806)<br>
	- To fix lighting difference, I tried Otsu thresholding (good only for local parts of map) vs AdaptiveThreshold (good for overall but has dot noise, removeable).
	- To extract the shape of city blocks, I tried to "blur" the map than get the large contours (in bromley 1879 layer_id 1403, city blocks have shaded areas on the inner border, thus one idea is to blur and pick up such shaded areas) For blurring, tried medianBlur vs GaussianBlur vs bilateralFiltering vs blur(simple avg). During this process, implemented a parameter grid-search tool for visual comparisons of parameter sets. The finding is that small amount of blurring doesn't turn shaded areas into concrete borders, while large amount of blurring cause printed street name to merge with block borders. In short, blurring is hard to tune and not clean enough for detecting block contours. Canny + Blur doesn't help much either. Another noticeable problem with the data is that some block has a special building on one border (colored in red) but doesn't have shaded region as other parts do. Also, one trick is inversing the color of the image so that contours are tracing the shape of the blocks (foreground) while streets are in black (background). 
	- Since getting the contours by "looking at it from a bird eye view" (blurrily) is not showing good progress, I tried to make an attempt by creating detailed but rough-edged contours and then pruning them to get smooth city block contours. One common challenge I found with city block contour detection in historical maps is that some street number and dimension number are printed so close to the block border that the numbers touch the border. Then when detecting contours, it is very hard to remove the printed numbers from the contours. For that, I tried detecting comparatively much smaller segments, detecting sudden changes in the directions of line segments, or combination of both. During the process, I realize it's better to first simply the contour with approximate polygons, then remove the comparatively too small segments. The results from this approach is good for some blocks, but not for others. Additional finetuning and human checking is required, which makes the process less attractive.

5. Experiment Marker-based Approach (20210807)<br>
	- In light of the efforts going into detecting the city block contours, I start to reflect on where the bottlenecks are for this task. Successful batch processing relies on regularity in data. One source of regularity, as analyzed above, comes from the shade region at inner borders. Another regularity is that the shapes of the city blocks are, in many places, standardized parallelogram. This also means the streets that cut out the blocks are straigt lines in many places. Once I realized this, I started exploring a manual marking + machine detection approach to expedite the contour detection process.
	- Line vs Dot


**Rasterio**

> High performance, lower cognitive load, cleaner and more transparent code. This is what Rasterio is about. ([Intro](https://rasterio.readthedocs.io/en/latest/intro.html))
> 
> For Mac OS X, pip install rasterio ([Installation for other OS](https://rasterio.readthedocs.io/en/latest/installation.html))
> 
> `import rasterio`
> 
> `dataset = rasterio.open('example.tif')`
> 
> `dataset.count` (number of bands) A dataset band is an array of values representing the partial distribution of a single variable in 2-dimensional (2D) space. All band arrays of a dataset have the same number of rows and columns. 
> 
> `dataset.bounds`
> 
> `dataset.transform` `dataset.transform * (dataset.width, dataset.height) -> (x, y) in the CRS`
> 
> `dataset.crs`
> 
> **Read raster data**
> 
> `dataset.indexes` `(1,)` Following the GDAL convention, bands are indexed from 1.
> 
> `band1 = dataset.read(1)`
> 
> **Translate between pixel positions and coordinates**
> 
> `row,col = dataset.index(x,y)`
> `x, y = dataset.xy(row,col)`
> 
> Create raster data - sample code [here](https://rasterio.readthedocs.io/en/latest/quickstart.html#creating-data).
> 
> Advanced topics
> 
> Raster data processing with CLI [rio-calc](https://rasterio.readthedocs.io/en/latest/topics/calc.html#using-rio-calc) 
> 
> RGB [Color](https://rasterio.readthedocs.io/en/latest/topics/color.html) will be in three separate bands of a GeoTIFF. Check color interpretation by `dataset.colorinterp[0]`, set it during creation using `dataset.profile['photometric']`. 
> 
> [Vector Features](https://rasterio.readthedocs.io/en/latest/topics/features.html) via `shapes()` and `rasterize()`.
> 
> [Interoperability between raster and image](https://rasterio.readthedocs.io/en/latest/topics/image_processing.html)
> 
> `from rasterio.plot import reshape_as_raster, reshape_as_image`
> 
> `raster = rasterio.open("tests/data/RGB.byte.tif").read()`
> `raster.shape (3, 718, 791)`
> 
> `image = reshape_as_image(raster)`
> `image.shape (718, 791, 3)`
> 
> [Masking a raster using a shapefile](https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html#masking-a-raster-using-a-shapefile). [Nodata Mask](https://rasterio.readthedocs.io/en/latest/topics/masks.html) (Special mask meaning in Numpy vs Rasterio)
> 
> Reduced resolution [overview](https://rasterio.readthedocs.io/en/latest/topics/overviews.html) and [Resampling](https://rasterio.readthedocs.io/en/latest/topics/resampling.html) and [**Plotting**](https://rasterio.readthedocs.io/en/latest/topics/plotting.html). 
> 
> [Reprojection](https://rasterio.readthedocs.io/en/latest/topics/reproject.html)
> 
> High performance: [Concurrent processing](https://rasterio.readthedocs.io/en/latest/topics/concurrency.html), [In-Memory Files](https://rasterio.readthedocs.io/en/latest/topics/memory-files.html), [Windowed reading and writing](https://rasterio.readthedocs.io/en/latest/topics/windowed-rw.html).


**opencv** 

- https://docs.opencv.org/4.5.3/index.html (Colab uses version 4.1.2)
- [Thresholding](https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html)
- [Contours](https://docs.opencv.org/4.5.2/d3/d05/tutorial_py_table_of_contents_contours.html)

**scikit-image** 

- https://scikit-image.org/


**Miscellaneous**

A very interesting [StackOverflow Thread](https://stackoverflow.com/questions/56905592/automatic-contrast-and-brightness-adjustment-of-a-color-photo-of-a-sheet-of-pape) about "Automatic Contrast and Brightness Adjustment".

[StackOverflow Thread](https://dsp.stackexchange.com/questions/2411/what-are-the-most-common-algorithms-for-adaptive-thresholding) on Common Adpative Thresholding Algorithms.

[StackOverflow Thread](https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv) on detecting lines and connecting them.


**Additional Resources**: 

- Annotation tool suggested by NYU Librarian [Andrew Battista](https://library.nyu.edu/people/andrew-battista/): [Allmaps](https://observablehq.com/@bertspaan/using-allmaps-to-draw-geojson-on-a-iiif-image).



