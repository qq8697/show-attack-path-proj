from flask import Flask,Response
from flask import render_template
from flask import jsonify
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getInitData',methods=['GET','POST'])
def getInitData():
    with open('./static/data/initData.json','r')as json_file:
        data=json.load(json_file)
        print(data)
        return jsonify(data)

@app.route('/getPrePersent',methods=['GET','POST'])
def getPrePersent():
    with open('./static/data/prePersent.json','r')as json_file:
        data=json.load(json_file)
        print(data)
        return jsonify(data)

if __name__ == '__main__':
    app.run()
