import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def handle_missing(self):
        self.df = self.df.fillna(method="ffill")

    def validate_data(self):
        if 'quantity' in self.df.columns:
            self.df = self.df[self.df['quantity'] > 0]

        if 'price' in self.df.columns:
            self.df = self.df[self.df['price'] > 0]

    def standardize_dates(self):
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')

    def clean_text(self):
        if 'city' in self.df.columns:
            self.df['city'] = self.df['city'].str.lower().str.strip()

    def get_clean_data(self):
        return self.df