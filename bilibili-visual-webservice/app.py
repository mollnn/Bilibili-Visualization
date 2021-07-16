from flask import Flask, jsonify, render_template
from flask.helpers import make_response
import connectorSSHMySQL as msql
from flask_cors import CORS
import jieba
import myhtml

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

CORS(app, resources=r'/*')


@app.route('/')
def api_index():
    return render_template("index.html")


@app.route('/getrc/<path:name>/')
def api_getrc(name):
    print(name)
    return myhtml.getRequestsContent(name)


@app.route('/api/sum/')
def api_sum():
    return jsonify(msql.query("biliview", "SELECT count(*) as scnt, cast(sum(view) as signed) as sview, cast(sum(danmaku) as signed) as sdanmaku,cast(sum(coin) as signed) as scoin, cast(sum(likes) as signed) as slikes FROM ovinfo;", isDict=True))


@app.route('/api/view/distrib/')
def api_view_distrib():
    return jsonify(msql.query("biliview", "select * from oviewdistrib;"))


@app.route('/api/likes/distrib/')
def api_likes_distrib():
    return jsonify(msql.query("biliview", "select * from olikesdistrib;"))


@app.route('/api/coin/distrib/')
def api_coin_distrib():
    return jsonify(msql.query("biliview", "select * from ocoindistrib;"))


@app.route('/api/favorite/distrib/')
def api_favorite_distrib():
    return jsonify(msql.query("biliview", "select * from ofavoritedistrib;"))


@app.route('/api/duration/distrib/')
def api_duration_distrib():
    return jsonify(msql.query("biliview", "select * from odurationdistrib;"))


@app.route('/api/reply/distrib/')
def api_reply_distrib():
    return jsonify(msql.query("biliview", "select * from oreplydistrib;"))


@app.route('/api/type/distrib/')
def api_type_distrib():
    return jsonify(msql.query("biliview", "select tname as name, cnt as value from otype;", isDict=True))


@app.route('/api/v/info/<bv>/')
def api_vinfo(bv):
    return jsonify(msql.query("biliview", """select * from ovinfo where bvid = "{bv}";""".format(bv=bv), isDict=True))


@app.route('/api/v/danmu/distrib/<bid>/')
def api_v_danmu_freq(bid):
    return jsonify(msql.query("biliview", """select t as name, cnt as value from odmdistrib where bvid = "{bid}";""".format(bid=bid), isDict=True))


@app.route('/api/v/danmu/wordcount/<bid>/')
def api_v_danmu_wordcount(bid):
    return jsonify(msql.query("biliview", """select word as name, cnt as value from odmwfreq where bvid = "{bid}";""".format(bid=bid), isDict=True))


@app.route('/api/test/')
def api_test():
    ans = jsonify(
        [1, 1, 4, 5, 1, 4]
    )
    return make_response(ans)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
