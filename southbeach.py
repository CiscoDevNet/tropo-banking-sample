# Voice script

from time import sleep

# greeting message
say("Welcome to South Beach Bank, Voice Banking")
sleep(1)

# ask for account number
accountNumber = ask("Please enter your 10 digit account number", {
	"choices": "[10 DIGITS]",
	"attempts": 3,
	"onBadChoice": lambda event : hangup() #Hangup if no valid entry after 3 tries
	})
analystPhone = "+1"+accountNumber.value #We'll re-use the 'account number' as a phone# to call for Option 3 below

sleep(1) #Pause one second

say("How can we help?  Please enter the number corresponding to the following option")

#main menu instructions to be spoken
mainMenu = 'Select, 1, for your account balance. Select, 2, to review recent transactions. Select, 3, to speak to a representative.'

#Some dummy account transaction data for use with Option 2 below
transactions = [
	{"TimeStamp": "February 13, 2015", "Payee": "FTD Florists", "Amount": "$75.15"},
	{"TimeStamp": "February 14, 2015", "Payee": "Outback Steak House", "Amount": "$94.00"},
	{"TimeStamp": "February 15, 2015", "Payee": "Denny's Restaurant", "Amount": "$26.00"}
]

while True: #loop in the main menu forever, until the caller hangs up
	option = ask(mainMenu, {"choices": "1,2,3"}) #speak the main menu instructions and obtain a response

	# if option 1 'account balance' is selected
	if option.value == "1":
		balance='$'+accountNumber.value[:-2]+'.'+accountNumber.value[-2:] #Turn the 'account number' into a dollar value
		say("Account balance. Your account balance is "+balance) #speak the account balance
		sleep(1)
		
	# if option 2 'review recent transactions' is selected		
	if option.value == "2":
		redFlags = False #if the caller flags a transaction for review, we'll set this to True
		say('Recent transactions.  Please listen to each transaction, then indicate whether the transaction should be approved or flagged for review.')
		sleep(1)
		for i in range(len(transactions)): #loop through all of the transactions
			say('Transaction number '+str(i+1))
			say(transactions[i]['TimeStamp'])
			say('For payee, '+transactions[i]['Payee'])
			say('In the amount of, '+transactions[i]['Amount'])
			approve=ask('Press, 1, to confirm this transaction.  Press, 2, to flag this transaction for review.', {"choices": "1,2"})
			if approve.value == "1":
				say('Transaction approved.')
			else:
				redFlags = True
				say('Transaction flagged for review.')
		if redFlags: #if any of the transactions were flagged for review
			say('You have indicated that one or more transactions should be reviewed.')
			say('Please hold while we connect you to the next available analyst, who can help resolve these transactions.')
			sleep(1) #Pause 1 second
			#transfer the call to the phone number composed from the original 'account number'
			transfer(analystPhone, {
				"playvalue":"http://www.phono.com/audio/holdmusic.mp3",
				"onTimeout": lambda event : say("Sorry.  No analysts are available."),
				})
			hangup() #After the transfer, end this session
				
	# if option 3 'speak to a representative' is selected
	if option.value == "3":
		say("Speak to a representative.")
		say('Please hold while we connect you to the next available representative.')
		sleep(1) #Pause 1 second
		#transfer the call to the phone number composed from the original 'account number'
		transfer(analystPhone, {
			"playvalue":"http://www.phono.com/audio/holdmusic.mp3",
			"onTimeout": lambda event : say("Sorry.  No analysts are available."),
			})
		hangup()

	say("Main menu") # Ready to start main menu loop again
