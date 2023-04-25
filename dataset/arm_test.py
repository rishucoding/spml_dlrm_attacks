## For a particular dataset, run ARM to identify the frequently occuring brand combinations (one or two or more... )
## Play with the parameters: min_support, confidence


import numpy as np
from scipy.sparse import lil_matrix
import pandas as pd
from os import listdir
from os.path import isfile, join

mypath = '/i3c/hpcl/rzj5233/courses/597-spml/spml_dlrm_attacks/dataset'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
newfiles = ['taobao_dataset_with_orders_male.csv', 'taobao_dataset_with_orders_female.csv',
            'taobao_dataset_with_orders_age_level_0.csv',
            'taobao_dataset_with_orders_age_level_1.csv',
            'taobao_dataset_with_orders_age_level_2.csv',
            'taobao_dataset_with_orders_age_level_3.csv',
            'taobao_dataset_with_orders_age_level_4.csv',
            'taobao_dataset_with_orders_age_level_5.csv',
            'taobao_dataset_with_orders_age_level_6.csv',
            ]
"""

for x in onlyfiles:
    print(x[:6])
    if x[:6] == 'taobao':
        newfiles.append(x)
"""

for zz in newfiles:
    print(f'Begin {zz}')
    df = pd.read_csv(zz)
    df = df.loc[df.duplicated(subset='order_id', keep=False)]
    order_dict = {}
    for row in df.itertuples():
        order_id = row.order_id
        brand = row.brand
        if order_id in order_dict:
            order_dict[order_id].append(brand)
        else:
            order_dict[order_id] = [brand]

# Create a list of all unique brands
    all_brands = sorted(list(set(df['brand'])))

    from scipy.sparse import lil_matrix
    from mlxtend.frequent_patterns import apriori, association_rules

# Create a dictionary to map brand names to column indices
    brand_to_col = {brand: i for i, brand in enumerate(all_brands)}

# Create a sparse matrix to represent the transactions
    num_rows = df['order_id'].nunique()
    num_cols = len(all_brands)
    X = lil_matrix((num_rows, num_cols), dtype=int)

# Iterate over each order and update the sparse matrix
    for i, (_, group) in enumerate(df.groupby('order_id')):
        brands = group['brand'].values
        for brand in brands:
            col = brand_to_col[brand]
            X[i, col] = 1

    X_df = pd.DataFrame.sparse.from_spmatrix(X, columns=all_brands)

# Convert integer column names to string column names
    X_df.columns = X_df.columns.astype(str)

# df = pd.DataFrame(data=csr_matrix.todense(sparse_matrix))
# X_df.to_csv('X_df.csv', index=False)

# Perform frequent itemset mining using the Apriori algorithm

    min_support = 0.0003
    print(X_df.shape)
    frequent_itemsets = apriori(X_df, min_support=min_support, use_colnames=True)
    print("frequent_itemsets", frequent_itemsets)
    print(">>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>> SUPPORT is " + str(min_support))
    for x in frequent_itemsets['itemsets']:
        print(x)

    print(">>>>>>>>>>>>>>>>>>")
# Generate association rules from the frequent itemsets
    min_confidence = 0.2
# rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_confidence)
    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=.2)

# Print the rules
    print(rules)

    print(f'End {zz}')
