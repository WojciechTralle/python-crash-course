#slicing a list
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
#slice with everything from the beginning until element at specified index
print(players[:4])
#slice that includes the end of the list
print(players[2:])

players = ['charles','martina','michael','florence','eli']
#last three elements of the list:
print(players[-3:])
#last two elements of the list:
print(players[-2:])
#print the entire list
print(players[:])
#print every second player starting with second player in the list:
print(players[1::2])
#print every second player starting at the beginning
print(players[::2])

#looping through a slice
players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())









