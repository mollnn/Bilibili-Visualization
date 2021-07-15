from flask import Flask, jsonify, render_template
from flask.helpers import make_response
from flask_cors import CORS
import myhtml

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

CORS(app, resources=r'/*')

@app.route('/getrc/<path:name>')
def api_getrc(name):
    return myhtml.getRequestsContent(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
