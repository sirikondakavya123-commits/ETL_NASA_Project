import os
import time
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

# Initialize Supabase client
load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def load_nasa():
    # Path of transformed NASA data
    csv_path = "../data/staged/transformed_nasa_data.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing file: {csv_path}")

    df = pd.read_csv(csv_path)

    # Convert date to proper format (just YYYY-MM-DD)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Supabase cannot accept NaN → convert to None
    df = df.where(pd.notnull(df), None)

    batch_size = 20
    total = len(df)

    for i in range(0, total, batch_size):
        batch = df.iloc[i:i + batch_size].to_dict("records")

        # Insert into Supabase
        supabase.table("nasa_apod").insert(batch).execute()
        
        print(f"Inserted rows {i+1} → {min(i+batch_size, total)}")
        time.sleep(0.3)

    print("Finished loading NASA APOD dataset.")

if __name__ == "__main__":
    load_nasa()
