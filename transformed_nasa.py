import pandas as pd
import json
import glob
import os

def transform_nasa_data():
    os.makedirs("../data/staged", exist_ok=True)

    latest_file = sorted(glob.glob("../data/raw/nasa_apod*.json"))[-1]

    with open(latest_file, "r") as f:
        data = json.load(f)

    df = pd.DataFrame([{
        "copyright": data.get("copyright"),
        "date": data.get("date"),
        "explanation": data.get("explanation"),
        "hdurl": data.get("hdurl"),
        "media_type": data.get("media_type"),
        "service_version": data.get("service_version"),
        "title": data.get("title"),
        "url": data.get("url")
    }])

    output_path = '../data/staged/transformed_nasa_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")
    return df

if __name__ == "__main__":
    transform_nasa_data()
