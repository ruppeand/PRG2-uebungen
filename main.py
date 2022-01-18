from ball import *

#Objekt erzeugen -> eine Instanz von Ball erzeugen
ball_player = Ball()
print(ball_player.x)
print(ball_player.y)
print(ball_player.r)

#zweites Objekt
ball_machine = Ball()
print(ball_machine.r)
ball_machine.r = 17
print(ball_machine.r)
print(ball_player.r)