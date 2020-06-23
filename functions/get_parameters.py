import pandas as pd
import nltk.data
import pyLDAvis

from tqdm import tqdm_notebook, tnrange, tqdm
from newsrelations.query_db.relation_query import DBQueryHandlerCoocc
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from gensim import models, corpora, similarities

nltk.download("stopwords")
tokenizer = nltk.data.load("/home/jonas/anaconda3/lib/python3.7/nltk_data/punkt/english.pickle")

stop_words = set(stopwords.words("english"))
# extend stopwords with typical stopwords from news-paper articles
extend_stop_words = ["also", "said", "one", "new", "two", "says", "could", "would", "should", "three", "three", "like"]
for word in extend_stop_words:
    stop_words.add(word)



class getParameters:
    def __init__(self, relation_models_path, model):
        self.relation_models_path = relation_models_path
        self.model = model

    def create_tf_idf_table(self):
        """
        This function calculates the TF-IDF value over all words mentioned in the [model]s corpus.
        
        input:      relation_models_path = string
                    realtion_model = string
        
        output:     df = DataFrame (containing all tf-idf-values for each word)
        """
        # number of top words in corpus
        N = 10
        
        # initialize db_handler
        db_handler = DBQueryHandlerCoocc(self.relation_models_path, self.model)
        # retrieve all articles from database into article
        articles = db_handler.get_articles()


        preprocessed_articles = ""

        # preprocessing of articles
        for article in tqdm(articles):
            # get text, lower it and tokenize it into sentences, strip punctuation and stop words
            single_article = str(article.text)
            single_article = single_article.lower()
            single_article = word_tokenize(single_article)
            single_article = [word for word in single_article if word.isalnum()]
            single_article = [word for word in single_article if not word in stop_words]

            # concat everything into a string again 
            art = ""
            for word in single_article:
                art = art + " " + word
            # append to corpus-string   
            preprocessed_articles = preprocessed_articles + " " + art    
        preprocessed_articles = [preprocessed_articles]
        
        # calculate TF-IDF
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(preprocessed_articles)
        names = vectorizer.get_feature_names()
        data = vectors.todense().tolist()

        # Create a dataframe with the results
        df = pd.DataFrame(data, columns=names)
        df = df[filter(lambda x: x not in list(stop_words) , df.columns)]
        """
        for i in df.iterrows():
            print(i[1].sort_values(ascending=False)[:N])
        """    
        return df
        
        
        
    def LDA(self, number_of_topics):
        """
        This function conducts a LDA on a given [model]
        
        input:     relation_models_path = str
                   model = str
                   
        output:    lda-model = model (for further use in LDAvis)
        """

        # initialize database handler
        db_handler = DBQueryHandlerCoocc(self.relation_models_path, self.model)
        # retrieve all articles from database into article
        articles = db_handler.get_articles()

        preprocessed_articles = []
        # preprocessing of articles
        for article in tqdm(articles):
            # get text, lower it and tokenize it into sentences, strip punctuation and stop words
            single_article = article.text
            single_article = single_article.lower()
            single_article = word_tokenize(single_article)
            single_article = [word for word in single_article if word.isalnum()]
            single_article = [word for word in single_article if not word in stop_words]

            preprocessed_articles.append(single_article)

        dictionary = corpora.Dictionary(preprocessed_articles)

        # creating the corpus
        corpus = [dictionary.doc2bow(text) for text in preprocessed_articles]

        # train the lda model on the corpus of all posts
        lda = models.LdaMulticore(corpus, id2word=dictionary, num_topics=number_of_topics)

        return lda, corpus, dictionary



    def chi_squared(self, contingency_table, print_orig = False, print_expect = False, print_chi_contr = False):
        """
        This function conducts a chi-squared test of independence between the different rows of a contingency table
        
        input: contingency_table
        
        ouput: None
        """
        contingency_table = sm.stats.Table(contingency_table)
        results = contingency_table.test_nominal_association()
        
        
        # orig contingency table
        if print_orig == True:
            print("Original contingency table:")
            print(contingency_table.table_orig)
        # expected values
        if print_expect == True:
            print("\nExpected values:")
            print(contingency_table.fittedvalues)
        # chi-squared contributions
        if print_chi_contr == True:
            print("\nChi-square contributions:")
            print(contingency_table.chi2_contribs)
        
        # results
        print("\nResults:")
        print(results)

       
        return
        
        
        
        
    def do_chi_squared_comparison(self, topic_of_interest, no_entities):
        """
        This function extracts chi-squared test results for all combinations of news-outlets
        
        input: contingency_table
        
        ouput: None
        """

        # extracting a contingency table from a single reference entity
        i = 0
        j = 0

        df_results = pd.DataFrame()

        for i in range(len(relation_models)):
            for j in range(len(relation_models)):
                models = []
                models = [relation_models[i]] + [relation_models[j]]

                contingency_table = build_contingency_table_from_single_topic(
                    relation_models_path, models, topic_of_interest, no_entities
                )

                contingency_table = sm.stats.Table(contingency_table)
                results = contingency_table.test_nominal_association()

                df_results[
                    str(relation_models[i][-10:-7])
                    + " - "
                    + str(relation_models[j][-10:-7])
                ] = [
                    results.statistic,
                    results.pvalue,
                ]

        df_results = df_results.transpose()
        df_results = df_results.rename(columns={0: "chi_sq", 1: "p_value"})
        df_results

        return df_results


