from json import encoder
import connectorSSHMySQL as msql
import jieba
import json
import csv

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


def doWordcut():
    sqlres = msql.query(
        "bilibili", """select bvid, stext from (select cid,group_concat(text) as stext from Danmu group by cid) as T1 inner join Vinfo on Vinfo.cid=T1.cid;""")
    
    ans=[]
    f=open("output.csv","w",encoding="utf-8",newline="")
    cout=csv.writer(f)
    cout.writerow(["bvid","word","cnt"])
    for v in sqlres:
        bvid=v[0]
        text=v[1].replace(",","，")
        words=wordFreqCount(text)
        cnt=100
        for i in words:
            cout.writerow([bvid,i[0],i[1]])
            cnt-=1
            if cnt==0: break

    print("succ write to csv")


if __name__ == '__main__':
    doWordcut()