import connectorSSHMySQL as msql
import jieba

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


def doWordcut(bid):
    sqlres = msql.query(
        "bilibili", """create table ans as select text from Danmu where cid in (select cid from Vinfo where bvid = "{bid}")""".format(bid=bid))
    lst = []
    for i in sqlres:
        lst += [i[0]]
    str = ' '.join(lst)
    wf = wordFreqCount(str)
    ans = []
    cnt=100
    for i in wf:
        ans += [{"name":i[0], "value":i[1]}]
        cnt -= 1
        if cnt == 0:
            break
    return ans


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
