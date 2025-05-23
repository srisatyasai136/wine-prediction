from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures
import os


app=Flask(__name__) # our flask app


@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/predict') # rendering the html template
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['GET','POST']) # route for our prediction
def predict():
    
    # loading model which we saved
    

    # print(os.path.dirname(__file__))
    model_path = os.path.join(os.path.dirname(__file__), 'wineQuality_new.pkl')
    model = pickle.load(open(model_path, 'rb'))

    # model = pickle.load(open('wineQuality_new1.pkl', 'rb'))
 
    data = [[x for x in request.form.values()]] 
    print(data)   
    
    pred= model.predict(data)[0]
    print(pred)
    if pred==0:
        prediction="Bad"
    else:
        prediction="Good"
    
    return render_template('pred.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,port=5000)