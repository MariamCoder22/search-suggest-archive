# scripts/validate_data.py

import pandas as pd

def clean_csv(input_path="data/mock_search_logs.csv", output_path="data/cleaned.csv"):
    df = pd.read_csv(input_path)

    df['query'] = df['query'].str.strip().str.lower()
    df = df.drop_duplicates()
    df = df[df['query'].str.len() > 2]  # Filter too-short terms

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_csv()
