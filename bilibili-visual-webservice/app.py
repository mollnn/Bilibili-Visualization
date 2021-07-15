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
    return myhtml.getRequestsContent(name)

@app.route('/api/sum/')
def api_sum():
    return jsonify(msql.query("bilibili", "SELECT count(*) as scnt, cast(sum(view) as signed) as sview, cast(sum(danmaku) as signed) as sdanmaku,cast(sum(coin) as signed) as scoin, cast(sum(likes) as signed) as slikes FROM Vinfo;", isDict=True))


@app.route('/api/view/range/')
def api_view_range():
    return jsonify(msql.query("bilibili", "select min(view) as mn, max(view) as mx from Vinfo;"))


@app.route('/api/view/distrib/<d>/')
def api_view_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(view/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/likes/range/')
def api_likes_range():
    return jsonify(msql.query("bilibili", "select min(likes) as mn, max(likes) as mx from Vinfo;"))


@app.route('/api/likes/distrib/<d>/')
def api_likes_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(likes/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/coin/range/')
def api_coin_range():
    return jsonify(msql.query("bilibili", "select min(coin) as mn, max(coin) as mx from Vinfo;"))


@app.route('/api/coin/distrib/<d>/')
def api_coin_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(coin/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/favorite/range/')
def api_favorite_range():
    return jsonify(msql.query("bilibili", "select min(favorite) as mn, max(favorite) as mx from Vinfo;"))


@app.route('/api/favorite/distrib/<d>/')
def api_favorite_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(favorite/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/duration/range/')
def api_duration_range():
    return jsonify(msql.query("bilibili", "select min(duration) as mn, max(duration) as mx from Vinfo;"))


@app.route('/api/duration/distrib/<d>/')
def api_duration_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(duration/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/reply/range/')
def api_reply_range():
    return jsonify(msql.query("bilibili", "select min(reply) as mn, max(reply) as mx from Vinfo;"))


@app.route('/api/reply/distrib/<d>/')
def api_reply_distrib(d):
    return jsonify(msql.query("bilibili", "select v*{d} as val ,count(v) as cnt from (select floor(reply/{d}) as v from Vinfo) as T group by v order by v;".format(d=str(d))))


@app.route('/api/type/distrib/')
def api_type_distrib():
    return jsonify(msql.query("bilibili", "select tname as name, count(*) as value from Vinfo group by tname order by cnt desc;", isDict=True))

@app.route('/api/type/distrib10/')
def api_type_distrib_10():
    return jsonify(msql.query("bilibili", """ select tname as name, cast(cnt as signed) as value from (select tname, count(*) as cnt from Vinfo vv1 
    group by tname order by cnt desc limit 10) as t1 union all select "其它",cast(sum(cnt) as signed) as cnt from (select tname, count(*) 
    as cnt from Vinfo vv2 group by tname order by cnt desc limit 10,99) as t2""", isDict=True))


@app.route('/api/v/info/<bv>/')
def api_vinfo(bv):
    return jsonify(msql.query("bilibili", """select * from Vinfo where bvid = "{bv}";""".format(bv=bv), isDict=True))

@app.route('/api/v/danmu/freq/<bid>/')
def api_v_danmu_freq(bid):
    return jsonify(msql.query("bilibili", """select floor(floattime) as t, count(*) as cnt from Danmu where cid in (select cid from Vinfo where bvid = "{bid}" ) group by floor(floattime) order by t;""".format(bid=bid)))


def wordFreqCount(txt):
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items


@app.route('/api/v/danmu/wordcount/<bid>/<int:cnt>/')
def api_v_danmu_wordcount(bid, cnt):
    sqlres = msql.query(
        "bilibili", """select text from Danmu where cid in (select cid from Vinfo where bvid = "{bid}")""".format(bid=bid))
    lst = []
    for i in sqlres:
        lst += [i[0]]
    str = ' '.join(lst)
    wf = wordFreqCount(str)
    ans = []
    for i in wf:
        ans += [{"name":i[0], "value":i[1]}]
        cnt -= 1
        if cnt == 0:
            break
    return jsonify(ans)


@app.route('/api/test/')
def api_test():
    ans = jsonify({
        "product": [5, 20, 36, 10, 10, 20]
    })
    return make_response(ans)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
