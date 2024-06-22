import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def submit():
    symbol = symbol_entry.get()
    company = company_entry.get()
    acquirer_disposer = acquirer_disposer_entry.get()
    category_of_person = category_of_person_entry.get()
    type_of_security_prior = type_of_security_prior_entry.get()
    no_of_security_prior = int(no_of_security_prior_entry.get())
    shareholding_prior = float(shareholding_prior_entry.get())
    no_of_securities = int(no_of_securities_entry.get())
    value_of_security = float(value_of_security_entry.get())
    transaction_type = transaction_type_entry.get()
    no_of_security_post = int(no_of_security_post_entry.get())

    # Data for analysis
    data_dict = {
        'No. of Security (Prior)': no_of_security_prior,
        'Shareholding (Prior)': shareholding_prior,
        'No. of Securities (Acquired/Disposed)': no_of_securities,
        'Value of Security (Acquired/Disposed)': value_of_security,
        'No. of Security (Post)': no_of_security_post
    }

    # Display graphical analysis
    display_bar_chart(data_dict)

    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, "Data Submitted:\n")
    output_text.insert(tk.END, f"Symbol: {symbol}\n")
    output_text.insert(tk.END, f"Company: {company}\n")
    output_text.insert(tk.END, f"Acquirer/Disposer: {acquirer_disposer}\n")
    output_text.insert(tk.END, f"Category of Person: {category_of_person}\n")
    output_text.insert(tk.END, f"Type of Security (Prior): {type_of_security_prior}\n")
    output_text.insert(tk.END, f"No. of Security (Prior): {no_of_security_prior}\n")
    output_text.insert(tk.END, f"Shareholding (Prior): {shareholding_prior}\n")
    output_text.insert(tk.END, f"No. of Securities (Acquired/Disposed): {no_of_securities}\n")
    output_text.insert(tk.END, f"Value of Security (Acquired/Disposed): {value_of_security}\n")
    output_text.insert(tk.END, f"Acquisition/Disposal Transaction Type: {transaction_type}\n")
    output_text.insert(tk.END, f"No. of Security (Post): {no_of_security_post}\n")
    
    if check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type):
        output_text.insert(tk.END, "Potential insider trading detected!\n")
    else:
        output_text.insert(tk.END, "No indications of insider trading.\n")

def check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type):
    if "insider" in acquirer_disposer.lower() and no_of_securities > 1000 and transaction_type == "Acquisition":
        return True
    else:
        return False

def display_bar_chart(data_dict):
    df = pd.DataFrame(data_dict, index=[0])
    ax = df.plot(kind='bar', legend=False)
    ax.set_xlabel('Inputs')
    ax.set_ylabel('Values')
    ax.set_title('Input Data Analysis')
    plt.xticks(rotation=45)
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(ax.figure, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
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

output_text = tk.Text(mainframe, height=10, width=50)
output_text.grid(column=0, row=12, columnspan=2, sticky=tk.W)

graph_frame = ttk.Frame(mainframe)
graph_frame.grid(column=0, row=13, columnspan=2, sticky=tk.W)

ttk.Button(mainframe, text="Submit", command=submit).grid(column=1, row=11, pady=10)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
