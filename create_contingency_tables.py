import pandas as pd
import numpy as np
from newsrelations.query_db.relation_query import DBQueryHandlerCoocc
from newsrelations.helper_classes.synonym_handler import SynonymHandler
from newsrelations.metrics.distances import DistanceMeasure



class createContingencyTables:

    def __init__(self, relation_models_path, relation_models):
        self.relation_models_path = relation_models_path
        self.relation_models = relation_models


    def build_contingency_table_from_preset_cooccurrences(self, model, cooccurrences_list):
        """
        This function builds a contingency table from a input list of relation models generated with relation_miner.py 
        in regards to predetermined co_occurrences [co_occurrences_list].
        
        input:  model = str (name of reference model)
                co_occurrences_list = list of tuples
                
        output: contingency_table = pandas DataFrame [rows = different models, columns = entities]
        """
        E1_SYNSET = 0
        E2_SYNSET = 0

        # write first row of contingency_table
        contingency_table = pd.DataFrame(columns=[str(model)])

        # initialize db_handler()
        db_handler = DBQueryHandlerCoocc(self.relation_models_path, model)

        # buffer for cooccurrences
        co_occs = []
        # loop through all entities and get number of co-occurrences
        for single_tuple in cooccurrences_list:
            co_occs.append(
                len(
                    list(
                        db_handler.select_relations(
                            e1=single_tuple[0].lower(),
                            e2=single_tuple[1].lower(),
                            e1_is_synset=E1_SYNSET,
                            e2_is_synset=E2_SYNSET,
                        )
                    )
                )
            )

        contingency_table[str(model)] = co_occs

        # transpose the contingency table to get it into the right format
        contingency_table = contingency_table.transpose()
        return contingency_table


    def build_contingency_table_from_single_topic(self, topic_of_interest, no_entities=10):
        """
        This function builds a contingency table from a input list of relation models generated with relation_miner.py 
        in regards to predetermined topic [TOPIC_OF_INTEREST].
        The first model in [RELATION_MODELS] is the reference model all other models will be compared with.
        The function extracts the top [NO_ENTITIES] co_occuring entities from the model and builds a contingency table.
        
        input:  relation_models = list
                relation_models_path = str 
                topic_of_interest = str           
                no_entities = int (standard 10)
                
        output: contingency_table = pandas DataFrame [rows = different models, columns = entities]
        """
        E1_SYNSET = 0
        E2_SYNSET = 1

        # initialize DistanceMeasure with reference-model
        dm = DistanceMeasure(self.relation_models_path, str(self.relation_models[0]))

        # extract top NO_ENTITIES entities
        top = dm.get_top_co_occurrences(
            topic_of_interest,
            cutoff=no_entities,
            e1_is_synset=E1_SYNSET,
            e2_is_synset=E2_SYNSET,
        )
        # write first row of contingency_table
        contingency_table = pd.DataFrame(
            np.array([t[1] for t in top]),
            index=[t[0] for t in top],
            columns=[str(self.relation_models[0])],
        )

        # loop through all remaining models
        for model in self.relation_models[1:]:
            # initialize db_handler()
            db_handler = DBQueryHandlerCoocc(self.relation_models_path, model)

            # buffer for cooccurrences
            co_occs = []
            # loop through all entities and get number of co-occurrences
            for row in contingency_table.index:
                co_occs.append(
                    len(
                        list(
                            db_handler.select_relations(
                                e1=topic_of_interest.lower(),
                                e2=row.lower(),
                                e1_is_synset=E1_SYNSET,
                                e2_is_synset=E2_SYNSET,
                            )
                        )
                    )
                )

            contingency_table[str(model)] = co_occs

        # transpose the contingency table to get it into the right format
        contingency_table = contingency_table.transpose()
        return contingency_table


    def build_contingency_table_from_topic_list(self, topic_of_interest_list, no_entities=10):
        """
        This function builds a contingency table from a input list of relation models generated with relation_miner.py 
        in regards to predetermined topic list [topic_of_interest_list].
        The first model in [relation_models] is the reference model all other models will be compared with.
        The function extracts the top [no_entities] co-occuring entities for the first [topic_of_interest] from the 
        model and builds a contingency table.
        
        
        input:  relation_models = list
                relation_models_path = str 
                topic_of_interest_list = list           
                no_entities = int (standard 10)
                
        output: contingency_table = pandas DataFrame [rows = different models, columns = entities]
        """
        # identifier for models in relation_models_list
        i = 0
        # print models with idx
        j = 0
        for model in self.relation_models:
            print("model(" + str(j) + "): " + str(model))
            j += 1

        # initialize DistanceMeasure with reference-model
        dm = DistanceMeasure(self.relation_models_path, str(self.relation_models[0]))

        # extract top NO_ENTITIES entities
        top = dm.get_top_co_occurrences(
            topic_of_interest_list[0], cutoff=no_entities, e1_is_synset=0, e2_is_synset=0
        )
        # write first row of contingency_table
        contingency_table = pd.DataFrame(
            np.array([t[1] for t in top]),
            index=[t[0] for t in top],
            columns=[str(topic_of_interest_list[0]) + " (" + str(i) + ")"],
        )

        # loop through the models
        for model in self.relation_models[:]:
            # initialize db_handler()
            db_handler = DBQueryHandlerCoocc(self.relation_models_path, model)

            for topic in topic_of_interest_list:
                # buffer for co-occurrencces
                co_occs = []

                # loop through all all entities and get number of co-occurrences
                for row in contingency_table.index:
                    co_occs.append(
                        len(
                            list(
                                db_handler.select_relations(
                                    e1=topic.lower(),
                                    e2=row.lower(),
                                    e1_is_synset=0,
                                    e2_is_synset=0,
                                )
                            )
                        )
                    )
                contingency_table[str(topic) + " (" + str(i) + ")"] = co_occs

            i += 1

        # transpose the contingency table to get it into the right format
        contingency_table = contingency_table.transpose()

        return contingency_table

