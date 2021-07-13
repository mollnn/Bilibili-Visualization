import jieba
txt = "你好，你是猪吗，反正我不是！"

def wordFreqCount(txt):
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key = lambda x:x[1], reverse=True)
    return items

print(wordFreqCount(txt))