from twilio.rest import TwilioRestClient
from time import gmtime, strftime

print("Twilio message test at: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()))

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token   = "ec33fd1862a7700578ef67050cdba290"

#these are the TEST credentials
#account = "ACdc5eafe1d3133241cfc9bd53f23a2785"
#token = "1b354730c3cb7981d6963ed0f80c8f42"

client = TwilioRestClient(account, token)

txt = "tracing this with wireshark @ " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
message = client.messages.create(to="+17326820887", from_="+17323336281",
    body=txt)