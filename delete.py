def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]  # 以行的形式读取停用词表，同时转换为列表
    return stopwords

stopwords = stopwordslist('stopwords.txt')
inputfile = open("二十大报告全文output.txt",'r',encoding = 'utf-8')
outputfile = open('20.txt', 'w',encoding='utf-8')
for line in inputfile:
    sline = line.split()
    for word in sline:
        if word not in stopwords:  # 判断分词后的词语是否在停用词表内
            if word != '\t':
                outputfile.write(word)
inputfile.close()
outputfile.close()



