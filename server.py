from flask import Flask, send_from_directory,request,jsonify
from nn import digitRecogniser
app = Flask(__name__)

@app.route('/')
def hello_world():
   return send_from_directory("templates", "index.html")

# @app.route('/dist/<path:path>')
# def send_report(path):
#     return send_from_directory('public', path)

@app.route('/digit', methods =['GET'])
def getValue():
    index=request.args.get("index")
    value=digitRecogniser(int(index))
    print(value)
    res={
        "predictedValue":str(value)
    }
    return jsonify(res)
    # return "predicted value:"+str(value)


if __name__ == '__main__':
   app.run(port=8000,debug=True)