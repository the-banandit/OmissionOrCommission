## Master Thesis 
This addition to the [News-Relations library](https://github.com/fhamborg/NewsRelations) enables you to compare cooccurrences of different news-outlets and run statistical analysis on them, with the aim of detecting **bias by omission or comission**.


## Motivation
This project is based on the NewsRelations library and seeks to prove, that co-occurrences of entities between different news-outlets could be feasible to detect bias by omission or commission and cluster similar-slant news-outlets together.

 
## Features


## Code examples
<!-- Include **very short code examples** that show what the project does as **concisely** as possible. Developers should be able to figure out **how** your project solves their problem by looking at the code examples. Make sure the API you are showing off is intuitive, and that your code is short and concise. See the [news-please project](https://github.com/fhamborg/news-please/blob/master/README.md#use-within-your-own-code-as-a-library) for example. -->

## Installation
The project can run within the notebook, if an Anaconda environment is installed.

Additional requirements are:
[NewsRelations](https://github.com/fhamborg/NewsRelations) >= 0.0.1  
[news-please](https://github.com/fhamborg/news-please) >= 1.2.28  
[stats-models](https://github.com/statsmodels/statsmodels) >= 0.11.1   


## API reference
<!-- For small projects with a simple enough API, include the reference docs in this README. For medium-sized and larger projects, provide a link to the API reference docs.-->

## Tests (optional: only if you have tests)
<!-- Describe and show how to run the tests with code examples.-->

## How to use and extend the project? (maybe)
<!-- Include a step-by-step guide that enables others to use and extend your code for their projects. Whether this section is required and whether it should be part of the `README.md` or a separate file depends on your project. If the **very short** `Code Examples` from above comprehensively cover (despite being concise!) all the major functionality of your project already, this section can be omitted. **If you think that users/developers will need more information than the brief code examples above to fully understand your code, this section is mandatory.** If your project requires significant information on code reuse, place the information into a new `.md` file.-->


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


### Results
Hypothesis 1.1:
|            | Precision | Recall | F1-score | Support |
|------------|-----------|--------|----------|---------|
| same-slant | 1.0000    | 0.7222 | 0.8387   | 18      |

Hypothesis 1.2:
|                 | Precision | Recall   | F1-score | Support |
|-----------------|-----------|----------|----------|---------|
| different-slant | 1.0000    | 0.2593   | 0.4118   | 54      |

Combined results:
|                 | Precision | Recall | F1-score | Support |
|-----------------|-----------|--------|----------|---------|
| different-slant | 0.7368    | 0.2593 | 0.3836   | 54      |
| same-slant      | 0.2453    | 0.7222 | 0.3662   | 18      |

Hence, hypothesis 1 got rejected.



<!-- If you performed evaluations as part of your project, include your preliminary results that you also show in your final project presentation, e.g., precision, recall, F1 measure and/or figures highlighting what your project does. If applicable, briefly describe the dataset your created or used first before presenting the evaluated use cases and the results.

If you are about to complete your thesis, include the most important findings (precision/recall/F1 measure) and refer to the corresponding pages in your thesis document.-->

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use it except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](https://github.com/the-banandit/MasterThesis/blob/master/LICENSE).
