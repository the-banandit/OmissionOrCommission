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

## Approaches

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

| news-outlet         | acronym | period                     | number of articles  | avg. article length | news-segment | slant-group from literature |
|---------------------|---------|----------------------------|---------------------|---------------------|--------------|-----------------------------|
| Cable News Network  | CNN     | 2012-01-01 -<br>2012-12-31 | 4.909               | 824                 | news         | centre                      |
| Fox News            | FXN     | 2012-01-01 -<br>2012-12-31 | 3.784               | 499                 | news         | conservative                |
| Huffington Post     | HFP     | 2012-01-01 -<br>2012-12-31 | 4.909               | 559                 | news         | liberal                     |
| New York Times      | NYT     | 2012-01-01 -<br>2012-12-31 | 2.541               | 846                 | news         | liberal                     |
| Reuters             | RET     | 2012-01-01 -<br>2012-12-31 | 2.135               | 722                 | news         | centre                      |
| Wall Street Journal | WSJ     | 2012-01-01 -<br>2012-12-31 | 1.215               | 499                 | news         | conservative                |



Main dataset:

| news-outlet                      | acronym | period                     | number of articles  | avg. article length | news-segment | slant-group from literature |
|----------------------------------|---------|----------------------------|---------------------|---------------------|--------------|-----------------------------|
| Cable News Network               | CNN     | 2011-01-01 -<br>2011-12-31 | 2.652               | 822                 | news         | centre                      |
| Chicago Tribune                  | CTB     | 2011-01-01 -<br>2011-12-31 | 2.843               | 538                 | news         | conservative                |
| Fox News                         | FXN     | 2011-01-01 -<br>2011-12-31 | 6.508               | 704                 | news         | conservative                |
| Huffington Post                  | HFP     | 2011-01-01 -<br>2011-12-31 | 14.876              | 556                 | news         | liberal                     |
| National Broadcasting<br>Company | NBC     | 2011-01-01 -<br>2011-12-31 | 3.958               | 367                 | news         | centre                      |
| New York Times                   | NYT     | 2011-01-01 -<br>2011-12-31 | 11.281              | 858                 | news         | liberal                     |
| Reuters                          | RET     | 2011-01-01 -<br>2011-12-31 | 16.767              | 677                 | news         | centre                      |
| Washington Post                  | WPO     | 2011-01-01 -<br>2011-12-31 | 14.814              | 609                 | news         | liberal                     |
| Wall Street Journal              | WSJ     | 2011-01-01 -<br>2011-12-31 | 2.522               | 559                 | news         | conservative                |



## Results
For each approach of entitiy extraction I calculated the accuracy, precision, recall and F1 score.

 
| entity extraction<br>approach     | accuracy | slant-group<br>affiliation from <br>literature | precision | recall | F1-score |
|-----------------------------------|----------|------------------------------------------------|-----------|--------|----------|
| TF-IDF                            |          | same (n=18)                                    |           |        |          |
|                                   |          | diff (n=54)                                    |           |        |          |
| LDA argmax                        | 0.4722   | same (n=18)                                    | 0.2222    | 0.4444 | 0.2963   |
|                                   |          | diff (n=54)                                    | 0.7222    | 0.4815 | 0.5778   |
| top n<br>co-occurring<br>entities | 0.375    | same (n=18)                                    | 0.7468    | 0.2593 | 0.3836   |
|                                   |          | diff (n=54)                                    | 0.2453    | 0.7222 | 0.3662   |
| manual extraction 1               | 0.4167   | same (n=18)                                    | 0.75      | 0.3333 | 0.4615   |
|                                   |          | diff (n=54)                                    | 0.25      | 0.6667 | 0.3636  
| manual extraction 2               | 0.5556   | same (n=18)                                    | 0.2308    | 0.3333 | 0.2727   |
|                                   |          | diff (n=54)                                    | 0.7391    | 0.6296 | 0.68     |


<!--
for clustering: with 0.5
<!-- results clustering  --> 

| metric     | clusters <br>(threshold <br>$ c = 0.5 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.75 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.8 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.9 * c_{\omega}$) |
|------------|------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| argmin     | CTB , FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ | FXN, CNN, CTB, <br>RET, WPO, HFP                      | FXN, CNN, CTB,<br>HFP                                | FXN, CNN, CTB,<br>HFP                                |
| argmax     | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CNN, RET, WPO, <br>WSJ, CTB, NBC,                     | WSJ, RET, WPO                                        | WSJ, RET, WPO                                        |
| arithmetic | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CTB, RET, WPO,<br>FXN, CNN, HFP,<br>WSJ               | HFP, CNN, CTB                                        | HFP, CNN, CTB                                        |
| geometric  | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CTB, RET, WPO<br>FXN, CNN, HFP, <br>NBC, WSJ          | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         |


<!-- results clustering without 0.5 -->

| metric     | clusters <br>(threshold <br>$ c = 0.75 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.8 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.9 * c_{\omega}$) |
|------------|-------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| argmin     | FXN, CNN, CTB, <br>RET, WPO, HFP                      | FXN, CNN, CTB,<br>HFP                                | FXN, CNN, CTB,<br>HFP                                |
| argmax     | CNN, RET, WPO, <br>WSJ, CTB, NBC,                     | WSJ, RET, WPO                                        | WSJ, RET, WPO                                        |
| arithmetic | CTB, RET, WPO,<br>FXN, CNN, HFP,<br>WSJ               | HFP, CNN, CTB                                        | HFP, CNN, CTB                                        |
| geometric  | CTB, RET, WPO<br>FXN, CNN, HFP, <br>NBC, WSJ          | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         |




## Literature

Opsahl, T., Panzarasa, P., 2009. Clustering in weighted networks. Social Networks 31 (2), 155-163

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use it except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](https://github.com/the-banandit/MasterThesis/blob/master/LICENSE).
