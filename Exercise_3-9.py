'''***********************************************************************************************
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
***********************************************************************************************'''

guests = ['Ahmed','Jamshed','Shahid']
for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

print('\n' +str(len(guests))+' Nos. of guests are invited on dinner')

print("\nMr. " + guests[1] + " will not able to make it to dinner\n")

#Replace Mr. 'Jamshed' with new person
guests[1]= "Shahrukh"

for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

print('\n' +str(len(guests))+' guests are invited on dinner')

print("\nWe found a bigger dinning table and are inviting some more friends on dinner\n")

guests.insert(0,"Imran")
guests.insert((round(len(guests)/2)),"Murtaza")
guests.append("Saad")

for guest in guests:
    print("Dear Mr. " + guest + " your are cordially invited to dinner party")

print('\n' +str(len(guests))+' guests are invited on dinner')

print("\nWe are sorry as we can invite only two people for dinner \n")

for i in range(0,len(guests)-2):
    removed_guest = guests.pop(0)
    print("Mr." + removed_guest + " I am sorry as I can’t invite you to dinner due to some administrative issue")

print('\n' +str(len(guests))+' guests are invited on dinner\n')

for i in range(0,len(guests)):
    print("Dear Mr. " + guests[0] + " your are still invited to dinner party")
    del(guests[0])


print(guests)
