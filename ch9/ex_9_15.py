# Exercise 9-15
from random import choice

random_list = [1,4,23,5,'o','j','a','w',3,10,7,'v',0,2,57]

chosen_list = []
for _ in range(4):
	elt = choice(random_list)
	chosen_list.append(elt)

print(f"Any ticket matching all four elements of {chosen_list} wins a prize!")


my_ticket = []
attempt_no = 0
while sorted(my_ticket, key=str) != sorted(chosen_list, key=str):
	my_ticket = []
	for _ in range(4):
		elt = choice(random_list)
		my_ticket.append(elt)
	attempt_no += 1

print(f"You won the prize after {attempt_no} attempts!")






