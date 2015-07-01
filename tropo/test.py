from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):

	t = Tropo()

	t.call(to="+17326820887", network = "SMS")
	t.say("Tag, you're it!")
	
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)