#Exercise 3-4
#If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.
guest_list = ['Maria C.','Arnold','LuckyLuke','A.C.Doyle']
print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Dear Mr. {guest_list[3]}. I really enjoyed your novel the 'Hound of Baskervilles', and even though you're deceased I'd love to invite you for dinner!")

#Exercise 3-5
#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still
#in your list.
guest_list = ['Maria C.','Arnold','LuckyLuke','A.C.Doyle']
print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Dear Mr. {guest_list[3]}. I really enjoyed your novel the 'Hound of Baskervilles', and even though you're deceased I'd love to invite you for dinner!")


print(f"Unfortunately, {guest_list[3]} can't make it to dinner because he's deceased.")
guest_list.remove('A.C.Doyle')
guest_list.append('RandomGuy')
#print(guest_list)

print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Hi {guest_list[3]}. I'd love to invite you for dinner because you're just so random...")


#Exercise 3-6
#You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#call to the end of your program informing people that you found a bigger
#dinner table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

guest_list = ['Maria C.','Arnold','LuckyLuke','A.C.Doyle']
print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Dear Mr. {guest_list[3]}. I really enjoyed your novel the 'Hound of Baskervilles', and even though you're deceased I'd love to invite you for dinner!")


print(f"Unfortunately, {guest_list[3]} can't make it to dinner because he's deceased.")
guest_list.remove('A.C.Doyle')
guest_list.append('RandomGuy')
#print(guest_list)

print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Hi {guest_list[3]}. I'd love to invite you for dinner because you're just so random...")

print("Dear all, I have just found a bigger table, so there's more space available.")
guest_list.insert(0, 'TheFirstGuy')
#print(guest_list)
guest_list.insert(int(len(guest_list)/2),'TheMiddleGuy')
#print(guest_list)
guest_list.append('TheLastGuy')

print(guest_list)

print(f"Hello {guest_list[0]}. You're the first guy, so just come!")
print(f"Hello {guest_list[1]} I wonder how you're doing these days. So you're invited.")
print(f"Hi {guest_list[2]}. You're no longer the middle guy, but you're still invited.")
print(f"Hi {guest_list[3]}. Are you still lifting weights and doing protein drinks with Shnapps? Come to dinner!")
print(f"Hello {guest_list[4]}. I still don't know you, but it's ok.")
print(f"You're still pretty random, but you can come.")
print(f"I'm sorry to announce that you're the last on the list, but it's fine for dinner...")

#Exercise 3-7
guest_list = ['Maria C.','Arnold','LuckyLuke','A.C.Doyle']
print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Dear Mr. {guest_list[3]}. I really enjoyed your novel the 'Hound of Baskervilles', and even though you're deceased I'd love to invite you for dinner!")


print(f"Unfortunately, {guest_list[3]} can't make it to dinner because he's deceased.")
guest_list.remove('A.C.Doyle')
guest_list.append('RandomGuy')
#print(guest_list)

print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Hi {guest_list[3]}. I'd love to invite you for dinner because you're just so random...")

print("Dear all, I have just found a bigger table, so there's more space available.")
guest_list.insert(0, 'TheFirstGuy')
#print(guest_list)
guest_list.insert(int(len(guest_list)/2),'TheMiddleGuy')
#print(guest_list)
guest_list.append('TheLastGuy')

print(guest_list)

print(f"Hello {guest_list[0]}. You're the first guy, so just come!")
print(f"Hello {guest_list[1]} I wonder how you're doing these days. So you're invited.")
print(f"Hi {guest_list[2]}. You're no longer the middle guy, but you're still invited.")
print(f"Hi {guest_list[3]}. Are you still lifting weights and doing protein drinks with Shnapps? Come to dinner!")
print(f"Hello {guest_list[4]}. I still don't know you, but it's ok.")
print(f"You're still pretty random, but you can come.")
print(f"I'm sorry to announce that you're the last on the list, but it's fine for dinner...")

print(f"I can only invite two people for dinner! Sorry!")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}! I'm sorry but there are not enough tables!")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}! I'm sorry but there are not enough tables!")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}! I'm sorry but there are not enough tables!")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}! I'm sorry but there are not enough tables!")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}! I'm sorry but there are not enough tables!")

print(f"Hi {guest_list[0]}! You're still invited!")
print(f"Hi {guest_list[1]}! You're still invited!")


del guest_list[0]
del guest_list[0]
print(guest_list)






