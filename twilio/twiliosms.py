from twilio.rest import TwilioRestClient
from time import gmtime, strftime

print("Twilio message test")

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token   = "ec33fd1862a7700578ef67050cdba290"

client = TwilioRestClient(account, token)

message = client.messages.create(to="+17326820887", from_="+17323336281",
    body="Hello from IDT's Twilio App!")
