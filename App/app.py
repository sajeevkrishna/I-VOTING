from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        aadharno=request.form.get('aadharno')
        voterid=request.form.get('voterid')

@app.route('/templates/app.html',methods=['GET','POST'])
def verify():
    if request.method=='GET':
        return render_template('app.html')
    if request.method=='POST':
        otp=request.form.get('OTP')

@app.route('/templates/clist.html',methods=['GET','POST'])
def ballot():
    if request.method=='GET':
        return render_template('clist.html')
    if request.method=='POST':
        vote=request.form.get('vote')

@app.route('/templates/result.html')
def result():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)