# scripts/load_data.py

import csv

# This script mocks loading archived query data from Wayback or any source

MOCK_DATA = [
    "climate change",
    "covid 19",
    "machine learning",
    "elon musk",
    "black holes",
    "global warming",
    "quantum computing",
    "solar eclipse",
    "moon landing",
    "cryptocurrency"
]

# Save mock data into a CSV
def save_mock_data(filename="data/mock_search_logs.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["query"])  # header
        for item in MOCK_DATA:
            writer.writerow([item])
    print(f"Mock data saved to {filename}")

if __name__ == "__main__":
    save_mock_data()

