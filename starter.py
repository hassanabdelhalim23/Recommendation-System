#!/usr/bin/python

from flask import Flask, request, jsonify
from flask import render_template
from test import Recommendersystem

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		object=Recommendersystem()
		object.init()
		stop_words = 'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,love,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,really,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,totally,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'.split(',')
		message = []
		for i, value in enumerate(request.form['nicedit-message'].lower().split(" ")):
			if value in stop_words:
				continue
			message.append(value)
		message = ' '.join(message)
		print (message)
		recommendation = object.Recommend(message)
		return render_template('index.html', rcm=recommendation)
	
	return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run()