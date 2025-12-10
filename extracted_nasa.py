import json
from pathlib import Path
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Define directories
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
IMG_DIR = BASE_DIR / "data" / "images"

RAW_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

def extract_nasa_data():
    url = "https://api.nasa.gov/planetary/apod"
    
    params = {
        "api_key": NASA_API_KEY,
        "hd": True
    }
    
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    # ---- Save JSON metadata ----
    json_filename = RAW_DIR / f"nasa_apod_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    json_filename.write_text(json.dumps(data, indent=2))
    print(f"Metadata saved to {json_filename}")

    # ---- Download the image ----
    image_url = data.get("hdurl") or data.get("url")

    if image_url:
        image_ext = image_url.split(".")[-1]
        image_filename = IMG_DIR / f"nasa_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{image_ext}"

        img_response = requests.get(image_url)
        img_response.raise_for_status()

        with open(image_filename, "wb") as f:
            f.write(img_response.content)

        print(f"Image saved to {image_filename}")
    else:
        print("No image found in the API response.")


    return data


if __name__ == "__main__":
    extract_nasa_data()
