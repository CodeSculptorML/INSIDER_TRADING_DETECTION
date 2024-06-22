# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:14:55 2024

@author: COMPUTER
"""

import tkinter as tk
from tkinter import ttk

from sklearn.svm import SVC
import joblib

# Function to train SVM model and save it to a file
def train_and_save_model(data, labels, filename):
    svm_model = SVC(kernel='linear')
    svm_model.fit(data, labels)
    joblib.dump(svm_model, filename)
    print("SVM model trained and saved successfully.")

# Function to load SVM model from a file
def load_model(filename):
    loaded_model = joblib.load(filename)
    return loaded_model

# Global variable to store the SVM model
svm_model = None
svm_model = load_model("svm_model.pkl")

def submit():
    symbol = symbol_entry.get()
    company = company_entry.get()
    acquirer_disposer = acquirer_disposer_entry.get()
    category_of_person = category_of_person_entry.get()
    type_of_security_prior = type_of_security_prior_entry.get()
    no_of_security_prior = no_of_security_prior_entry.get()
    shareholding_prior = shareholding_prior_entry.get()
    no_of_securities = no_of_securities_entry.get()
    value_of_security = value_of_security_entry.get()
    transaction_type = transaction_type_entry.get()
    no_of_security_post = no_of_security_post_entry.get()

    # Here you can perform further processing with the collected data
    print("Data Submitted:")
    print("Symbol:", symbol)
    print("Company:", company)
    print("Acquirer/Disposer:", acquirer_disposer)
    print("Category of Person:", category_of_person)
    print("Type of Security (Prior):", type_of_security_prior)
    print("No. of Security (Prior):", no_of_security_prior)
    print("% Shareholding (Prior):", shareholding_prior)
    print("No. of Securities (Acquired/Disposed):", no_of_securities)
    print("Value of Security (Acquired/Disposed):", value_of_security)
    print("Acquisition/Disposal Transaction Type:", transaction_type)
    print("No. of Security (Post):", no_of_security_post)
    
    if check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type):
        print("Potential insider trading detected!")
    else:
        print("No indications of insider trading.")

def check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type):
    # Example: Check if the acquirer/disposer is an insider and if the transaction involves a significant number of securities
    # You can define your own criteria based on regulations and common practices
    if "insider" in acquirer_disposer.lower() and int(no_of_securities) > 1000 and transaction_type == "Acquisition":
        return True
    else:
        return False

root = tk.Tk()
root.title("Insider Trading Information")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Symbol").grid(column=0, row=0, sticky=tk.W)
symbol_entry = ttk.Entry(mainframe, width=30)
symbol_entry.grid(column=1, row=0)

ttk.Label(mainframe, text="Company").grid(column=0, row=1, sticky=tk.W)
company_entry = ttk.Entry(mainframe, width=30)
company_entry.grid(column=1, row=1)

ttk.Label(mainframe, text="Name of the Acquirer/Disposer").grid(column=0, row=2, sticky=tk.W)
acquirer_disposer_entry = ttk.Entry(mainframe, width=30)
acquirer_disposer_entry.grid(column=1, row=2)

ttk.Label(mainframe, text="Category of Person").grid(column=0, row=3, sticky=tk.W)
category_of_person_entry = ttk.Entry(mainframe, width=30)
category_of_person_entry.grid(column=1, row=3)

ttk.Label(mainframe, text="Type of Security (Prior)").grid(column=0, row=4, sticky=tk.W)
type_of_security_prior_entry = ttk.Entry(mainframe, width=30)
type_of_security_prior_entry.grid(column=1, row=4)

ttk.Label(mainframe, text="No. of Security (Prior)").grid(column=0, row=5, sticky=tk.W)
no_of_security_prior_entry = ttk.Entry(mainframe, width=30)
no_of_security_prior_entry.grid(column=1, row=5)

ttk.Label(mainframe, text="% Shareholding (Prior)").grid(column=0, row=6, sticky=tk.W)
shareholding_prior_entry = ttk.Entry(mainframe, width=30)
shareholding_prior_entry.grid(column=1, row=6)

ttk.Label(mainframe, text="No. of Securities (Acquired/Disposed)").grid(column=0, row=7, sticky=tk.W)
no_of_securities_entry = ttk.Entry(mainframe, width=30)
no_of_securities_entry.grid(column=1, row=7)

ttk.Label(mainframe, text="Value of Security (Acquired/Disposed)").grid(column=0, row=8, sticky=tk.W)
value_of_security_entry = ttk.Entry(mainframe, width=30)
value_of_security_entry.grid(column=1, row=8)

ttk.Label(mainframe, text="Acquisition/Disposal Transaction Type").grid(column=0, row=9, sticky=tk.W)
transaction_type_entry = ttk.Entry(mainframe, width=30)
transaction_type_entry.grid(column=1, row=9)

ttk.Label(mainframe, text="No. of Security (Post)").grid(column=0, row=10, sticky=tk.W)
no_of_security_post_entry = ttk.Entry(mainframe, width=30)
no_of_security_post_entry.grid(column=1, row=10)

ttk.Button(mainframe, text="Submit", command=submit).grid(column=1, row=11, pady=10)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
