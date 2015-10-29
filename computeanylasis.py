from textblob import TextBlob as tb
import math
class computetffre:

	def tf(self,word, blob): # the word "java" was repeated 3 times in the file "CS" and hence its TF = 3 /15
		# print "TF: ", blob.words.count(word) / float(len(blob.words))
		return blob.words.count(word) / float(len(blob.words))

	def n_containing(self,word, bloblist):
		# print "n: ", sum(1 for blob in bloblist if word in blob)
		return sum(1 for blob in bloblist if word in blob)

	def idf(self,word, bloblist):
		try:
			# print self.n_containing(word, bloblist)
			value = math.log(len(bloblist) / float(self.n_containing(word, bloblist)))
			# print self.n_containing(word, bloblist)
			# print "word: ", word, len(bloblist), self.n_containing(word, bloblist), value
		except:
			value = 0
		# print "value: ", value
		return value # n_containing returns the number of files containing the word

	def tfidf(self,word, blob, bloblist):
		return self.tf(word, blob) * self.idf(word, bloblist)