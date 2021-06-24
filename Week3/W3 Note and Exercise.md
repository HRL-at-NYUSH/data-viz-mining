## W3 - Special Data

This note is based on the special data presentation this week. You can find a copy of the deck in the same folder as this note. 

### 1. What are date types and why care?

In the past two weeks, we have discussed visualization theory, data cleaning workflow, as well as exploratory data analysis. One essential element of the different topics is **data type**. We need to know what kind of data type in order to design effective **visual encoding**; when cleaning and managing datasets, data type information is critical to **data modeling**. 

So how many data types are out there? One popular categorization is the measurement typology proposed by Harvard Psychologist Stanley Smith Stevens in the 1960s. 

Here I quote the summary of Stevens' typology by Jeff Hale in [his medium article](https://towardsdatascience.com/7-data-types-a-better-way-to-think-about-data-types-for-machine-learning-939fae99a689) on data types.

> - **Ratio** (equal spaces between values and a meaningful zero value — mean makes sense)
- **Interval** (equal spaces between values, but no meaningful zero value — mean makes sense)
- **Ordinal** (first, second, third values, but not equal space between first and second and second and third — median makes sense)
- **Nominal** (no numerical relationship between the different categories — mean and median are meaningless)

If we look at popular data visualization platforms, here is the data types on [Tableau](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm). 

<img src="./images/tableau_data_types.png" alt="tableau_data_types" width="600"/>

Note: The documentation site of Tableau is quite comprehensive and there are a lot to learn in temrs of platform visual design and visualization workflow.

Here is the interface of the academic exploratory data visualization platform [Voyager 2](https://vega.github.io/voyager2). 

<img src="./images/voyager2.png" alt="voyager2" width="500"/>

The platform categorized different fields into three categories: `Categorical`, `Temporal`, `Quantitative`. 

One common observation is that the common data types are mostly **numeric** (quantitative or ratio / interval or date time) or **simple text with limited options** (categorical or nominal / ordinal). 

### 2. So why some data types are more popular and what is special data?

The data types we see above are often referred to as "**structured data**". These kinds of data have several good features, see the diagram below from [Lawtomated.com](https://lawtomated.com/structured-data-vs-unstructured-data-what-are-they-and-why-care/). 

<img src="./images/unstructured.png" alt="unstructured" width="600"/>

The comparison above are mainly about data storage and management. It's worth noting that **special data** (or unstructured data) such as images, raw texts, and geospatial information are also **harder to analyze** (because most statistical and data analysis tools are designed for the structured data types) **and visualize** (although we do have a few specialized charts like word clouds). 

### 3. What special data do we have for the HRL projects?

#### Textual Data

<img src="./images/textual_data.png" alt="textual_data" width="500"/>

#### Visual Data

For historical street views, check out this brilliant interactive website called [Old NYC](https://www.oldnyc.org) by Dan Vanderkam. Note that each photo has description on the back of its original copy, thus this data source is visual, textual, and spatial at the same time. I have collected the image dataset through NYPL space-time directory project, contact me if you are interested.

For tax photos, please visit the [NYC Municipal Archives Collections](https://nycma.lunaimaging.com/luna/servlet/NYCMA~5~5). There is also a great website called [1940s.nyc](https://1940s.nyc) by Julian Boilen. 

<img src="./images/visual_data.png" alt="visual_data" width="500"/>

#### Spatial Data

<img src="./images/spatial_data.png" alt="spatial_data" width="500"/>

### 4. How do we transform special data into structured data?

#### Textual Data

<img src="./images/textual_transform.png" alt="textual_tranform" width="500"/>

#### Visual Data

Data Mining of Visual Data would a pioneering work and a great piece of challenge to put your computer vision skills at work. This lends

I have collected [some academic papers](https://drive.google.com/drive/folders/1Xf0Hx3S7chVLQRJU7mz7xwt20mgYd3bn?usp=sharing) on semantic scene parsing of street views, building model reconstruction, real estate price estimation, etc. 

The [Distant Viewing Lab](https://www.distantviewing.org) have more general tools and resources for visual data mining for the Humanities.

<img src="./images/visual_transform.png" alt="visual_tranform" width="500"/>

#### Spatial Data

<img src="./images/spatial_transform.png" alt="spatial_tranform" width="500"/>


### 5. Transformation among special data

<img src="./images/transform_among_special_data.png" alt="transform_among_special_data" width="500"/>

<img src="./images/map_extraction.png" alt="map_extraction" width="500"/>

<img src="./images/ocr_process.png" alt="ocr_process" width="500"/>

### 6. Special data needs special handling

...


---
<br><br><br>

## W3 Exercise


- **Task 1:** Refine and polish your insight report from last week: Add necessary comments and streamline the narrative, such that a person who didn't attend the presentation can understand what you did and how you did it by reading through the notebook. 

> **Note:** Please update the link in the repo if you have made new updates. I will email you individual feedback on your reports on Friday night for your reference. By ***the middle of next week***, you should have a clean version of the report ready to share with the larger group. 

- **Task 2:** Based on resources about special data above, propose one piece of special data related work that you think 1) will most greatly enrich the data exploration experience, 2) attracts you the most.

	When proposing the idea, please describe: 
	
	1. Which dataset(s) do you plan to use
	2. What kind of transformation you want to apply
	3. How will the outcome be utilized in data exploration (why is it important)
	4. Why you are excited about this work
	5. To what extent do you need to / want to learn new skills to carry out this work

> **Note:** Note that you don't have to stick to this idea for your individual project starting July. You can also propose an idea that might be above your current skill level but sounds very interesting to you. This exercise is meant to encourage you to think more about the rich possibilities with special data, and broaden your pool of choices before you decide on the topic of your mini-project. No formatting requirements for this one, but a basic Google Doc organized by the prompt questions is recommended.
