import pandas as pd
import math


def clustering(df, mode):
    """
    This function calculates the clustering coefficient c_omega of all nodes in [df_list]
    
    input: df = DataFrame
    
    output: print(estimated clusters for threshold 0.5,0.75, 0.8 and 0.9*argmax(c_omega))
	"""
    # split into list of dfs containing only one reference node
    df_list = [df.loc[i : i + 8 - 1, :] for i in range(0, len(df), 8)]

    df_coefficient = pd.DataFrame()

    # loop over every single node
    for df_single in df_list:
        df_single = df_single.reset_index()
        total_value = 0

        # loop over the weights of all connected nodes
        for j in range(len(df_single) - 1):
            if mode == "geometric":
                # geometric
                total_value = total_value + math.sqrt(df_single.chi_sq[j] * df_single.chi_sq[j + 1])
            if mode == "arithmetic":                
                # arithmetic
                total_value = total_value + ((df_single.chi_sq[j] * df_single.chi_sq[j + 1]) / 2)
            if mode == "argmax":                
                # max
                total_value = total_value + max(df_single.chi_sq[j], df_single.chi_sq[j + 1])
            if mode == "argmin":
                # min
                total_value = total_value + min(df_single.chi_sq[j], df_single.chi_sq[j + 1])

        for i in range(len(df_single) - 1):
            if mode == "geometric":
                # geometric
                triplet_value = math.sqrt(df_single.chi_sq[i] * df_single.chi_sq[i + 1])
            if mode == "arithmetic":
                # arithmetic
                triplet_value = (df_single.chi_sq[i] * df_single.chi_sq[i + 1]) / 2
            if mode == "argmax":
                # max
                triplet_value = max(df_single.chi_sq[i], df_single.chi_sq[i + 1])
            if mode == "argmin":                    
                # min
                triplet_value = min(df_single.chi_sq[i], df_single.chi_sq[i + 1])

        cluster_coefficient = triplet_value / total_value
        buffer = [
            [
            df_single.reference[i],
            df_single.comparison[i],
            df_single.comparison[i + 1],
            triplet_value,
            cluster_coefficient,
            ]
        ]
        df_coefficient = df_coefficient.append(buffer)

    df_coefficient = df_coefficient.reset_index()

    print("\n\n threshold 0.5*c_omega")
    check_list = []
    # print out triangles that have a cluster coefficient bigger, than X
    for i in range(len(df_coefficient)):
        if df_coefficient[4][i] >= ((0.5) * df_coefficient[4].max()):
            print(list(df_coefficient.loc[i][1:4]))
            check_list.append(list(df_coefficient.loc[i][1:4]))
        else:
            continue

    print("\n\n threshold 0.75*c_omega")
    check_list = []
    for i in range(len(df_coefficient)):
        if df_coefficient[4][i] >= ((0.75) * df_coefficient[4].max()):
            print(list(df_coefficient.loc[i][1:4]))
            check_list.append(list(df_coefficient.loc[i][1:4]))
        else:
            continue

    print("\n\n threshold 0.8*c_omega")
    check_list = []
    for i in range(len(df_coefficient)):
        if df_coefficient[4][i] >= ((0.9) * df_coefficient[4].max()):
            print(list(df_coefficient.loc[i][1:4]))
            check_list.append(list(df_coefficient.loc[i][1:4]))
        else:
            continue


    print("\n\n threshold 0.9*c_omega")
    check_list = []
    for i in range(len(df_coefficient)):
        if df_coefficient[4][i] >= ((0.9) * df_coefficient[4].max()):
            print(list(df_coefficient.loc[i][1:4]))
            check_list.append(list(df_coefficient.loc[i][1:4]))
        else:
            continue

    return
