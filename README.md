## Omission or commission: Identifying media bias via an analysisof co-occurring entities
This extension to the [News-Relations library](https://github.com/fhamborg/NewsRelations) enables you to compare cooccurrences of different news-outlets and run statistical analysis on them, with the aim of detecting **bias by omission or comission**.

There are different possiblities to select the co-occurring entities, based on classical NLP methods.

If you are interested in the datasets please contact me via e-mail.

## Motivation
Bias by omission or commission describes the wanted or unwanted discrepancy of information between news-articles from different news outlets, covering the same topic. It manifests in the omission of perspectives or sources. Hence, it shows similarities to source-selection bias. 
Since co-occurrences carry additional infomation regarding the author's weighing of necessary content, they seem feasible for the detection of this form of media bias. 

The basis of this thesis is the [News-Relations library](https://github.com/fhamborg/NewsRelations), which extracts all co-occurrences of entities within a given corpus.
I use it to extract the co-occurrences of different corpora and quantitatively compare them. 
Based on this I can derive the relation of corpora and the likelihood of an affiliation towards a similar slant group. 

The jupyter notebook contains the application of all code and can call and reproduce all results I produced within this thesis. 


## Installation
The code can run witin a Anaconda 3 environment. 

Additional requirements are:

[NewsRelations](https://github.com/fhamborg/NewsRelations) >= 0.0.1  
[news-please](https://github.com/fhamborg/news-please) >= 1.2.28  
[stats-models](https://github.com/statsmodels/statsmodels) >= 0.11.1

It is possible apply the code on different databases, if they were gathered with News-Relations.


## Datasets
My results are based on two datasets scraped with [news-please](https://github.com/fhamborg/news-please) from [Common Crawl](http://commoncrawl.org/) and preprocessed with [NewsRelations](https://github.com/fhamborg/NewsRelations).
The datasets can be found and downloaded [here](https://tinyurl.com/banandit-thesis-datasets).

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



## Content

The primary objective of this project is to cluster different corpora into similar slant groups analysing co-occurrences of entities.

Therefore, this approach heavily relies on the selected entities for co-occurrence extraction. 
I ran different approaches on the selection entities, featuring classical methods from NLP.

I applied: 

**TF-IDF** on every corpus and extracted the top *n* occurring entities.

**LDA** on every corpus to find *m* topics and selected the top *n* entities describing those topics.

A **Reference entity** and extraced *n* co-occurring entities for every constellation of corpus tuples.

**Manually selected** entities by reading through the outer spectrum of the different slant groups and selected entities with a high likelihood of being covered ambivalently within different slant groups. (I repeated this process two times with no major differences.


After extracting the co-occurring entities I processed every constellation of corpus-pairing from my dataset and calculated the chi-statistic and hence the relation/dependence of the different corpora. 
The results can be seen below.

Finally, I clustered all corpora based after creating a undirected, interconnected, weighted network-stucture.
I chose the chi-statistics as weights for the edges and clustered everything with Opsahl's clustering coefficient.
I chose the cluster affiliation threshold of the coefficient to be a fraction of the maximum occurring clustering coefficient. 
The results can be seen below. 

<!--For further reading see [this](https://thesisLink.com)-->



## Results
For each approach of entitiy extraction I calculated the accuracy, precision, recall and F1 score.

| entity extraction<br>approach     | accuracy | precision | recall | F1-score |
|-----------------------------------|----------|-----------|--------|----------|
| TF-IDF                            | 0.2500   | 0.1250    | 0.5000 | 0.2000   |
| LDA argmax                        | 0.5278   | 0.5278    | 0.5370 | 0.4963   |
| top n<br>co-occurring<br>entities | 0.6250   | 0.5089    | 0.5093 | 0.5090   |
| manual extraction 1               | 0.5834   | 0.5000    | 0.5000 | 0.4958   |
| manual extraction 2               | 0.4444   | 0.5151    | 0.5185 | 0.4375   |



| metric     | clusters <br>(threshold <br>$ c = 0.5 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.75 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.8 * c_{\omega}$) | clusters <br>(threshold <br>$ c = 0.9 * c_{\omega}$) |
|------------|------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| argmin     | CTB , FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ | FXN, CNN, CTB, <br>RET, WPO, HFP                      | FXN, CNN, CTB,<br>HFP                                | FXN, CNN, CTB,<br>HFP                                |
| argmax     | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CNN, RET, WPO, <br>WSJ, CTB, NBC,                     | WSJ, RET, WPO                                        | WSJ, RET, WPO                                        |
| arithmetic | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CTB, RET, WPO,<br>FXN, CNN, HFP,<br>WSJ               | HFP, CNN, CTB                                        | HFP, CNN, CTB                                        |
| geometric  | CTB, FXN, HFP, <br>RET, WPO, CNN, <br>NBC, NYT, WSJ  | CTB, RET, WPO<br>FXN, CNN, HFP, <br>NBC, WSJ          | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         | FXN, CNN, CTB,<br>HFP, <br><br>WSJ, RET, WPO         |




## How to extend the project?

This project can be easily extended by different approaches of selecting entities for co-occurrence analysis. 
Especially an integration of ideology- or bias-terms, e.g. in combination with the LDA approach could lead to better results.


## Literature

Opsahl, T., Panzarasa, P., 2009. Clustering in weighted networks. Social Networks 31 (2), 155-163

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use it except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](https://github.com/the-banandit/MasterThesis/blob/master/LICENSE).
