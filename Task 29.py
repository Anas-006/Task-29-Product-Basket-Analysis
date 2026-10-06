import pandas as pd
from collections import Counter
from itertools import combinations
df=pd.read_excel(r"c:\Users\Admin\Desktop\online_retail_II.xlsx")

print(df.head())
print(df.shape)
print(df.columns)

print(df.isnull().sum())
df=df.dropna(subset=["Description"])
df=df[~df["Invoice"].astype(str).str.startswith("C")]
df=df[df["Quantity"]>0]
print("Cleaned Shape",df.shape)
print(df.head())

basket_data=df[["Invoice","Description"]].copy()
basket_data=basket_data.drop_duplicates()
print("\n Basket Data:")
print(basket_data.head())

orders = {}

for invoice, product in zip(
    basket_data["Invoice"],
    basket_data["Description"]
):
    if invoice not in orders:
        orders[invoice] = []

    orders[invoice].append(product)

pair_counter = Counter()

for products in orders.values():
    unique_products = sorted(set(products))

    for pair in combinations(unique_products, 2):
        pair_counter[pair] += 1

print("Number of Orders:", len(orders))
print("Total Product Pairs:", len(pair_counter))

pairs_df = pd.DataFrame(
    pair_counter.items(),
    columns=["Product Pair", "Orders Together"]
)

pairs_df["Product 1"] = pairs_df["Product Pair"].apply(lambda x: x[0])
pairs_df["Product 2"] = pairs_df["Product Pair"].apply(lambda x: x[1])

pairs_df = pairs_df.drop(columns=["Product Pair"])

pairs_df = pairs_df[
    ["Product 1", "Product 2", "Orders Together"]
]

pairs_df = pairs_df.sort_values(
    by="Orders Together",
    ascending=False
).reset_index(drop=True)

print("\nTop 20 Product Pairs:")
print(pairs_df.head(20))

top_pairs = pairs_df.head(20)

top_pairs.to_csv(
    "top_product_pairs.csv",
    index=False
)

print("\nTop product pairs saved as top_product_pairs.csv")

recommendations = []

for _, row in top_pairs.iterrows():

    recommendations.append({
        "Product": row["Product 1"],
        "Recommended Product": row["Product 2"],
        "Orders Together": row["Orders Together"]
    })

    recommendations.append({
        "Product": row["Product 2"],
        "Recommended Product": row["Product 1"],
        "Orders Together": row["Orders Together"]
    })

recommendations_df = pd.DataFrame(recommendations)

print("\nRecommendations:")
print(recommendations_df.head(20))

recommendations_df.to_csv(
    "product_recommendations.csv",
    index=False
)

print("\nRecommendations saved as product_recommendations.csv")

print("\n========== TOP 10 PRODUCT PAIRS ==========")

print(
    pairs_df.head(10).to_string(index=False)
)

print("\n========== SUMMARY ==========")

print("Original Rows:", df.shape[0])
print("Unique Orders:", df["Invoice"].nunique())
print("Unique Products:", df["Description"].nunique())
print("Total Product Pairs:", len(pairs_df))

df.to_csv(
    "cleaned_online_retail.csv",
    index=False
)

print("\nCleaned data saved as cleaned_online_retail.csv")

print("\n======================================")
print("TASK 29 PRODUCT BASKET ANALYSIS DONE")
print("======================================")