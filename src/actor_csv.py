import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/prices.csv")

class CSVTool:
    def __init__(self, csv_path=CSV_PATH):
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_path)

    def query_price(self, query: str):
        query = query.lower()
        # If asking for max
        if "max" in query or "maximum" in query:
            col = "price"  # adjust based on your CSV column
            max_row = self.df.loc[self.df[col].idxmax()]
            return f"Maximum {col} is {max_row[col]} for {max_row['item']}"
        # If asking for specific item
        for item in self.df["item"].tolist():
            if item.lower() in query:
                price = self.df.loc[self.df['item'].str.lower() == item.lower(), 'price'].values[0]
                return f"The price of {item} is {price}"
        return "Item not found."
