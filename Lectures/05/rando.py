import flask as fl
import numpy as np 

#Create a new web app/
app = fl.Flask(__name__)


#Add a root route.
@app.route('/')
def home():
    return app.send_static_file('index.html')
#Add a uniform route.
@app.route('/api/uniform')
def uniform():
    return {"value": np.random.uniform()}

#Add a normal route.
@app.route('/api/normal')
def normal():
    return {"value": np.random.normal()}