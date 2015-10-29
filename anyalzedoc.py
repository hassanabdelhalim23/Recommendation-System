from textblob import TextBlob as tb
from computeanylasis import computetffre
class compute:
    CS_Fild=""
    Is_filed=""
    IT_field=""
    dict=list()

    def __init__(self):
        self.object = computetffre()
    
    def readcontent(self):
        
        ope=open('Cs.txt','r')
        ope1=open('Is.txt','r')
        ope2=open('It.txt','r')
        self.CS_Fild=ope.read().lower()
        self.Is_filed=ope1.read().lower()
        self.IT_field=ope2.read().lower()
        self.Cs=tb(self.CS_Fild)
        self.Is=tb(self.Is_filed)
        self.It=tb(self.IT_field)
        self.bloblist = [self.Cs,self.Is,self.It]

    def anyalze(self):
       for i, blob in enumerate(self.bloblist):
            # for word in blob.words:
            #     print self.object.tfidf(word, blob, self.bloblist)
            scores = {word: self.object.tfidf(word, blob, self.bloblist) for word in blob.words}
            # print scores
            self.sorted_words = sorted(scores.items(),key=lambda x: x[1], reverse=True)
            self.dict.append(self.sorted_words)
            # print self.sorted_words
            # for x in self.sorted_words:
            #     print(x)





