import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import requests
import os

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
OUTPUT_CSV = "../data/online_retail.csv"
SIMULATED_CSV = "../data/simulated_retail.csv"  # Separate file for simulated data

def download_data(url, output_path):
    """Downloads the dataset from the given URL."""
    print(f"Downloading data from {url}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Data downloaded successfully to {output_path}")
        return True  # Indicate success
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        return False # Indicate failure

def excel_to_csv(excel_path, csv_path):
    """Converts the Excel file to a CSV file."""
    print(f"Converting Excel to CSV...")
    try:
        df = pd.read_excel(excel_path)
        df.to_csv(csv_path, index=False)
        print(f"CSV file created at {csv_path}")
        return True
    except Exception as e:
        print(f"Error converting Excel to CSV: {e}")
        return False

def generate_simulated_data(num_records):
    """Generates simulated e-commerce data."""
    print(f"Generating {num_records} simulated data records...")
    try:
        # Define lists of possible values for each column
        num_records = int(num_records) # make sure num_records is an integer
        order_ids = [f"ORD-{i}" for i in range(1, num_records + 1)]
        product_codes = [f"P{i:04d}" for i in range(1, 201)]  # Up to 200 products
        product_names = [f"Product {i}" for i in range(1, 201)]
        customer_ids = [1000 + i for i in range(1, 51)]  # Up to 50 customers
        countries = ["USA", "UK", "Canada", "Germany", "France", "Australia", "Japan", "Brazil", "India", "China"]

        # Create an empty list to hold the data
        data = []

        # Generate data for each record
        for order_id in order_ids:
            product_code = random.choice(product_codes)
            product_name = product_names[int(product_code[1:])-1] # get product name based on product code
            quantity = random.randint(1, 100)
            # Generate a random timestamp within a reasonable range (e.g., last 3 years)
            start_date = datetime(2021, 1, 1)
            end_date = datetime(2024, 1, 1)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            order_timestamp = start_date + timedelta(days=random_number_of_days)

            unit_price = round(random.uniform(1, 100), 2)  # Price between 1 and 100
            customer_id = random.choice(customer_ids)
            country = random.choice(countries)

            data.append([order_id, product_code, product_name, quantity, order_timestamp, unit_price, customer_id, country])

        # Create a Pandas DataFrame from the data
        df = pd.DataFrame(data, columns=["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"])

        # Save the DataFrame to a CSV file
        df.to_csv(SIMULATED_CSV, index=False)
        print(f"Simulated data saved to {SIMULATED_CSV}")
        return True
    except Exception as e:
        print(f"Error generating simulated data: {e}")
        return False

if __name__ == "__main__":
    data_option = input("Do you want to use (1) public data or (2) simulated data? Enter 1 or 2: ")

    if data_option == "1":
        # Download and convert the public data
        if download_data(DATA_URL, "../data/online_retail.xlsx"):
            excel_to_csv("../data/online_retail.xlsx", OUTPUT_CSV)
        else:
            print("Failed to get public data. Exiting.")
            exit()
    elif data_option == "2":
        # Generate simulated data
        num_records = input("Enter the number of records to generate: ")
        if not num_records.isdigit():
            print("Invalid number of records. Exiting")
            exit()
        generate_simulated_data(int(num_records))
    else:
        print("Invalid input. Please enter 1 or 2. Exiting.")
        exit()

    print("Data extraction/generation complete.")
