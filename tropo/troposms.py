from tropo import all

event = call("+14075550100", {
	"network":"SMS"})
event.value.say("Don't forget your meeting at 2 p.m. on Wednesday!")