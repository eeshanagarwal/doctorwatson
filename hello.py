from flask import Flask, request, redirect
import twilio.twiml
import json
from collections import Counter
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+16508669177": "Eeshan",
}
 
@app.route("/", methods=['GET', 'POST'])

def search_disease(symptoms):
	return "ha!"
    # with open('finalDB.json') as data_file:    
    #     data = json.load(data_file)
    # matchingDs = []

    # for aSymptom in symptoms:
        
    #     for x in data:
    #         symsm = x['Symptom'].split(",")

    #         for s in symsm:
    #             if aSymptom in s:
    #                 matchingDs.append(x['Disease'])
               
    
    # counterC = Counter(matchingDs)
    # return str(counterC.most_common(3)) 

def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
 	
 	body = request.values.get('Body', None)
	message = search_disease(body)

    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)


