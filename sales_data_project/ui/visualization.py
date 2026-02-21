import matplotlib.pyplot as plt
import seaborn as sns

def sales_by_city(df):
    grouped = df.groupby("city")["total_amount"].sum().reset_index()

    plt.figure(figsize=(8,5))
    sns.barplot(data=grouped, x="city", y="total_amount")
    plt.xticks(rotation=45)
    plt.title("Sales by City")
    plt.show()