from twilio.rest import TwilioRestClient

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token = "ec33fd1862a7700578ef67050cdba290"

#these are the TEST credentials
#account = "ACdc5eafe1d3133241cfc9bd53f23a2785"
#token = "1b354730c3cb7981d6963ed0f80c8f42"

client = TwilioRestClient(account, token)

call = client.calls.create(to="7326820887",
		from_="7323336281",
		url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

print(call.sid)
