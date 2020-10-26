from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")
    
# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, -1)
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='This customer will result to a Churn'
        elif int(result)== 0 : 
            prediction ='This Customer is not a Churn'            
        return render_template("result.html", prediction = prediction) 
    
if __name__ == '__main__':
    app.run(debug=True)