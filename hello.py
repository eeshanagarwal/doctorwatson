
from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+16508669177": "Eeshan",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
 	counter = session.get('counter', 0)
 
    # increment the counter
    counter += 1
 
    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Bro, thanks for the message!"
 	
 	if(counter > 1)
 	{
 		message = "Enter your symptoms: "
 	}
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)