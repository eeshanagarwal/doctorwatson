
from flask import Flask, request, redirect
import twilio.twiml
import csv
import json
import re
from pprint import pprint
from collections import Counter
from twilio.rest import TwilioRestClient


app = Flask(__name__)
 # The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)
 
# Try adding your own number to this list!
callers = {
    "+16508669177": "Eeshan",
}
 
@app.route("/", methods=['GET', 'POST'])

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
        


def hello_monkey():
	body = request.values.get('Body', None)
	message = search_disease(body)

	r = twiml.Response()
	r.message = message
	return str(r)

 
  #   from_number = request.values.get('From', None)
  #   if from_number in callers:
  #       message = callers[from_number] + ", thanks for the message!"
  #   else:
  #       message = "Bro, thanks for the message!"
 	
 	# if counter > 0:
	
 
if __name__ == "__main__":
    app.run(debug=True)