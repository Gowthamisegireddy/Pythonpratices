'''1.Strings are Immutable: once we declare the sting we cannot modify it.
if we try to modify the string it will create new string

2.iF new String does not  have any refernces variable then it will be removed
 
3. Python Internally uses String Interning.

4. String Interning is the proces of checking string Intern pool
before creating any new object.

whenever we want to create new object , python first will check string 
intern pool, weather that objectb alreadyb exist or not.

when object already exist in the string intern Records then adrress
of existing object will be reused.
'''

#s1 = 'Kodnest'
#s1=s1.upper()
#print(s1)

#s1 = 'K'
#print(s1,id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2,id(s2))

print('s1 ID of H:',id(s1[0]))
print('s1 ID of w:',id(s1[0]))

print('s2 ID of o:',id(s2[-1]))
print('s2 ID of O:',id(s2[1]))

print('s1 ID of l:',id(s2[2]))
print('s1 ID of l:',id(s1[3]))
print('S2 ID of l:',id(s2[3]))

