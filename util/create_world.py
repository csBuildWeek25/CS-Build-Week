from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.sample_generator import World
import random

Room.objects.all().delete()
world = World()
world.generate_rooms(10, 10, 100)

room_descriptions = [
    'This is a generic room',
    'BOOOOMMM!',
    'AHHHH',
    'RUNN',
    'BLAMM',
    'Peace at last',
    'It only gets worse from here',
    'Go',
    'stars are awesome',
    'what will you do now?',
    'natural',
    'Fantacy',
    'today is your lucky day',
    'brooom',
]


roomTracker = {}

for row in world.grid:
    for rm in row:
        des = random.choice(room_descriptions)
        room = Room(title=f'{rm.name}', description=des)
        room.save()
        roomTracker[(rm.x, rm.y)] = room
        if rm.e_to != None:
            coords = (rm.e_to.x, rm.e_to.y)
            if coords in roomTracker:
                roomTracker[rm.x, rm.y].connectRooms(roomTracker[coords], 'e')
                roomTracker[coords].connectRooms(roomTracker[rm.x, rm.y], 'w')
        if rm.w_to != None:
            coords = (rm.w_to.x, rm.w_to.y)
            if coords in roomTracker:
                roomTracker[rm.x, rm.y].connectRooms(roomTracker[coords], 'w')
                roomTracker[coords].connectRooms(roomTracker[rm.x, rm.y], 'e')
        if rm.s_to != None:
            coords = (rm.s_to.x, rm.s_to.y)
            if coords in roomTracker:
                roomTracker[rm.x, rm.y].connectRooms(roomTracker[coords], 's')
                roomTracker[coords].connectRooms(roomTracker[rm.x, rm.y], 'n')

players = Player.objects.all()
for p in players:
    p.currentRoom = world.grid[0][0].id
    p.save()
