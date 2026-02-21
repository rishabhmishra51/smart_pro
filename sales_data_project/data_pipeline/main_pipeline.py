from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_processor import DataProcessor

file_path = "../datasets/sales_data_sample.csv"

loader = DataLoader(file_path)
df = loader.load_data()

cleaner = DataCleaner(df)
cleaner.remove_duplicates()
cleaner.handle_missing()
cleaner.validate_data()
cleaner.standardize_dates()
cleaner.clean_text()

clean_df = cleaner.get_clean_data()

processor = DataProcessor(clean_df)
processor.create_total_amount()
processor.create_profit()

final_df = processor.get_processed_data()

print(final_df.head())