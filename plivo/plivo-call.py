import plivo

auth_id 	= "MANDU1Y2Y0ZMQYOTE5MZ"
auth_token 	= "NDEzMzM2ZmRlNTMxZmMxYmZiNzMxOWVkN2QzZTY1"

p = plivo.RestAPI(auth_id, auth_token)

# Make Calls
params = {
    'from'			: '+13305206782', # Caller Id
    'to' 			: '+17326820887', # User Number to Call
    'ring_url' 		: "http://example.herokuapp.com/ring_url",
    'answer_url' 	: "http://example.com/answer_url",
    'hangup_url' 	: "http://example.herokuapp.com/hangup_url",
}
response = p.make_call(params)