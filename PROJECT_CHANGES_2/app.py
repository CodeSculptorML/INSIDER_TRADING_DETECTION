from flask import Flask, render_template
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io 
import base64

app = Flask(__name__)

# Function to encode image file as base64
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

def generate_bars(company):
        df = pd.read_csv('new_dataset.csv')
        grouped = df.groupby('SYMBOL \n')
        company_names_list = ['MHRIL','SBFC','LALPATHLAB','EMAMILTD','VASCONEQ','BSOFT','LT','M&M']
        for company in company_names_list:
            if company in grouped.groups:
                # Get data for the current company
                data = grouped.get_group(company)

                # Filter the DataFrame for buy and sell transactions for the current company
                buy_transactions = data[data['ACQUISITION/DISPOSAL TRANSACTION TYPE \n'] == 'Buy']
                sell_transactions = data[data['ACQUISITION/DISPOSAL TRANSACTION TYPE \n'] == 'Sell']

                # Group transactions by date and count the occurrences
                buy_counts = buy_transactions.groupby('DATE OF ALLOTMENT/ACQUISITION FROM \n').size()
                sell_counts = sell_transactions.groupby('DATE OF ALLOTMENT/ACQUISITION FROM \n').size()

                # Combine buy and sell counts into a single DataFrame
                transaction_counts = pd.DataFrame({'Buy': buy_counts, 'Sell': sell_counts}).fillna(0)

                # Plot the bar chart for the current company
                fig, ax = plt.subplots()
                transaction_counts.plot(kind='bar', stacked=True, ax=ax)
                ax.set_xlabel('Date')
                ax.set_ylabel('Transaction Count')
                ax.set_title(f'Buy and Sell Transactions Over Time for {company}')
                ax.legend(title='Transaction Type')
                ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability
                plt.tight_layout()  # Adjust layout to prevent clipping of labels
                #plt.show()
                plt.savefig(f"static/{company}_bar.png")  # Adjust the path as needed
                plt.close()
            else:
                print(f"No data available for {company}")

        

def generate_company_graph(company):
        # Load data and filter for the specific company
        df = pd.read_csv('new_dataset.csv')  # Replace 'your_data.csv' with your actual dataset file
        company_data = df[df['SYMBOL \n'] == company]

        # Plot buy-sell graph
        plt.figure(figsize=(10, 6))
        plt.plot(company_data['DATE OF ALLOTMENT/ACQUISITION FROM \n'], company_data['ACQUISITION/DISPOSAL TRANSACTION TYPE \n'], marker='o')
        plt.title(f"Buy-Sell Graph for {company}")
        plt.xlabel('Date')
        plt.ylabel('Transaction Type')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Save the graph
        plt.savefig(f"static/{company}_graph.png")  # Adjust the path as needed
        plt.close()

@app.route('/')
def index():
    # Load data and perform necessary operations
    # Assuming you have already processed the data and generated the graphs and accuracy
    # Replace these with your actual data and logic
    suspected_companies_display_forgraph=['M&M','MHRIL']
    suspected_companies_display_forbar=['MHRIL','SBFC','LALPATHLAB','EMAMILTD','VASCONEQ','BSOFT','LT','M&M']
    suspected_companies = ["MHRIL","SBFC","LALPATHLAB","KOTAKBANK","KPITTECH","CIPLA","STARCEMENT","EMAMILTD","DMART","VASCONEQ","WIPRO","JSWSTEEL","BSOFT","NAM-INDIA","RELIGARE","AUBANK","LTTS","DIVISLAB","LT","VIPIND","BIOCON","THOMASCOOK","M&M","MPHASIS","GOODLUCK","BAJAJ-AUTO","COFORGE","MTARTECH","KIRLPNU","JBCHEPHARM","ICICIGI","EMKAY"]
    #accuracy1 = 82  # Example accuracy
    #company_names_list = ['CHOICEIN', 'THOMASCOOK', 'ACCENTMIC', 'M&M', 'MPHASIS', 'COFORGE', 'JAYNECOIND']
    # Generate and save pie chart
    
    # accuracy2=98
    # labels = ['Correct', 'Incorrect']
    # sizes = [accuracy2, 100 - accuracy2]
    # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    # plt.title('Model Accuracy')
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # chart_data2 = base64.b64encode(buffer.getvalue()).decode()

    # # Embed the chart into HTML
    # chart_html2 = f'<img src="data:image/png;base64,{chart_data2}" alt="Pie Chart">'
    # accuracy3=83
    # labels = ['Correct', 'Incorrect']
    # sizes = [accuracy3, 100 - accuracy3]
    # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    # plt.title('Model Accuracy')
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # chart_data3 = base64.b64encode(buffer.getvalue()).decode()

    # # Embed the chart into HTML
    # chart_html3 = f'<img src="data:image/png;base64,{chart_data3}" alt="Pie Chart">'

    chart_html_list = {}
    model_name=['LSTM RNN','SVM','SVM Logistic']
    accuracy=[83,82,98]
    labels = ['Correct', 'Incorrect']
    for d in range(3):
        # Generate the pie chart
        
        sizes = [accuracy[d], 100 - accuracy[d]]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Model Accuracy')
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        chart_data1 = base64.b64encode(buffer.getvalue()).decode()

    # Embed the chart into HTML
        chart_html1 = f'<img src="data:image/png;base64,{chart_data1}" alt="Pie Chart">'
        
        # Embed the chart into HTML
        md=model_name[d]
        chart_html_list[md]=chart_html1

        # Clear the current figure to prepare for the next chart
        plt.close()
    

    # Generate and save graphs for suspected companies
    for company in suspected_companies_display_forgraph:
        generate_company_graph(company)

    # Dictionary to store image data for each suspected company
    graphs = {}

    # Load and encode images for suspected companies
    for company in suspected_companies_display_forgraph:
        #image_path = f"insider trading\static\{company}_graph.png"  # Adjust the path to your saved graphs
        #insider trading\static\M&M_graph.png
        image_path = f"static/{company}_graph.png"

        encoded_image = encode_image(image_path)
        graphs[company] = encoded_image

    for company in suspected_companies_display_forbar:
        generate_bars(company)

    # Dictionary to store image data for each suspected company
    bars = {}

    
    for company in suspected_companies_display_forbar:
        #image_path = f"insider trading\static\{company}_graph.png"  # Adjust the path to your saved graphs
        #insider trading\static\M&M_graph.png
        image_path = f"static/{company}_bar.png"

        encoded_image = encode_image(image_path)
        bars[company] = encoded_image

    # chart_html3 = f'<img src="data:image/png;base64,{chart_data3}" alt="Pie Chart">'
    return render_template('index.html', suspected_companies=suspected_companies, graphs=graphs,bars=bars,data_rows=data_rows,chart_html_list=chart_html_list)
    #chart_html1=chart_html1,chart_html2=chart_html2,chart_html3=chart_html3)
suspected_companies = ["MHRIL","SBFC","LALPATHLAB","KOTAKBANK","KPITTECH","CIPLA","STARCEMENT","EMAMILTD","DMART","VASCONEQ","WIPRO","JSWSTEEL","BSOFT","NAM-INDIA","RELIGARE","AUBANK","LTTS","DIVISLAB","LT","VIPIND","BIOCON","THOMASCOOK","M&M","MPHASIS","GOODLUCK","BAJAJ-AUTO","COFORGE","MTARTECH","KIRLPNU","JBCHEPHARM","ICICIGI","EMKAY"]
def chunks(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]
data_rows=list(chunks(suspected_companies,6))

if __name__ == '__main__':
    app.run(debug=True)
