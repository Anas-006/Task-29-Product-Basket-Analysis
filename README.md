# Task 29 - Product Basket Analysis

## Project Overview

This project performs Product Basket Analysis using transaction-level retail data.

The objective is to identify products that are frequently purchased together within the same order and generate useful product recommendations.

## Objective

The main objective is to analyze customer purchase combinations and identify frequently co-purchased products.

## Dataset

Dataset used:

Online Retail II

The dataset contains retail transaction information including invoice details, product descriptions, quantities, and other transaction attributes.

## Tools Used

- Python
- Pandas
- itertools
- collections
- CSV

## Data Cleaning

The following cleaning steps were performed:

- Removed records with missing product descriptions.
- Removed cancelled transactions.
- Removed transactions with non-positive quantities.
- Removed duplicate product entries within the same invoice.
- Standardized product descriptions by removing unnecessary spaces.

## Methodology

1. Loaded the Online Retail II dataset.
2. Cleaned the transaction data.
3. Grouped products based on Invoice ID.
4. Created unique product combinations within each order.
5. Counted how frequently each product pair occurred.
6. Sorted product pairs based on purchase frequency.
7. Generated product recommendations from frequently purchased combinations.

## Key Analysis

The analysis focuses on:

- Product combinations
- Order frequency
- Frequently purchased product pairs
- Product recommendations
- Cross-selling opportunities

## Output Files

The project generates the following output files:

- cleaned_online_retail.csv
- top_product_pairs.csv
- product_recommendations.csv

## Business Insights

Frequently purchased product combinations provide useful information about customer purchasing behavior.

These combinations can be used for:

- Cross-selling
- Product recommendations
- Bundle offers
- Promotional campaigns
- Product placement decisions

## Recommendations

Businesses can use frequently co-purchased products to create targeted recommendations and bundle offers.

Product recommendations can also be displayed during shopping and checkout to encourage additional purchases.

## Conclusion

Product Basket Analysis helps identify relationships between products based on customer transactions.

The analysis demonstrates how transaction data can be converted into actionable insights for cross-selling, product recommendations, and promotional strategies.
