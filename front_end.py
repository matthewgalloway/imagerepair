from flask import Flask, escape, request, render_template



app=Flask(__name__)
@app.route('/')
def my_form():
    return render_template('accept_user_input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return text

app.run(host='0.0.0.0', port=5000)
