import pandas as pd
from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('models/catboost_model-2.pkl','rb'))

def model_prediction(features):
    test_data=pd.DataFrame(features)
    predection=model.predict(test_data)
    return int(prediction)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
    
    
    
@app.route('/predict',method=['POST'])
def predict():
    if request.method=='POST':
       Age=int(request.form['Age'])
       RestingBp=int(request.form['RestingBp'])
       Cholesterol = int(request.form['Cholesterol'])
       Oldpeak = float(request.form['Oldpeak'])
       FastingBS = int(request.form['FastingBS'])
       MaxHR = int(request.form['MaxHR'])
       prediction=model.predict([[Age,RestingBp,Cholesterol,Oldpeak,FastingBS,MaxHR]])
       if prediction[0]==1:
          return render_template('index.html',prediction_text="Kindly make an appointment with the doctor!")
       else:
          return render_template('index.html'prediction_text="You are well! no worry")
    else:
       return render_template('index.html')
       
       
if __name__=="__main__":
   app.run(host='0.0.0.0',port=5000,debug=True)
   
       
