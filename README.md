#Tropo Scripting (Python) - Banking Example

##Overview: This script provides a short demonstration of various Tropo features as they might be used in a banking environment:

- Answer incoming call
- Play a text-to-speech (TTS) message to the caller
- Retrieve DTMF input from the caller
- Process and play an account balance
- Play out a list of 'recent transactions' which the user can 'Confirm' of 'Flag for review' via DTMF
- Transfer a call to a third party ('analyst')

The script is self-contained, can be used concurrently, is commented, and can be uploaded and used on any Tropo account with 'outbound' voice calling enabled (contact Tropo support.)

##Caveats: The script does not work with SMS; invalid input and other error checking is minimal and may cause unexpected behaviour.

##ow to Run the Demo:

- Upload the script to your Tropo account as a new script, and assign it a phone # (note: outbound calling must be enabled)
- Call the script phone #
- At the prompt, enter a 10 digit 'account number'.  Note, this number should actually be the phone number of a second phone, to which the caller will be transferred in later steps
- At the main menu, select Option '1' to hear an account balance.  The value is calculated from the 'account number' previously entered, e.g. 4055551212 -> $40,555,512.12
- At the main menu, select Option '2' to hear a series of transactions.  
	- Select Option '2' ('Flag for review') on at least one transaction to trigger a transfer to the 'analyst' phone #.  Note: this will end the session
- (Start the session again if needed) At the main menu, select Otion '3' to be transferred to the 'analyst' phone #
- Hangup at any time to reset the script
