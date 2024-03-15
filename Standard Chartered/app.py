from flask import Flask, render_template, request, redirect, url_for,flash
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Chart']
complaints_collection = db['complaints']




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process_cheque', methods=['GET', 'POST'])
def process_cheque():
    if request.method == 'POST':
        cheque_image = request.files['cheque_image']
        if cheque_image:
            cheque_image.save('uploads/cheque_image.jpg')
            flash('Cheque image uploaded successfully')
            return redirect(url_for('home'))
        else:
            flash('Please upload a cheque image')
    return render_template('process_cheque.html')


@app.route('/raise_complaint', methods=['GET', 'POST'])
def raise_complaint():
    if request.method == 'POST':
        issuetype = request.form['issuetype']
        complaint = request.form['complaint']
        name = request.form['name']
        email = request.form['email']
        
        complaints_collection.insert_one({
            'issuetype': issuetype,
            'complaint': complaint,
            'name': name,
            'email': email,
            'reply': ''
        })
        # flash('Complaint raised successfully')
        return redirect(url_for('complaint_status'))
    return render_template('raise_complaint.html')


@app.route('/complaint_status')
def complaint_status():
    complaints = complaints_collection.find()
    return render_template('complaint_status.html', complaints=complaints)

@app.route('/reply_complaint/<complaint_id>', methods=['GET', 'POST'])
def reply_complaint(complaint_id):
    if request.method == 'POST':
        reply = request.form['reply']
        complaints_collection.update_one({'_id': ObjectId(complaint_id)}, {'$set': {'reply': reply}})
        #flash('Complaint replied successfully')
        return redirect(url_for('complaint_status'))
    complaint = complaints_collection.find_one({'_id': ObjectId(complaint_id)})
    return render_template('reply_complaint.html', complaint=complaint)


@app.route('/chat_ui')
def chat_ui():
    return render_template('chat_ui.html')

if __name__ == '__main__':
    app.run(debug=True)

