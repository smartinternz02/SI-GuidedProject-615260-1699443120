import pickle
import joblib
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='/Users/akshatgattani/Desktop/Shipping prediction/templates', static_folder='/Users/akshatgattani/Desktop/Shipping prediction/templates')
model = pickle.load(open("/Users/akshatgattani/Desktop/Shipping prediction/model/rf_acc_68.pkl", "rb"))
Data_normalizer = joblib.load("/Users/akshatgattani/Desktop/Shipping prediction/model/scl_model.pkl")

@app.route("/")
def Home():
    return render_template("app.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/contact")
def Contact():
    return render_template("contact.html")

@app.route("/predict", methods=['GET', 'POST'])
def Predict():
    if request.method == 'GET' :
        return render_template("predict.html")

    if request.method == 'POST' :

        Warehouse_block=request.form["warehouse_block"]
        Mode_of_Shipment=request.form["mode_of_shipment"]
        Customer_care_calls= request.form["customer_care_calls"]
        Customer_rating= request.form["customer_rating"]
        cost_of_the_Product = request.form["cost_of_the_product"]
        Prior_purchases = request.form["prior_purchases"]
        Product_importance = request.form["product_importance"]
        Gender = request.form["gender"]
        Discount_offered =  request.form["discount_offered"]
        Weight_in_gms = request.form["weight_in_gms"]

        x = np.zeros(10)

        if(Warehouse_block == 'D'):
            x[0]= 0
        elif(Warehouse_block == 'F'):
            x[0] = 1
        elif(Warehouse_block == 'A'):
            x[0] = 2
        elif(Warehouse_block == 'B'):
            x[0] = 3
        elif(Warehouse_block == 'C'):
            x[0] = 4

        if(Mode_of_Shipment == 'Flight'):
            x[1]= 0
        elif(Mode_of_Shipment == 'Ship'):
            x[1] = 1
        elif(Mode_of_Shipment == 'Road'):
            x[1] = 2

        x[2] = Customer_care_calls
        x[3] = Customer_rating
        x[4] = cost_of_the_Product
        x[5] = Prior_purchases
        x[6] = Product_importance

        if(Gender == 'F'):
            x[7]= 0
        elif(Gender == 'M'):
            x[7] = 1

        x[8] = Discount_offered
        x[9] = Weight_in_gms

        x = x.reshape(1,-1)
        x = Data_normalizer.transform(x)

        xx=model.predict(x)

        prob=model.predict_proba(x)[0]
        n_reach = prob[0]
        reach = prob[1]

        print('There is a {0:.2f}% chance that your product will reach in time'.format(reach*100))
        print (xx)

        return render_template("predict.html", ans = 'There is a {0:.2f}% chance that your product will reach in time'.format(reach*100))

if __name__ == '__main__' :
    print(model.predict(Data_normalizer.transform(np.array([1, 1, 1, 1, 200, 3, 1, 1, 50, 1000]).reshape(1,-1))))
    app.run()