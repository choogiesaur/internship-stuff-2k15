from twilio.rest import TwilioRestClient
import random

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token   = "ec33fd1862a7700578ef67050cdba290"

twilio_num 	= "+1xxxyyyzzzz"
recipient 	= "+1aaabbbcccc"

client = TwilioRestClient(account, token)

threshold = 50
num = random.randint(0,100)

#num exceeds threshold, send alert
if num > threshold:
	message = "Alert! Value " + str(num) + " is > than the threshold " + str(threshold)
	print(message)
	sms = client.messages.create(to=recipient, from_=twilio_num, body=message)
#num is safe. of course you can exclude this if you just need alerts.
elif num <= threshold:
	message = "Safe. Value " + str(num) + " is <= the threshold " + str(threshold)
	print(message)
	sms = client.messages.create(to=recipient, from_=twilio_num, body=message)
