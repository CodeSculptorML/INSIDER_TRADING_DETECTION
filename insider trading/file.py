# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:06:52 2024

@author: COMPUTER
"""

import tkinter as tk
from tkinter import filedialog
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class InsiderTradingGraphAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph-Based Insider Trading Analyzer")
        
        self.label = tk.Label(root, text="Select CSV file for analysis:")
        self.label.pack()
        
        self.analyze_button = tk.Button(root, text="Select File", command=self.select_file)
        self.analyze_button.pack()
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()
        
    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith('.csv'):
            self.analyze(file_path)
        else:
            self.status_label.config(text="Please select a CSV file.")
            
    def analyze(self, file_path):
        try:
            df = pd.read_csv(file_path)
            G = nx.from_pandas_edgelist(df, source='Trader', target='Company')
            self.plot_graph(G)
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            
    def plot_graph(self, G):
        plt.figure(figsize=(10, 6))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', linewidths=1, font_size=10)
        plt.title("Insider Trading Connections")
        plt.axis('off')
        plt.show()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = InsiderTradingGraphAnalyzer(root)
    root.mainloop()
