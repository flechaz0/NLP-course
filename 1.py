import jieba  # 用jieba库进行分词
import xlwt    #用于创建表格
import pandas as pd

#先把指定数据集的content导出到txt方便分词与词频统计
data = pd.read_csv(r'D:\桌面文件\Study\NLP\期末\datasets\dataset_1.csv',usecols=[3])
data_list = data.values.tolist()
content = []
for item in data_list:
     content.append(item[0])
with open('content.txt', 'w', encoding='utf-8') as f:
    for item in content:
         f.write(str(item))
# 读取数据
text = open('content.txt', 'r', encoding='utf-8').read()
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords
stopwords = stopwordslist('stopwords.txt')
# 先进行分词
words = jieba.cut(text, cut_all=False, HMM=True)
# 去停用词,统计词频
word_ = {}
for line in words:
    sline = line.split()
    for word in sline:
        if word not in stopwords:
            if word != ' ':
                if word in word_:
                    word_[word] += 1
                else:
                    word_[word] = 1

# 将词汇和词频以元组的形式保存
word_freq = []
for word, freq in word_.items():
    word_freq.append((word, freq))

# 进行降序排列
word_freq.sort(key=lambda x: x[1], reverse=True)

#把词频统计（前50）输出到Excel表格
book = xlwt.Workbook(encoding = 'utf-8')
sheet = book.add_sheet('word')
col = ('关键词','词频')
for i in range(0,2):
    sheet.write(0,i,col[i])
for i in range(50):
     word, freq = word_freq[i]
     sheet.write(i+1,0,word)
     sheet.write(i+1,1,freq)
     print(word, freq)
savepath = 'Word frequency.xls'
book.save(savepath)


