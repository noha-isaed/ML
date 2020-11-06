from flask import Flask , render_template , request
import csv
import pandas as pd

app = Flask(__name__)

#read parameters's file  and store it in list *1
data = pd.read_csv("lm_parameters.csv", dtype = float) 
parameters = list(data)

@app.route('/')
#function to route to html file *2
def index(): 
    return render_template('index.html') 


@app.route('/predict' , methods=['GET' ,'POST'])
#function to read parameters's file and take input from user and calculate h(X)
def Predict_Price(): 

     if request.method== "POST" :

       Theta0 = data.iloc[0][0]
       price = 0

       Features = request.form.getlist('Feature[]')  #get all input from user and store it in array *3
       
       price += float(Theta0)

       for i in range(0 , 6): #loop in parameters and features to calculate the price
         price += (float(parameters[i])*float(Features[i]))
       
       result = "The Price Of your House Is : " + str(price)
       return str(result)
       
   
if __name__ == '__main__':
  app.run(debug=True)

#1-https://stackoverflow.com/questions/31933257/python-3-how-to-read-a-csv-file-and-store-specific-values-as-variables
#2-https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
#3-https://www.semicolonworld.com/question/59783/sending-a-form-array-to-flask