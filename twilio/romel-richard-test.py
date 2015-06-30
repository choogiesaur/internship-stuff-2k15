from twilio.rest import TwilioRestClient
import random

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token   = "ec33fd1862a7700578ef67050cdba290"

group = ["+17326820887", "", ""] 
twilio_num = "+17323336281"

client = TwilioRestClient(account, token)

for recipient in group:
	sms = client.messages.create(to=recipient, from_=twilio_num, body="This is a test message to Romel and Richard.")
