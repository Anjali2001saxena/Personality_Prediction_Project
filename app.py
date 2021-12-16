import numpy as np
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import joblib
app = Flask(__name__)
model = joblib.load("train_model.pkl")
scaler = StandardScaler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      gender = request.form['gender']
      if(gender == "Female"):
        gender_no = 1
      else:
        gender_no = 2
      age = request.form['age']
      openness = request.form['openness']
      neuroticism = request.form['neuroticism']
      conscientiousness = request.form['conscientiousness']
      agreeableness = request.form['agreeableness']
      extraversion = request.form['extraversion']
      result = np.array([gender_no, age, openness,neuroticism, conscientiousness, agreeableness, extraversion], ndmin = 2)
      final = scaler.fit_transform(result)
      personality = str(model.predict(final)[0])
      return render_template("submit.html",answer = personality)

if __name__ == '__main__':
    app.run()