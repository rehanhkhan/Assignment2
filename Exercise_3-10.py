'''***********************************************************************************************
3-10. Every Function: Think of something you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
***********************************************************************************************'''

#mylist
a = ['Pakistan','Sind','Punjab','Balochistan','KPK','Karachi','Lahore','Islamabad','Quetta','Pishawar','Urdu','Sindhi','Punjabi','Balochi','Pashto','Bangali']

print(a[0].title())
a.append('Indus River')
print(a)
a.insert(0,'Asia')
print(a)
del a[5]
print(a)
item = a.pop(0)
print(item)
print(a)
item = a.pop()
print(item)
print(a)
a.remove('Bangali')
print(a)
a.sort
print(a)
a.sort(reverse=True)
print(a)
b = sorted(a)
print(b)
a.reverse()
print(a)
print(len(a))



