from twilio.rest import TwilioRestClient

#these are the LIVE credentials!!!
account = "ACab6ad52e72143acd38066c67d687496e"
token 	= "ec33fd1862a7700578ef67050cdba290"

#these are the TEST credentials
#account = "ACdc5eafe1d3133241cfc9bd53f23a2785"
#token = "1b354730c3cb7981d6963ed0f80c8f42"

client = TwilioRestClient(account, token)

call = client.calls.create(to="8484597219",
		from_="7323336281",
		url="http://twimlbin.com/450a3717")
	"""host audio file on google drive; gen TwiML link at twimlbin.com"""
	"""https://googledrive.com/host/0B4wa-51xiOmPfkxBZVdFcWJLMlY4SEpYaExhay1YT3BFQlJaNGtHT1UtTkt2WC1KUmZRa2s/tdh_test.mp3"""

print(call.sid)

#testing github windows branching