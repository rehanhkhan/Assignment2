'''***********************************************************************************************
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
of your program.
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

print("\nWe are sorry as we can invite only two people for dinner \n")

for i in range(0,len(guests)-2):
    removed_guest = guests.pop(0)
    print("Mr." + removed_guest + " I am sorry as I can’t invite you to dinner due to some administrative issue")

print('\n')

for i in range(0,len(guests)):
    print("Dear Mr. " + guests[0] + " your are still invited to dinner party")
    del(guests[0])


print(guests)

