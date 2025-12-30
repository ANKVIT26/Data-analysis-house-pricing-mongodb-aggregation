# Data-analysis-house-pricing-mongodb-aggregation
Data analysis project that explores house pricing data using MongoDB’s aggregation pipeline and Python (PyMongo). Implements stages like `$match`, `$group`, and `$sort` to derive insights such as combined bedroom–floor metrics and exports the final results as newline‑delimited JSON for further analysis or visualization.

# Data Analysis on House Pricing Data using MongoDB Aggregation Pipelines

This project demonstrates how to perform **data analysis on house pricing data** using MongoDB’s aggregation pipeline with Python (PyMongo). It covers connecting to MongoDB Atlas, inserting sample house pricing documents, running aggregation stages like `$match`, `$group`, and `$sort`, and exporting the final results to a JSON file for further analysis or visualization.

## Features

- Connect to MongoDB Atlas using PyMongo.
- Create a `House` database and `HousePricingDB` collection with sample data.
- Use aggregation stages:
  - `$match` to filter houses by location (e.g., `Patna`). [web:134]
  - `$group` to compute derived metrics such as `floorrooms = bedrooms + floor`. 
  - `$sort` to order results by computed fields. 
- Export aggregation results to `data.json` with one JSON document per line for easy downstream processing. 

## Tech Stack

- Python (PyMongo)
- MongoDB Atlas (NoSQL document database)
- MongoDB Aggregation Framework (`$match`, `$group`, `$sort`) 

## Getting Started

1. **Clone the repository**
https://github.com/ANKVIT26/Data-analysis-house-pricing-mongodb-aggregation


