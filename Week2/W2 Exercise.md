## W2 - Exercise


*Last week*, we explored the Census data and shared about the interesting insights we found in the data. 
*This week*, we will go one step further to visualize and document the insight. 

Please organize your discussion, explanation, and visualization into a report, in the format of **Colab notebook** or **Google Doc**. The materials you are creating now can be polished and turned into public-facing **data stories**, so it's a great chance to showcase your critical thinking and enrich your portfolio.

****

Here are a few prompt questions to help you structure your report:

1. **What is an interesting insight you found?**
	- Don't be afraid to make an *argument*, but be prepared to back it up.
	- Describe it in *details*. Consider 5W1H: when, where, who, what, why, how.

2. **Why do you think it is interesting?**
	- 	There are many ways to define interesting insights, here I will quote the definition by [C. North et al.](https://ieeexplore.ieee.org/document/1626178) to give us some inspiration.

	>   - **Complex**: Insight is complex, involving all or large amounts of the given data in a synergistic way, not simply individual data values.
	>  	- **Deep**: Insight builds up over time, accumulating and building on itself to create depth. Insight often gen- erates further questions and, hence, further insight.
	>  	- **Qualitative**: Insight is not exact, can be uncertain and subjective, and can have multiple levels of resolution. 
	>  	- **Unexpected**: Insight is often unpredictable, serendip-
itous, and creative.
	>  	- **Relevant**: Insight is deeply embedded in the data
domain, connecting the data to existing domain knowledge and giving it relevant meaning. It goes beyond dry data analysis, to relevant domain impact.

	- More readings on what defines insight are available in the Appendix.

3. **How can you use visualizations to show/explain the insight?**
	- Places to find different chart types
		- [From Data to Viz](https://www.data-to-viz.com) "leads you to the most appropriate graph for your data. It links to the code to build it and lists common caveats you should avoid."
		- [Data Viz Project](https://datavizproject.com) "try to present all relevant data visualizations, so you can find the right visualization and get inspired how to make them."
		- The sources above are two of the most comprehensive and logical chart selection guides I find on the Internet. You are encouraged to look for more and nominate new ones by creating a PR to this repo. 
	- What charts would you use and why? 
		- What are the **characteristics** of the data?
		- What is the **concept/function** you wish to visualize?
		- Is your insight correctly and fully conveyed through the chosen visualization? Does the visualization imply extra information that is not intended?
		- Try at least **one more chart type** for the same data and explain  the pros and cons of different options.
		- Will interactivity and animation help convey the message? 

4. **What are the reasons that explain this insight? What are your assumptions?**
	- Challenge yourself by asking if the insight you found really exists? Or is it simply due to improper framing and calculation methods? 
		- Example: The absolute number of X in group A may be higher than in group B, but maybe the proportion of X in group B is higher.
	- Reflect on the implicit assumptions you made, how will they affect the robustness of your argument? 
		- Example: Did I assume that the best proxy for "ethnic group" is "birthplace"? Is "father/mother's birthplace" better? Should "immigration year" matter?
	- Try to come up with several potential explanation of the observed phenomenon in data. Think of some strategies to verify them and test out the strategies to the best you can.
	- List some future directions that you want to explore as the next steps. You are encouraged to read related History literature to provide some historical context as well.

<br>

> **Note 1:** Please add the link of your Notebook or Doc to ***the sectoin below*** by <span style="color:orange">the noon of next Tuesday (June 22, 2021)</span>. You can continue refining the report after the meeting but please share the main parts on time so that we can preview and discuss over the meeting. 

> **Note 2:** If you encounter technical difficulties and couldn't find solutions elsewhere, feel free to contact me via email or post a question on Slack. Here is a guide from Stack Overflow that talks about [How to Ask a Good Question](https://stackoverflow.com/help/how-to-ask).

> **Note 3:** For datasets, you should have access to the Google Drive folder (named *data\_2021\_may*). A useful resource is the [Census Data Codebook](https://docs.google.com/document/d/1YHucLq-P9GwJL08nWL9o1AerlMhVBtizKa1NOl8GgXE/edit?usp=sharing).

<br>

****

### Insight Reports

- [Data Exploration on Population Movements and Italian Immigrants - Amanda Huang](https://nbviewer.jupyter.org/gist/Oysters1874/fdd0e259c59b52d46810f334d6c49eeb)

> In my insight report, based on the census data of a specific year, I would like to explore the distribution of immigrants' birth countries and the overall trends of population movements. I draw the world map with pyechart and use different colors to encode the number of immigrants. Adding dynamic lines can make the visualization more vivid. But it may be more efficient to encode the number through the thickness of the lines, however, I haven't figured out how to do it with pyechart.

> I also want to study the characteristics of Italian immigrants and their living conditions in the United States, by analyzing their age distributions, literacy rate, naturalization status, and occupations. I have used bar chart, stacked bar chart, and heat map to visualize it. By using the module Altair, it is easy to add the tooltip, therefore enhancing the interactivity. Stacked bar charts will be a good choice when we need to show the quantitative difference between different groups. It is very intuitive and can deliver accurate data information.

- [Fixing Stereotype or Not? Gender vs Occupation - Simon Bian](https://colab.research.google.com/drive/1vu1bShkzQ0iE3dTOZIyR-q-zSQaO0uaK?usp=sharing)

> With regards to previous scattered, case-by-case discussions on feminization in certain fields, this insight aims to explore how feminization in the most popular types of jobs has a relationship with job prestige. The data that I chose is the top 20 most occupied jobs given in the US census data from 1880 to 1940, as well as the data from the National Opinion Research Center (NORC) to provide a quantitative evaluation of certain occupations. Using the former, 20 jobs instead of all jobs, can lower the running time and eliminate jobs that appear owing to data errors. Using the latter, the arbitrary classification of jobs could be halted and more quantitative and less subjective results will be yielded. The final product is a scatterplot in which for each dot, its size varies with respect to the number of workers in certain fields, its coloration varies by the degree of confidence level we put in, its x-axis being a normalized scale of occupation prestige, and the y axis is a result yielded from regression analysis of women participation rate over years. The conclusion reached by this exploration is that in positions of higher social status, feminization plays a role. In spite of this, in positions contrary to higher perceived social statuses, feminization has mixed roles. It does not merely shift women towards the lower pay - as negative correlation and positive correlation constitute the two poles observed in the above graph.

- [Profiles of Literate NYC Residents - Veronica Hu](https://colab.research.google.com/drive/1o3ub0rwH4w8nut8iG27aodEkHA-FM-lb?usp=sharing)

> I started my exploration over the datasets by looking into the education background of NYC residents across different times. Since there are two special columns named "Can Read" and "Can Write," I thought an exploration centering these two fields may bring further insights about the relationship of education, literacy rate and other background of the residents, e.g. their occupations, gender and distribution, etc. 
> 
> Since different data types can be represented and compared through different charts/visualizations, the way I chose to visualize them depended on the characteristics of the columns/fields I was looking into. For example, to compare the gender proportion of people who can read&write, I used pie charts corresponding to each year. On the other hand, to compare the age distribution, I used kde (kernel density estimation) plots to show the density of different ages across different years. When it comes to occupations, I used bar charts to show the top 10 popular occupations of people who can read&write at different years. In this way, the charts can show the changes/no-changes in popular occupations across years, which also tells us the relationship between some occupations and the capabilities to read & write. In order to look into details of some occupations, I also drafted pie charts to represent the proportion of people who can read/write for a certain occupation and compare them among years. In the end, I summarized the statistics and information in a high-level bar chart, with color-coded bars representing different occupations that can read/speak English across different years. 

- [Changing Gender Composition of NYC Cooks - Tim Wu](https://colab.research.google.com/drive/1bz1Oykkjj_RmZ4qP_3l6glc5rk-TWLnh?usp=sharing)

> From 1860 to 1940, the gender composition of cooks in NYC had gradually transition from female-majority to male-majority. I want to explore what factors had driven this change. To answer the question, I used the demographic variables “Age”, “Marital Status”, “Birthplace” across the 9 censuses to depict the NYC cooks’ profile. To visually explore the data, I chose pie charts to show changing composition in “Gender” and “Marital Status”, I tried overlaid histograms with density curve to show “Age” distribution differences, and I wish I could use an animated bar chart to show the changing rankings of top ”Birthplaces” of cooks. Finally, with the help from the visualizations, I found that the reversed gender composition could be mainly caused by the shifting ethnic composition of the cooks. 

- [Data Exploration on Gender in "Relationship to Head of House" - Pamela Pan](https://colab.research.google.com/drive/1aGcd9dWKFJY_dc_kETsN88yEE8tr2IMB?usp=sharing)

- [Estimating Incomes of NYC Residents with LDA - Lucy Wu [Link to be added]](https://temp.com)

<br>
<br>

****

### Appendix

More readings on Insight, Visual Reasoning, and Visualization Evaluation: 

- [Toward measuring visualization insight. C. North et al. (2006)](https://www.semanticscholar.org/paper/Toward-measuring-visualization-insight-North/a5c76ac1c75da8e2d7e21cc602857ef3567b1f6c)
- [Defining Insight for Visual Analytics. R. Chang et al. (2009)](https://www.semanticscholar.org/paper/Defining-Insight-for-Visual-Analytics-Chang-Ziemkiewicz/b28ccb88c5fe7d728b0d7e5e426c9cf55ca26667)
- [From Visualization to Visually Enabled Reasoning. J. Meyer et al. (2010)](https://www.semanticscholar.org/paper/From-Visualization-to-Visually-Enabled-Reasoning-Meyer-Thomas/181ef6274ce08772d965d25669739ed3fbd7535e)
- [Value-driven evaluation of visualizations. J. Stasko. (2014)](https://www.semanticscholar.org/paper/Value-driven-evaluation-of-visualizations-Stasko/bf10c7c8f4e8b47e498fc67de3ad7fdf60f2fe20)
