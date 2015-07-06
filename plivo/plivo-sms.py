import plivo

auth_id 	= "MANDU1Y2Y0ZMQYOTE5MZ"
auth_token 	= "NDEzMzM2ZmRlNTMxZmMxYmZiNzMxOWVkN2QzZTY1"

p = plivo.RestAPI(auth_id,auth_token)

params = {
	'src': '+13305206782',
	'dst': '+17326820887',
	'text': 'Plivo test SMS from IDT!',
	'type': 'sms',
}

p.send_message(params)