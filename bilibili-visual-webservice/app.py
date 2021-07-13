from flask import Flask, jsonify, render_template
from flask.helpers import make_response
import connectorSSHMySQL as msql
from flask_cors import CORS

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
# 指定浏览器渲染的文件类型，和解码格式；
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

CORS(app, resources=r'/*')


@app.route('/api/demo/')
def api_demo():
    return jsonify(msql.query("bilibili", "select view, danmaku from Vinfo;"))


@app.route('/api/view/range')
def api_view_range():
    return jsonify(msql.query("bilibili", "select min(view) as mn, max(view) as mx from Vinfo;"))


@app.route('/api/view/distrib/<d>')
def api_view_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(view/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/likes/range')
def api_likes_range():
    return jsonify(msql.query("bilibili", "select min(likes) as mn, max(likes) as mx from Vinfo;"))


@app.route('/api/likes/distrib/<d>')
def api_likes_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(likes/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/coin/range')
def api_coin_range():
    return jsonify(msql.query("bilibili", "select min(coin) as mn, max(coin) as mx from Vinfo;"))


@app.route('/api/coin/distrib/<d>')
def api_coin_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(coin/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/favorite/range')
def api_favorite_range():
    return jsonify(msql.query("bilibili", "select min(favorite) as mn, max(favorite) as mx from Vinfo;"))


@app.route('/api/favorite/distrib/<d>')
def api_favorite_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(favorite/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/duration/range')
def api_duration_range():
    return jsonify(msql.query("bilibili", "select min(duration) as mn, max(duration) as mx from Vinfo;"))


@app.route('/api/duration/distrib/<d>')
def api_duration_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(duration/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/reply/range')
def api_reply_range():
    return jsonify(msql.query("bilibili", "select min(reply) as mn, max(reply) as mx from Vinfo;"))


@app.route('/api/reply/distrib/<d>')
def api_reply_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(reply/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/type/distrib')
def api_type_distrib():
    return jsonify(msql.query("bilibili", "select tname, count(*) as cnt from Vinfo group by tname order by cnt desc;"))


@app.route('/api/v/info/<bv>')
def api_vinfo(bv):
    return jsonify(msql.query("bilibili", """select * from Vinfo where bvid = "{bv}";""".format(bv=bv), isDict=True))


@app.route('/api/v/danmu/freq/<cid>')
def api_v_danmu_freq(cid):
    return jsonify(msql.query("bilibili", """select floor(floattime) as t, count(*) as cnt from Danmu where cid="{cid}" group by floor(floattime) order by t;""".format(cid=cid)))


@app.route('/api/test/')
def api_test():
    ans = jsonify({
        "product": [5, 20, 36, 10, 10, 20]
    })
    return make_response(ans)


if __name__ == '__main__':
    app.run(debug=True)
