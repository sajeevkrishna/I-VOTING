from flask import Flask,render_template,request,redirect
from block import block
from block import blockchain

b=blockchain()

app=Flask(__name__)

def getvotes():
    d={}
    for i in range(1,len(b.chain)):
        if b.chain[i].transaction in d:
            vote=b.chain[i].transaction
            d[vote]+=1
        else:
            vote=b.chain[i].transaction
            d[vote]=1
    return d

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        aadharno=request.form.get('aadharno')
        voterid=request.form.get('voterid')

@app.route('/authentication',methods=['GET','POST'])
def verify():
    if request.method=='GET':
        return render_template('app.html')
    if request.method=='POST':
        otp=request.form.get('OTP')

@app.route('/IVM',methods=['GET','POST'])
def ballot():
    if request.method=='GET':
        return render_template('clist.html')
    #b.peers.update(myport)

@app.route('/pollstats',methods=['GET','POST'])
def result():
    d=getvotes()
    parties=list(d.keys())
    votes=list(d.values())
    return render_template('result.html',title='CURRENT POLL STANDINGS', max=6, labels=parties, values=votes)

@app.route('/mineblock',methods=['GET','POST'])
def register_vote():
    vote=request.form.get('vote')
    b.mine(vote)
    return render_template('index.html',output='THANKS FOR VOTING')

if __name__=='__main__':
    app.run(debug=True,threaded=True)