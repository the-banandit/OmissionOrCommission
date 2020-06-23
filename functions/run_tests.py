import pandas as pd 
import statsmodels.api as sm

from tqdm import tqdm_notebook, tnrange, tqdm
from create_contingency_tables import createContingencyTables


class runTests:
    def __init__(self, relation_models_path, relation_models, topic_of_interest="placeholder", number_of_entities):
        self.relation_models_path = relation_models_path
        self.relation_models = relation_models
        self.topic_of_interest = topic_of_interest
        self.number_of_entities = number_of_entities

    def estimate_n(self, models):
        handler = createContingencyTables(self.relation_models_path, self.relation_models)
        
        df_results = pd.DataFrame()      
        description = str(str(models[0][-10:-7]) + "-" + str(models[1][-10:-7]))
        # loop through entity numbers until max entity is reached
        for n in tnrange(1, self.number_of_entities, desc=description):
            # create SQL query and build contingency table for sm.stats
            contingency_table = handler.build_contingency_table_from_single_topic(
                self.topic_of_interest, n
            )
            contingency_table = sm.stats.Table(contingency_table)
            # calculate results + add them to dataframe
            results = contingency_table.test_nominal_association()
            df_results[n] = [results.pvalue]

        df_results = df_results.transpose()
        df_results = df_results.rename(columns={0: description})
        
        return df_results



    def estimate_optimal_reference_entity(self, topic):
        # loop through model constellation in models list
        # for constellation in tqdm(models):
        handler = createContingencyTables(self.relation_models_path, self.relation_models)

        df_results = pd.DataFrame()
        description = str(str(self.relation_models[0][-10:-7]) + "-" + str(self.relation_models[1][-10:-7]))
        # loop through entity numbers until max entity is reached
        for n in tnrange(1, self.number_of_entities, desc=topic):
            try:
                # create SQL query and build contingency table for sm.stats
                contingency_table = handler.build_contingency_table_from_single_topic(
                    self.topic_of_interest, n
                )
                contingency_table = sm.stats.Table(contingency_table)
                # calculate results + add them to dataframe
                results = contingency_table.test_nominal_association()
                df_results[n] = [results.pvalue]
            except:
                print("There is too little data for " + topic)
                break

        df_results = df_results.transpose()
        df_results = df_results.rename(columns={0: topic})

        return df_results


 

