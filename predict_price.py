from flask import Flask , render_template , request , jsonify
import pandas as pd
import pickle , argparse
from argparse import ArgumentParser
import numpy as np

app = Flask(__name__)

def open_file():
"""
    loaded model by pickle and using path wiche the user enter it in the console
    :param: none
    :return: the model loaded from pickle file
"""
     loaded_model = pickle.load(open(path, 'rb'))
     return loaded_model

@app.route('/' , methods=['GET' ,'POST'])
def Predict_Price(): 
 """
    take features from user by 2 ways , first by post request using postman nd seconde way by get request using url 
    :param: none
    :return: Predicted home price
"""
     if request.method == "POST" :
          req_json = request.json
          # create array to store features wiche get from postman
          Features = [] 

          #using json to get feature ande add each feature to array
          Features.append(req_json['feature1'])
          Features.append(req_json['feature2'])
          Features.append(req_json['feature3'])
          Features.append(req_json['feature4'])
          Features.append(req_json['feature5'])
          Features.append(req_json['feature6'])

          #using reshape to convert from 1d array to 2d array
          New_Features = np.array(Features , dtype='float64').reshape(1,6) 
          result  =  loaded_model.predict(New_Features) 
          return jsonify(str(result))

     else:  
          Features = request.args.getlist('feature')
          New_Features = np.array(Features , dtype='float64').reshape(1,6)
          result  =  loaded_model.predict(New_Features)
          return str(result)
   
if __name__ == '__main__':
 """
    using argparse to give path of model file from user by enter it in the console and store this path in "path" 
    :param: none
    :return: path of file 
"""
     parser = argparse.ArgumentParser()
     parser.add_argument("path", type=str)
     args = parser.parse_args()
     path = args.path
     print(path)
     loaded_model = open_file()

     app.run(debug=True)

