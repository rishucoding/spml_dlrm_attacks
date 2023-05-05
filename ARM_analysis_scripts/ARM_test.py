import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from scipy.sparse import lil_matrix

df = pd.read_csv('../dataset/taobao_dataset_with_orders_400k_2.csv')

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


# Create a dictionary to map brand names to column indices
brand_to_col = {brand: i for i, brand in enumerate(all_brands)}

# Create a sparse matrix to represent the transactions
num_rows = df['order_id'].nunique()
num_cols = len(all_brands)
X = lil_matrix((num_rows, num_cols), dtype=int)

# Iterate over each order and update the sparse matrix
for i, (_, group) in enumerate(df.groupby('order_id')):
    # Get the list of brands in this order
    brands = group['brand'].values
    # Update the sparse matrix
    for brand in brands:
        col = brand_to_col[brand]
        X[i, col] = 1

X_df = pd.DataFrame.sparse.from_spmatrix(X, columns=all_brands)

# Convert integer column names to string column names
X_df.columns = X_df.columns.astype(str)

# Perform frequent itemset mining using the Apriori algorithm

# min_support value needs to be updated based on the system capacity
min_support = 0.01
frequent_itemsets = apriori(X_df, min_support=min_support, use_colnames=True)
print("frequent_itemsets", frequent_itemsets)

# Generate association rules from the frequent itemsets
min_confidence = 0.2
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=.2)

# Print the rules
print(rules)