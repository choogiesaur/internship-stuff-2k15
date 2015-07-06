group = ['+17326820887', '+17327057131', '+12015790427']

for number in group:
    event = call(number, {
       "network":"SMS"})
    event.value.say("Tropo test SMS from IDT!")