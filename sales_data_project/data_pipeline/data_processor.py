class DataProcessor:
    def __init__(self, df):
        self.df = df

    def create_total_amount(self):
        self.df['total_amount'] = self.df['quantity'] * self.df['price']

    def create_profit(self):
        self.df['profit'] = self.df['total_amount'] * 0.15

    def get_processed_data(self):
        return self.df