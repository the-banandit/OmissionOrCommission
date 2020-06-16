## Master Thesis 
Application of the [News-Relations library](https://github.com/fhamborg/NewsRelations) enables you to compare cooccurrences of different news-outlets and run statistical analysis on them, with the aim of detecting **bias by omission or comission**.


## Motivation
Bias by omission originates wanted or unwanted through discrepancies in the coverage of topics by different news-outlets. 
Within this thesis I want to evaluate whether the co-occurrences of entities are a feasible tool to identify bias by omission or commission, since discrepancies in co-occurrences could indicate discrepancies in coverage and therefore could be used to detect bias. 
As basis for this thesis I use the [News-Relations library](https://github.com/fhamborg/NewsRelations) to extract entites from a set of news-articles covering different news-outlets via a delimited period (c.f. Datasets).

The jupyter-notebook can be read as a walkthrough through the experiments I conducted to examine my hypothesis.

<!-- 
## Code examples
 Include **very short code examples** that show what the project does as **concisely** as possible. Developers should be able to figure out **how** your project solves their problem by looking at the code examples. Make sure the API you are showing off is intuitive, and that your code is short and concise. See the [news-please project](https://github.com/fhamborg/news-please/blob/master/README.md#use-within-your-own-code-as-a-library) for example. -->

## Installation
The project can run within the notebook, if an Anaconda environment is installed.

Additional requirements are:
[NewsRelations](https://github.com/fhamborg/NewsRelations) >= 0.0.1  
[news-please](https://github.com/fhamborg/news-please) >= 1.2.28  
[stats-models](https://github.com/statsmodels/statsmodels) >= 0.11.1

It is possible to apply the code on own databases, created with NewsRelations

<!--
## API reference
 For small projects with a simple enough API, include the reference docs in this README. For medium-sized and larger projects, provide a link to the API reference docs.-->

## Hypotheses

**Hypothesis 1**


1.1 Within same slant groups the co-occurring entities are independent from the news-outlet

1.2 Between different slant groups the co-occurring entities are dependent from the news-outlet
    
To check hypothesis 1 I ran chi-squared tests for same (1.1) and different-slant (1.2) news-outlets.
The results are matched with news-outlet groupings from literature. Accuracy, precision, recall and F1-score are estimated individually and combined.

**Hypothesis 2**
Goal of hypothesis 2 estimates whether there are other possibilities to categorize news-outlets into similar slant groups. 
Therefore a graph is constructed from the news-outlets. The news-outlets are represented by nodes, the edges by the chi-value of the news-outlet tuples. The chi-statistic was chosen, since it respects differences in the number of articles of the compared news-outlets.

The graphs were constructed as directed and undirected graphs.
For each Version the local clustering coefficient of each node was calculated after Opsahl and Panzarasa (2009).

**Hypothesis 3**
Since it is possible to cluster news-outlets via their co-occurrences, hypothesis 3 assumes, that a combination of sentiment analysis and the clustering by co-occurrences could identify slant groups.

First same-slant groups are identified by extracting only the sentiment of all co-occurring entities and the sentiment of their context. Therefore, scope (s) is defined that determines the number of sentences around the sentence in which a co-occurring entity is mentioned. The sentiment of all sentences within the scope is estimated.
Expirements are run with s=0 and s=1, since the likelihood of neutral sentiment increases with the number of analyzed sentences. The resulting vectors of each news-outlet and each co-occurring entity are clusterd via k-means into three groups 

<!-- 
## How to use and extend the project? (maybe)
Include a step-by-step guide that enables others to use and extend your code for their projects. Whether this section is required and whether it should be part of the `README.md` or a separate file depends on your project. If the **very short** `Code Examples` from above comprehensively cover (despite being concise!) all the major functionality of your project already, this section can be omitted. **If you think that users/developers will need more information than the brief code examples above to fully understand your code, this section is mandatory.** If your project requires significant information on code reuse, place the information into a new `.md` file.-->


## Datasets
The Results are based on two datasets scraped with [news-please](https://github.com/fhamborg/news-please) from [Common Crawl](http://commoncrawl.org/) and preprocessed with [NewsRelations](https://github.com/fhamborg/NewsRelations).

Calibration dataset for parameter tuning:

| news-outlet         | acronym | period                  | number of articles | news-segment | slant-group from literature |
|---------------------|---------|-------------------------|--------------------|--------------|------------------------------|
| Huffington Post     | HFP     | 2012-01-01 - 2012-03-01 | 4909               | news         | liberal                     |
| New York Times      | NYT     | 2012-01-01 - 2012-03-01 | 2541               | news         | liberal                     |
| Cable News Network  | CNN     | 2012-01-01 - 2012-03-01 | 2491               | news         | centre                      |
| Reuters             | RET     | 2012-01-01 - 2012-03-01 | 2135               | news         | centre                      |
| Fox News            | FXN     | 2012-01-01 - 2012-03-01 | 3784               | news         | conservative                |
| Wall Street Journal | WSJ     | 2012-01-01 - 2012-03-01 | 1215               | news         | conservative                |


Dataset to run experiments on:

| news-outlet                   | acronym | period                  | number of articles | news-segment | slant-group from literature |
|-------------------------------|---------|-------------------------|--------------------|--------------|-----------------------------|
| Cable News Network            | CNN     | 2011-01-01 - 2011-12-31 | 2652               | news         | centre                      |
| Chicago Tribune               | CTB     | 2011-01-01 - 2011-12-31 | 2843               | news         | conservative                |
| Fox News                      | FXN     | 2011-01-01 - 2011-12-31 | 6508               | news         | conservative                |
| Huffington Post               | HFP     | 2011-01-01 - 2011-12-31 | 14876              | news         | liberal                     |
| National Broadcasting Company | NBC     | 2011-01-01 - 2011-12-31 | 3958               | news         | centre                      |
| New York Times                | NYT     | 2011-01-01 - 2011-12-31 | 11281              | news         | liberal                     |
| Reuters                       | RET     | 2011-01-01 - 2011-12-31 | 16767              | news         | centre                      |
| Washington Post               | WPO     | 2011-01-01 - 2011-12-31 | 14814              | news         | liberal                     |
| Wall Street Journal           | WSJ     | 2011-01-01 - 2011-12-31 | 2522               | news         | conservative                |


## Results
**Hypothesis 1.1:**
|            | Precision | Recall | F1-score | Support |
|------------|-----------|--------|----------|---------|
| same-slant | 1.0000    | 0.7222 | 0.8387   | 18      |

**Hypothesis 1.2:**
|                 | Precision | Recall   | F1-score | Support |
|-----------------|-----------|----------|----------|---------|
| different-slant | 1.0000    | 0.2593   | 0.4118   | 54      |

**Combined results:**
|                 | Precision | Recall | F1-score | Support |
|-----------------|-----------|--------|----------|---------|
| different-slant | 0.7368    | 0.2593 | 0.3836   | 54      |
| same-slant      | 0.2453    | 0.7222 | 0.3662   | 18      |

Hypothesis 1 got rejected.

**Hypothesis 2**

![network structure](/images/network.png)

With the cluster coefficient of Opsahl and Panzarasa (2009) it was possible to estimate a cluster of NYT - RET - WPO, by using geometric mean and a boundary of 0.5. 


| news-outlet | cluster by <br>literature | cluster by<br>co-occurrences | cluster by<br>sentiment only | cluster by<br>sentiment and inverse<br>residual |
|-------------|---------------------------|------------------------------|------------------------------|-------------------------------------------------|
| CNN         | 1                         | 1                            | 0                            | 0                                               |
| CTB         | 2                         | 2                            | 0                            | 2                                               |
| FXN         | 2                         | 0                            | 1                            | 1                                               |
| HFP         | 0                         | 0                            | 0                            | 1                                               |
| NBC         | 1                         | 1                            | 2                            | 0                                               |
| NYT         | 0                         | 0                            | 0                            | 0                                               |
| RET         | 1                         | 0                            | 1                            | 0                                               |
| WPO         | 0                         | 0                            | 0                            | 0                                               |
| WSJ         | 2                         | 1                            | 0                            | 2                                               |


**Hypothesis 3**
The affiliation towards a certain slant group could not be proven by hypothesis 3.

## Literature

Opsahl, T., Panzarasa, P., 2009. Clustering in weighted networks. Social Networks 31 (2), 155-163

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use it except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](https://github.com/the-banandit/MasterThesis/blob/master/LICENSE).
