import smtplib
import numpy as np 
from flask import Flask,render_template,request, flash, redirect
import pickle
import pandas as pd
from cred import email, password

app= Flask(__name__)
app.secret_key = 'tappu@kappu.com'

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def MINI():
    return render_template('MINI.html') 


@app.route('/email',methods=['POST', 'GET'])
def email_send():
    if request.method == 'GET':
        return redirect('/', code=302)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)
    message = request.form['subject']
    user_email = request.form['MailId']
    session.sendmail(email, user_email, message)
    session.quit()

    flash('Contacted succefully')

    return redirect('/', code=302)


@app.route('/predict',methods=['POST'])
def predict():
   
    data1 = request.form['a']
    if data1.lower()=="male":
        data1=1
    elif data1.lower()=="female" :
        data1=0
    else :
        data1=0
    data2 = request.form['b']
    data3 = request.form['c']
    if data3.lower()=="central":
        data3=1
    else:
        data3=0
    data4 = request.form['d']
    data5 = request.form['e']
    if data5.lower()=="central":
        data5=1
    else:
        data5=0
    data6 = request.form['f']
    data7 = request.form['g']
    if data7.lower()=="y":
        data7=1
    elif data7.lower()=="n":
        data7=0
    data8= request.form['h']
    data9= request.form['i']
    if data9.lower()=="y":
        data9=1
    elif data9.lower()=="n":
        data9=0
    data10= request.form['j']

    x     = request.form['k']
    x=x.lower()
    y = { 'commerce':0, 'science':0, 'arts':0}
    y[x] = 1
    data11 = y['commerce']
    data12 = y['science']
    data13 = y['arts']

    p    = request.form['l']
    p=p.lower()
    q = { 'comm & Mng':0, 'sci & tech':0, 'others':0}
    q[p] = 1
    data14 = q['comm & Mng']
    data15 = q['others']
    data16 = q['sci & tech']


    
    # ... data16
    
    
   
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16]])

    prediction=model.predict(arr)


    return render_template('after.html',abc=prediction[0])

if __name__=="__main__":
    app.run(debug=True)  


      