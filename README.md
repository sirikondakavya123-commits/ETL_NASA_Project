NASA APOD ETL Pipeline

This project implements a complete ETL (Extract, Transform, Load) pipeline using Python.
It retrieves NASA’s Astronomy Picture of the Day (APOD) metadata using the NASA API, processes the data, and loads the final output into a Supabase database.
The pipeline is modular and divided into three stages: extraction, transformation, and loading.

Project Overview

The ETL pipeline performs the following tasks:

Extracts APOD metadata and downloads the image from the NASA APOD API.

Transforms the raw JSON metadata into a structured CSV file.

Loads the cleaned data into a Supabase table for storage and analysis.

Project Structure
project/
├── etl/
│   ├── extracted_nasa.py
│   ├── transformed_nasa.py
│   └── load_nasa.py
│
├── data/
│   ├── raw/
│   ├── images/
│   └── staged/
│
├── README.md
├── requirements.txt
└── .env

ETL Pipeline Details
Extract Phase

Script: extracted_nasa.py

This script sends a request to the NASA APOD API, retrieves JSON metadata, and downloads the APOD image.
The JSON file is stored in the data/raw/ directory, and the image is stored in data/images/.

Transform Phase

Script: transformed_nasa.py

This script reads the latest APOD JSON file, extracts relevant fields, and converts them into a structured CSV file.
The final CSV output is stored in the data/staged/ directory.

Load Phase

Script: load_nasa.py

This script reads the transformed CSV and uploads the data to a Supabase table.
It performs data cleaning before insertion and uploads the records in batches.

Setup Instructions
Step 1: Install Required Libraries
pip install -r requirements.txt

Step 2: Configure Environment Variables

Create a .env file with the following fields:

NASA_API_KEY=your_nasa_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_service_role_key

Step 3: Run Each ETL Stage
Extract
python etl/extracted_nasa.py

Transform
python etl/transformed_nasa.py

Load
python etl/load_nasa.py

Recommended Supabase Table Schema
Column	Type
id (optional)	bigint (Primary Key)
title	text
date	date
explanation	text
hdurl	text
url	text
copyright	text
media_type	text
service_version	text
Key Features

Modular ETL design with separation of extract, transform, and load logic

Automatic download and storage of APOD images

Standardized CSV output suitable for analysis

Cloud storage and integration using Supabase

Simple configuration using environment variables
