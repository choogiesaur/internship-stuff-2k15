import plivo, random

auth_id 	= 'MANDU1Y2Y0ZMQYOTE5MZ'
auth_token 	= 'NDEzMzM2ZmRlNTMxZmMxYmZiNzMxOWVkN2QzZTY1'

plivo_num 	= '+13305206782'
recipient 	= '+17326820887'

p = plivo.RestAPI(auth_id,auth_token)

threshold = 50
num = random.randint(0,100)

if num > threshold:

	message = "Alert! Value " + str(num) + " is > than the threshold " + str(threshold)
	print(message)

	params = {
		'src': plivo_num,
		'dst': recipient,
		'text': message,
		'type': 'sms',
	}
	
	p.send_message(params)

elif num <= threshold:

	message = "Safe. Value " + str(num) + " is <= the threshold " + str(threshold)
	print(message)
	
	params = {
		'src': plivo_num,
		'dst': recipient,
		'text': "Safe. Value " + str(num) + " is <= the threshold " + str(threshold),
		'type': 'sms',
	}
	
	p.send_message(params)
