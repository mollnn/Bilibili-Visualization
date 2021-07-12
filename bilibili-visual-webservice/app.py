from flask import Flask, jsonify, render_template
from flask.helpers import make_response
import connectorSSHMySQL as msql
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/api/demo/')
def api_demo():
    return jsonify(msql.query("bilibili", "select view, danmaku from Vinfo;"))


@app.route('/api/test/')
def api_test():
    ans = jsonify({
        "product": [5, 20, 36, 10, 10, 20]
    })
    return make_response(ans)


if __name__ == '__main__':
    app.run(debug=True)
