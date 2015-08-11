from twilio.rest import TwilioRestClient
import random

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token   = "ec33fd1862a7700578ef67050cdba290"

#my number, twilio number
group_a = ["+xxxyyyzzzz", "+aaabbbcccc"]
group_b = ["+xxxyyyzzzz", "+aaabbbcccc"]
twilio_num = "+1xxxyyyzzzz"

client = TwilioRestClient(account, token)

group_flag = bool(random.getrandbits(1))

if group_flag == True:
	for recipient in group_a:
		sms = client.messages.create(to=recipient, from_=twilio_num, body="This is a message to Group A!")
else:
	for recipient in group_b:
		sms = client.messages.create(to=recipient, from_=twilio_num, body="This is a message to Group B!")
