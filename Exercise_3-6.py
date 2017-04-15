'''***********************************************************************************************
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
***********************************************************************************************'''

guests = ['Ahmed','Jamshed','Shahid']
for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

print("\nMr. " + guests[1] + " will not able to make it to dinner\n")

#Replace Mr. 'Jamshed' with new person
guests[1]= "Shahrukh"

for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

print("\nWe found a bigger dinning table and are inviting some more friends on dinner\n")

guests.insert(0,"Imran")
guests.insert((round(len(guests)/2)),"Murtaza")
guests.append("Saad")

for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

