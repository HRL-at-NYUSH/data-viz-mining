**The purpose of** this notebook is to survey the existing tools for Auto EDA and Auto ML in the Python ecosystem, as well as related research literature. The end goal is to apply these libraries to the EDA of large historical datasets.

**Selection criteria:**

- Relevant (auto machine learning with explainability)
- Fresh (active development happening within a year)
- Python-based (for better integration)
- Well-documented (detailed references)

## AutoEDA tools

Pool: https://github.com/mstaniak/autoEDA-resources#python-libraries

- DataPrep by Simon Fraser University Database Group: https://github.com/sfu-db/dataprep (various domain-knowledge-based cleaning, list eda plots according to data types of fields)
- Dora by Nathan Epstein: https://github.com/NathanEpstein/Dora (version snapshot and action logs, simple actions as functions)
- HoloViews by HoloViz: http://holoviews.org/getting_started/Introduction.html (create viz automatically using short data annotations, intuitive layout grammar, raw data and its viz linked at all time enableing iterative selection and exploration) (Extensible with the [HoloViz Suite](https://holoviz.org/index.html))
- AutoViz from AutoViML: https://github.com/AutoViML/AutoViz (single line to get various visualization baesd on data types, sample randomly when data is large) (Extensible with the [AutoViML Suite](https://github.com/AutoViML))
- SweetViz by Francois Bertrand (author of Pandas-Profiling): https://github.com/fbdesignpro/sweetviz (Target analysis, compare distinct datasets, type inference, mixed-type associations for numerical (Pearson's correlation), categorical (uncertainty coefficient) and categorical-numerical (correlation ratio))
- dabl (data analysis baseline library) by Andreas Mueller: https://dabl.github.io/0.2.2/api.html (automatic plots for classification and regression (based on data types) and function to explain estimator)

## AutoML tools

(AutoML tools with explainability features are included)

Pool: https://github.com/windmaple/awesome-AutoML#tools-and-projects

- Auto_ml by Preston Parry: https://github.com/ClimbsRocks/auto_ml (specify column types, ml for analytics mode)
- AutoGluon by AWS Labs: https://github.com/awslabs/autogluon (handle texts and images in addition to tabular)
- FLAML by Microsoft: https://github.com/microsoft/FLAML (economical search, light-weight models)
- mljar-supervised by MLJar: https://github.com/mljar/mljar-supervised (decision trees visualization, permutation importances and SHAP)
- TPOT by Epistasis Lab at UPenn: https://github.com/EpistasisLab/tpot (optimizes ML pipelines using genetic programming, generate baseline codes)
- auto-sklearn by AutoML-Freiburg-Hannover: https://github.com/automl/auto-sklearn (combine meta learning, bayesian optimizer, greedy algorithm, etc, has support for explainability)

<br><br><br>


The section below are excerpt from "https://github.com/mstaniak/autoEDA-resources"

---

### Methods and tools for autoEDA

- [Interactive Data Exploration with “Big Data Tukey Plots”](http://www.absolutedc.com/resources/pdf/tukey.pdf) - automated visualization of big data.
- [Extracting Top-K Insights from Multi-dimensional Data](http://www4.comp.polyu.edu.hk/~csbtang/pub/SIGMOD17_insight.pdf).
- [Agency plus Automation: Designing Artificial Intelligence into Interactive Systems](http://idl.cs.washington.edu/files/2019-AgencyPlusAutomation-PNAS.pdf)
- [The Landscape of R Packages for Automated Exploratory Data Analysis](https://journal.r-project.org/archive/2019/RJ-2019-033/RJ-2019-033.pdf)
- [Issues in Automating Exploratory Data Analysis](https://pdfs.semanticscholar.org/ce09/ef8113c473e78c1896989d6ab6dd01fa9706.pdf)
- [Automating anomaly detection for exploratory data analytics](https://ieeexplore.ieee.org/abstract/document/8365228)
- [Task-Oriented Optimal Sequencing of Visualization Charts](https://arxiv.org/abs/1908.02502)
- [A Rank-by-Feature Framework for Interactive Exploration of Multidimensional Data](https://www.cs.umd.edu/hcil/hce/presentations/seo_shneiderman_rff_ivs.pdf) - A paper that describe many measures that can be used to sort 1d and 2d data displays.
- [Towards a benefit-based optimizer for Interactive Data Analysis](http://ceur-ws.org/Vol-2324/Paper16-PMarcel.pdf)
- [Spotfire: an information exploration environment](https://dl.acm.org/citation.cfm?id=245893)
- [AlphaClean: Automatic Generation ofData Cleaning Pipelines](https://arxiv.org/pdf/1904.11827.pdf)
- [Testing MS Excel's autoEDA tool](https://medium.com/datadriveninvestor/automated-exploratory-data-analysis-test-driving-ms-excels-ideas-feature-514f34d944e8#9cad-50ae56ae88ac)

### Visualization recommendation frameworks

- [Foresight: Recommending Visual Insights](http://www.vldb.org/pvldb/vol10/p1937-parthasarathy.pdf) - Foresight is a system that helps the user rapidly discover visual insights from large high-dimensional datasets.
- [DIVE: A Mixed-Initiative System Supporting Integrated Data Exploration Workflows](https://www.usedive.com/assets/DIVE_HILDA_2018.pdf). The web app is available on [MIT website](https://www.usedive.com/).
- [Voyager: Exploratory Analysis via Faceted Browsing of Visualization Recommendations](https://ieeexplore.ieee.org/document/7192728).
- [Voyager 2: Augmenting Visual Analysis with Partial View Specifications](https://idl.cs.washington.edu/files/2017-Voyager2-CHI.pdf)
- [VizML: A Machine Learning Approach to Visualization Recommendation](https://dl.acm.org/citation.cfm?id=3300358)
- [VizDeck: Streamlining Exploratory Visual Analytics of Scientific Data](https://faculty.washington.edu/billhowe/publications/pdfs/perry2013vizdeck.pdf)
- [Taggle: Scalable Visualization of Tabular Data through Aggregation](https://sci.utah.edu/~vdl/papers/2017_preprint_taggle.pdf)

### Augmented analytics

- [Augmenting Visualizations with Interactive Data Facts to Facilitate Interpretation and Communication](https://arjun010.github.io/static/papers/voder-infovis18.pdf).

### Conference presentations

- [Automating exploratory data analysis tasks with eda - Billy Buchanan](https://wbuchanan.github.io/stataConference2018/)

---