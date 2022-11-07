from flask import Flask

app = Flask('Flask tutorial')

@app.route('/', methods=['GET'])
def home():
    return 'hello world!'

app.run()
