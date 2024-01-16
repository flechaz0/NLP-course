import jieba


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords

# 对句子进行分词
def seg_sentence(sentence):
    words = {}
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopwords.txt')
    # 加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
    wordsfreq = []
    for word, freq in words.items():
        wordsfreq.append((word, freq))

    return outstr,wordsfreq

inputs = open('content.txt', 'r', encoding='utf-8')
outputs = open('content_out.txt', 'w', encoding='utf-8')

for line in inputs:
    line_seg = seg_sentence(line)[0]
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

