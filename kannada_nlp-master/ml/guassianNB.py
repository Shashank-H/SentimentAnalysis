# # -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
msg=pd.read_table('data-110.txt',delim_whitespace=False,names=['msg'])
label=pd.read_table('data_label.txt',delim_whitespace=False,names=['label'])
data = pd.concat([msg,label],axis=1)
msg = data.msg
label = data.label

xtrain = msg[20:]
xtest = msg[:20]
ytrain = label[20:]
ytest = label[:20]

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain).toarray()
xtest_dtm=count_vect.transform(xtest)

from sklearn.naive_bayes import GaussianNB
knn = GaussianNB().fit(xtrain_dtm, ytrain)
predicted = knn.predict(xtest_dtm.toarray())

from sklearn import metrics
print('Accuracy metrics')
print('Accuracy of the classifer is',metrics.accuracy_score(ytest,predicted)*100)