from keras.layers.core import Activation, Dense
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM,SimpleRNN
from keras.models import Sequential,load_model
from keras import optimizers
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import collections
import jieba
import pickle
import numpy as np
from keras.models import load_model
from button1 import *
PN=[]

model=load_model('RnnModel.h5')
MAX_SENTENCE_LENGTH = 40

pkl_file = open('myfile.pkl', 'rb')
word_index = pickle.load(pkl_file)
pkl_file.close()

def pre():
    global Content
    global PN
    ##### custom test data
    #INPUT_SENTENCES =['推','高調','RIP','笑死人了','柯P加油','政治','再帶風向阿','下去領500','承認','T','醜宅','蔡英文','臭甲', '他人還不錯啊','台女不意外','ez','廢物滾','新北','ㄈㄈ尺','母豬教','水桶','一家親','假新聞','崩潰噓','低能','賣國賊','國民黨','廢文','素質']
    INPUT_SENTENCES=Content
    XX = np.empty(len(INPUT_SENTENCES),dtype=list)
    # word2vec
    i=0
    for sentence in  INPUT_SENTENCES:
        words = jieba.cut_for_search(sentence)
        seq = []
        for word in words:
            if word in word_index:
                seq.append(word_index[word])
            else:
                seq.append(word_index['UNK'])
        XX[i] = seq
        i+=1
    
    # 補齊維度
    XX = sequence.pad_sequences(XX, maxlen=MAX_SENTENCE_LENGTH)

    # predict
    labels=[]
    #labels = [int(round(x[0])) for x in model.predict(XX) ]
    for x in model.predict(XX):
        labels.append(int(round(x[0])))
    label2word = {1:'正面', 0:'負面'}

    # show result
    for i in range(len(INPUT_SENTENCES)):
        if INPUT_SENTENCES[i][0]=='R' or INPUT_SENTENCES[i][0]=='[':
            continue
        PN.append(label2word[labels[i]])
        #PN.append(labels[i])
        #print('{}   {}'.format(label2word[labels[i]], INPUT_SENTENCES[i]))
if __name__ == '__main__':
    pre()
