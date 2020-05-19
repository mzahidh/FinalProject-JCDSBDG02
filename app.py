from flask import Flask, render_template, request, send_from_directory
from data import gas_utility,electric_utility, pre_retrofit_heating
from predictions import prediction
from sqlalchemy import create_engine
import mysql.connector
import pandas as pd

## Translate Flask to python object
app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def welcome():
    return render_template('welcome.html')

@app.route('/predict',methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        data['Total Project Cost'] = int(data['Total Project Cost'])
        data['Total Incentives'] = int(data['Total Incentives'])
        data['Size of Home'] = int(data['Size of Home'])
        data['Volume of Home'] = int(data['Volume of Home'])
        data['Number of Units'] = int(data['Number of Units'])
        data['Estimated Annual kWh Savings'] = int(data['Estimated Annual kWh Savings'])
        data['Estimated Annual MMBtu Savings'] = int(data['Estimated Annual MMBtu Savings'])
        data['First Year Energy Savings $ Estimate'] = int(data['First Year Energy Savings $ Estimate'])
        hasil = prediction(data)
        if hasil == 1:
            teks = 'Congratulations, you get Green Jobs-Green NY Free/Reduced Cost Audit!'
        else:
            teks = 'Sorry, you are failed to get Green Jobs-Green NY Free/Reduced Cost Audit, try again next year'
        return render_template("result.html",hasil_prediction=teks)
    return render_template('prediction.html',data_gas=sorted(gas_utility),
    data_electric=sorted(electric_utility),data_heating=sorted(pre_retrofit_heating))

@app.route('/storage/<path:x>')
def storage(x):
    return send_from_directory("storage", x)
    
@app.route('/about', methods = ["POST", "GET"])
def about():
    return render_template('about.html')

@app.route('/dataset', methods = ["POST", "GET"])
def dataset():
    # Connecting to MySQL Database
    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='123456ABCDEF',
        database='dashboard')

    mycursor= mydb.cursor()
    mycursor.execute('Select * FROM dataset')

    myresult = mycursor.fetchall()
    db_dashboard = pd.DataFrame(myresult,columns= mycursor.column_names)
    db_dashboard = db_dashboard.sample(10)

    # engine = create_engine("mysql+mysqlconnector://root:123456ABCDEF@localhost/dashboard?host=localhost?port=3306")
    # conn = engine.connect()
    # result = conn.execute('select * from dashboard.dataset').fetchall()
    
    return render_template('dataset.html',column_names=db_dashboard.columns.values,
    row_data=list(db_dashboard.values.tolist()),zip=zip)


if __name__ == '__main__':
    app.run(debug=True,port=3000)