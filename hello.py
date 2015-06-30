from flask import Flask, request, redirect
import twilio.twiml
import json
from collections import Counter
import urllib2

app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
	"+16508669177": "Eeshan",
}

def search_disease(symptoms):
	with open('finalDB.json') as data_file:    
		data = json.load(data_file)
	matchingDs = []

	for aSymptom in symptoms:
		
		for x in data:
			symsm = x['Symptom'].split(",")

			for s in symsm:
				if aSymptom in s:
					matchingDs.append(x['Disease'])
	counterC = Counter(matchingDs)
	return str(counterC.most_common(3)) 

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	body = request.values.get('Body', None)
	symptoms = body.split(",")

	req = urllib2.Request("https://raw.githubusercontent.com/eeshanagarwal/doctorwatson/master/finalDB.JSON")
	opener = urllib2.build_opener()
	f = opener.open(req)
	data = json.loads(f.read())

	# with open('finalDB.json') as data_file:    
	# 	data = json.load(data_file)
	matchingDs = []

	for aSymptom in symptoms:
		for x in data:
			symsm = x['Symptom'].split(",")

			for s in symsm:
				if aSymptom in s:
					matchingDs.append(x['Disease'])
	counterC = Counter(matchingDs)

	message = str(counterC.most_common(3)) 
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)
 
if __name__ == "__main__":
	app.run(debug=True)


