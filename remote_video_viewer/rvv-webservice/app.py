from flask import Flask, jsonify, render_template
from flask_cors import CORS
import osapi

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

CORS(app, resources=r'/*')


@app.route('/list/')
def api_list():
    return jsonify(osapi.getFileList("resource"))


@app.route('/video/<name>/')
def api_video(name):
    return osapi.getBinaryFile("resource/%s" % name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
