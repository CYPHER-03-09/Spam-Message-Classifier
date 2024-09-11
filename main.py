from flask import Flask, render_template, request
from SpammessageidentifierwithPythonFunction import predict_spam  # Import the predict_spam function

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
    message = request.form['message']
    result = predict_spam(message)
    return render_template('result.html', result=result)
  else:
    return f"<h1>405 Method Not Allowed</h1>"  # Handle non-POST requests

if __name__ == '__main__':
  app.run(debug=True)