import plivo

auth_id 	= "MANDU1Y2Y0ZMQYOTE5MZ"
auth_token 	= "NDEzMzM2ZmRlNTMxZmMxYmZiNzMxOWVkN2QzZTY1"

p = plivo.RestAPI(auth_id,auth_token)

group = ['+17326820887', '+17327057131', '+12015790427']

for number in group:

	params = {
		'src': '+13305206782',
		'dst': number,
		'text': 'Hello from Plivo!',
		'type': 'sms',
	}
	
	p.send_message(params)