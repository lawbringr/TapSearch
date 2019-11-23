from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
import re
import PyPDF2
import pickle
from django.conf import settings
import os


def seperateDoc(doc):
    docs = doc.split('\r\n\r\n')
    return docs

def parseText(docs,count):
    texts, words = {}, set()
    for i, doc in enumerate(docs):
        txt = re.findall(r'\w+', doc.lower())
        words |= set(txt)
        texts['Doc'+str(i+count)] = txt
    return texts, words

def createInvertedIndex(doc,count):
    texts, words = parseText(doc,count)
    invindex = {word:list(txt for txt, wrds in texts.items() if word in wrds) for word in words}
    return invindex

def updateDict(dic):
    old=getDict()
    if len(old)>0:
        merged=merge(old,dic)
    else:
        merged=dic
    with open('static/data.p', 'wb') as fp:
        pickle.dump(merged, fp, protocol=pickle.HIGHEST_PROTOCOL)

def getDict():
    data={}
    try:
        with open('static/data.p', 'rb') as fp:
            data = pickle.load(fp)    
    except EOFError:
        pass
    return data

def merge(a,b):
    copy=b.copy()
    add={}
    for key in b.keys():
        if key not in a.keys():
            add[key] = b[key]
            del copy[key]
    a.update(add)

    for key in a.keys():
        if type(a[key])!=list:
            a[key]=[a[key]]
        if key in copy.keys():
            if(type(copy[key])==list):
                a[key].extend(copy[key])
            else:
                a[key].append(copy[key])
    return a

def clearPickle():
    f = open('static/data.p', 'r+')
    f.truncate(0)

def getSearchList(term):
    inverseIndex=getDict()
    if term in inverseIndex:
        return inverseIndex[term]
    else:
        return []
    return u


def parsePDF(pdf):
    loc=settings.MEDIA_ROOT+"\\"+pdf
    pdfFileObj = open(loc, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    string=""
    pages= pdfReader.numPages 
    for i in range(pages):
        pageObj = pdfReader.getPage(i) 
        string+=pageObj.extractText()
    pdfFileObj.close() 
    deleteFile(loc)
    return string     

def deleteFile(loc):
    if os.path.exists(loc):
        os.remove(loc)
