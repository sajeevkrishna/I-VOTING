import datetime 
import hashlib 
import json
import requests
class block:
    def __init__(self,index,transaction,previous_hash,nonce):
        self.index=index
        self.transaction=transaction
        self.previous_hash=previous_hash
        self.nonce=nonce
        self.tostring=transaction+index+previous_hash+nonce
    def compute_hash(self):
        return hashlib.sha256((self.tostring).encode()).hexdigest()
class blockchain:
    peers=set()
    def __init__(self):
        self.chain=[]
        genesisproof=self.proofofwork('nota0null')
        self.chain.append(block('0','nota','null',genesisproof))
    def last(self):
        return self.chain[-1]
    @staticmethod
    def proofofwork(string):
        nonce=1
        difficulty=3
        while(1):
            strin=string+str(nonce)
            temphash=hashlib.sha256(strin.encode()).hexdigest()
            if temphash[:difficulty]=='0'*difficulty:
                return str(nonce)
            else:
                nonce+=1
    def isvalid(self):
        difficulty=3
        for i in range(1,len(self.chain)):
            if self.chain[i-1].compute_hash()!=self.chain[i].previous_hash:
                return False
            if self.chain[i].compute_hash()[:difficulty]!='0'*difficulty:
                return False
        return True
    def mine(self,transaction):
        lastblock=self.last()
        index=str(int(lastblock.index)+1)
        prev_hash=lastblock.compute_hash()
        string=transaction+index+prev_hash
        nonce=self.proofofwork(string)
        self.chain.append(block(index,transaction,prev_hash,nonce))
        if self.isvalid():
            pass
        else:
            self.chain.pop()
        #send a copy to all peers