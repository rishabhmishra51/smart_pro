import tkinter as tk
from tkinter import filedialog
import pandas as pd
from visualization import sales_by_city

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Data Analytics System")

        tk.Button(root, text="Upload CSV", command=self.upload).pack(pady=10)
        tk.Button(root, text="Show Sales by City", command=self.show_chart).pack(pady=10)

    def upload(self):
        self.file_path = filedialog.askopenfilename()
        self.df = pd.read_csv(self.file_path)

    def show_chart(self):
        sales_by_city(self.df)

root = tk.Tk()
app = Dashboard(root)
root.mainloop()