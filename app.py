from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
with open('customer_subscription_analysis.pickle','rb') as r_model:
    model=pickle.load(r_model)

print('model is loaded')

@app.route('/')
def index():
    return{"status": "server is running"}
    
@app.route('/pred',methods=['POST'])
def pred():
    data=request.get_json(force=True) 
    pred=model.predict(data['inputs'])
    return{'predictions':pred}
if __name__=='__main__':
    app.run()