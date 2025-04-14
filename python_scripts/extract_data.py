import requests
import pandas as pd

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
OUTPUT_CSV = "../data/online_retail.csv"

def download_data(url, output_path):
    print(f"Downloading data from {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for bad status codes

    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Data downloaded successfully to {output_path}")

def excel_to_csv(excel_path, csv_path):
    print(f"Converting Excel to CSV...")
    df = pd.read_excel(excel_path)
    df.to_csv(csv_path, index=False)
    print(f"CSV file created at {csv_path}")

if __name__ == "__main__":
    excel_file = "../data/online_retail.xlsx"
    download_data(DATA_URL, excel_file)
    excel_to_csv(excel_file, OUTPUT_CSV)
    print("Data extraction complete.")