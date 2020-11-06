from flask import Flask , render_template , request , jsonify
import pickle , argparse
from argparse import ArgumentParser
import numpy as np

app = Flask(__name__)

def open_file():

     loaded_model = pickle.load(open(path, 'rb'))
     return loaded_model

@app.route('/' , methods=['GET' ,'POST'])
def Predict_Price(): 

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

     parser = argparse.ArgumentParser()
     parser.add_argument("-n")
     args = parser.parse_args()
     path = args.n
     print(path)
     loaded_model = open_file()

     app.run(debug=True)
