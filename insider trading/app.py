from flask import Flask, render_template, request
import numpy as np
from sklearn.svm import SVC
import joblib
import pandas as pd

app = Flask(__name__)

# Load CSV data
csv_file = "insider trading\Insider Trading.csv"
data = pd.read_csv(csv_file)

# Load SVM model
svm_model = joblib.load("svm_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    symbol = request.form['symbol']
    company = request.form['company']
    acquirer_disposer = request.form['acquirer_disposer']
    category_of_person = request.form['category_of_person']
    type_of_security_prior = request.form['type_of_security_prior']
    no_of_security_prior = int(request.form['no_of_security_prior'])
    shareholding_prior = float(request.form['shareholding_prior'])
    no_of_securities = int(request.form['no_of_securities'])
    value_of_security = float(request.form['value_of_security'])
    transaction_type = request.form['transaction_type']
    no_of_security_post = int(request.form['no_of_security_post'])

    # Perform analysis
    insider_trading_detected = check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type)

    return render_template('result.html', insider_trading_detected=insider_trading_detected, company=company)

def check_for_unusual_activity(acquirer_disposer, no_of_securities, transaction_type):
    if "insider" in acquirer_disposer.lower() and no_of_securities > 1000 and transaction_type == "Acquisition":
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
