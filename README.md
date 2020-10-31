# I-VOTING
A SECURE VOTING PORTAL FOR THE ELECTION COMMISION OF INDIA

## DESCRIPTION
`
**PRE-REQUISITES FOR THE SOLUTION:**
	Voter-IDs are categorized into 2 classes; namely offline and online.
	Offline Voter-IDs can be used only at the EVMs.
	Similarly offline voter-IDs can be used only in the online voting portal.
	The voter can choose either type of the voter-ID before the commencement of the election.
	Every Voter-ID must be linked with the Aadhar card.
	
**WORK-FLOW OF THE SOLUTION:**
	1. Before the election commences, the voter can choose his voting preference(online or offline).
	2. The offline voting takes place parallely and will not interfere in the online voting mechanism.
	**OFFLINE VOTING:**
		This takes place as usual.
	**ONLINE VOTING:**
		i. The voter logs into the portal using his aadhar-linked voterid. It is checked to prevent double voting.
		ii. The voter, is permitted into the secret ballot page using multi-factor authentication.
		  The credentials are;
			OTP recieved via aadhar mobile number.
			Fingerprint authentication (stored in the aadhar database)
			Iris scan authentication (stored in the aadhar database)
		iii. The secret ballot opens upon successful verification of the above data.
		iv. The voter clicks the button of the preferred candidate.
		v. The blockchain is mined and the transaction is appended to the chain. The name of the author is encrypted
		   to prevent data leak in the public blockchain.
		vi. The voter can view the real time poll statistics.
		vii. Voting can be available from 6:00 am to 9:00 pm unlike offline voting.
	3. The votes of the online and offline streams are added together to give the final results.

**ADVANTAGES:**
	**AVAILABILITY:** Increased online voting duration ensures that the 29 lakh lost votes are polled.
	**FLEXIBILITY:** Classifying voter-ids does not strictly enforce online voting to the technologically weaker sections and provides flexibility.
	**FAKE-PROOF:** Linking voter-IDs with aadhar can prevent fake-votes.
	**CUTTING EDGE TECH:** Employs the state-of-art blockchain and RSA encryption technologies.
	**FAST:** Provides real-time results.
	**SECURE & TRANSPARENT:** Eliminates booth rigging and accusations of ballot riggings.
	**ROBUST:** Multi-factor authentication is an equivalent alternative for indelible ink.

**TECHNOLOGY STACKS USED:**
	PYTHON 3.8.0 (SERVER SIDE LANGUAGE)
		FLASK FRAMEWORK
	RSA ENCRYPTION ALGORITHM
	BLOCKCHAIN (PUBLIC)
	HTML
	JAVASCRIPT
	CSS, BOOTSTRAP
	SHA256 ALGORITHM
`

### RUNNING THE APP

Clone the project 
```
$ git clone https://github.com/sajeevkrishna/I-VOTING
```

Install the dependencies
```
cd App
pip install -r requirements.txt
```

Run the flaskapp with
```
app.py
```

### License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)
