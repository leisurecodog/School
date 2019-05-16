from keras.layers.core import Activation,Dense
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM,SimpleRNN
from keras.models import Sequential
from keras import optimizers
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import collections
import jieba
import pickle
import linecache
import tensorflow
import numpy as np
from keras.models import load_model

#nltk.download('punkt')

## analysis
# 計算訓練資料的字句最大字數
dic=[]
maxlen = 0
word_freqs = collections.Counter()
num_recs = 0
c=0
f=linecache.getlines('Gossip-Content.txt')
for line in f:
    c+=1
    tmp=line.strip().split('\t')
    if len(tmp)==1:
        continue
    dic.append(line)
    label=tmp[0]
    sentence=tmp[1]
    words = jieba.cut_for_search(sentence)
    Length=sum(1 for x in words)
    words = jieba.cut_for_search(sentence)
    if Length > maxlen:
        maxlen = Length
    for word in words:
        word_freqs[word] += 1
    num_recs += 1
    #if num_recs==20000:
        #break
print('max_len ',maxlen)
print('nb_words ', len(word_freqs))


## transform train data
MAX_FEATURES = 200000
MAX_SENTENCE_LENGTH = 40

pkl_file = open('myfile.pkl', 'rb')
word_index = pickle.load(pkl_file)
pkl_file.close()
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
'''
word_index = {x[0]: i+2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word_index["PAD"] = 0
word_index["UNK"] = 1
'''
print(len(word_index))
index2word = {v:k for k, v in word_index.items()}
X = np.empty(num_recs,dtype=list)
y = np.zeros(num_recs)
i=0


np.random.shuffle(dic)
# 讀取訓練資料，將每一單字以 dictionary 儲存
for line in dic:
    tmp=line.strip().split('\t')
    label=tmp[0]
    sentence=tmp[1]
    words = jieba.cut_for_search(sentence)
    seqs = []
    for word in words:
        if word in word_index:
            seqs.append(word_index[word])
        else:
            seqs.append(word_index["UNK"])
    X[i] = seqs
    y[i] = int(label)
    i += 1
    
# 補齊維度        
X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)

# train data and test data
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.01, random_state=42)
print(Xtrain.shape)
################### create model
HIDDEN_LAYER_SIZE = 64

#model = Sequential()
# Embedding
#model.add(Embedding(vocab_size, 128,input_length=MAX_SENTENCE_LENGTH))
# RNN model
#model.add(SimpleRNN(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))

#model.add(Dense(1))
#fully connection
#model.add(Activation("sigmoid"))
#parameter setting 
#model.compile(loss="mean_squared_error", optimizer="Adagrad",metrics=["accuracy"])
###################
model=load_model('RnnModel.h5')          
# train
model.fit(Xtrain, ytrain, batch_size=32, epochs=6)

# predict
#score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
#print("\nTest score: %.3f, accuracy: %.3f" % (score, acc))
print('{}   {}      {}'.format('預測','真實','句子'))
for i in range(50):
    idx = np.random.randint(len(Xtest))
    xtest = Xtest[idx].reshape(1,MAX_SENTENCE_LENGTH)
    ylabel = ytest[idx]
    ypred = model.predict(xtest)[0][0]
    sent = " ".join([index2word[x] for x in xtest[0] if x != 0])
    print(' {}      {}     {}'.format(int(round(ypred)), int(ylabel), sent))
    
# store model
model.save('RnnModel.h5')  # creates a HDF5 file 'Sentiment1.h5'
    
##### custom test data
INPUT_SENTENCES = ['垃圾','吃屎吧', '他人還不錯啊','畜生','廢物滾','死好','擊潰丁守中']
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
labels = [int(round(x[0])) for x in model.predict(XX) ]
label2word = {1:'正面', 0:'負面'}

# show result
for i in range(len(INPUT_SENTENCES)):
    print('{}   {}'.format(label2word[labels[i]], INPUT_SENTENCES[i]))
