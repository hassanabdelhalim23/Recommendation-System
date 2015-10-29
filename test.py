from anyalzedoc import compute
from textblob import TextBlob as tb
class Recommendersystem:
    object=compute()
    lists=list()
    def init(self):
        self.object.readcontent()
        self.object.anyalze()
        lists=list()
    def Recommend(self,TEXT):
        for x in  self.object.dict:
            sum=0
            for  word,item in x[:9]:
                 test=tb(TEXT)
                 if test.words.count(word) !=0:
                     sum=sum+1
            self.lists.append(sum/float(9*3)) # 6 is the top 6 & 3 is the number of files, IT, IS, CS
        index=self.lists.index(max(self.lists))
        if index ==0:
            return "we Recommend CS"
        if  index==1:
            return "we Recommend IS"
        if  index==2:
            return "we Recommend It"
