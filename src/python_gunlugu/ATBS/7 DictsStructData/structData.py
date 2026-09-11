birthdays ={'Alice' : 'Apr 1' , 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

for i in birthdays.items():
    print(i)

spam ={'color' : 'red', 'age' : 42}

for k,v in spam.items():
    print(f"Key : {k}, Value : {v}")

print(('color' in spam))

picnicItems ={'apples' : 5, 'cups' : 2}
print(f"I am bringing {str(picnicItems.get('cups',0))} cups")

print(f"I am bringing {str(picnicItems.get('eggs',100))} cups")