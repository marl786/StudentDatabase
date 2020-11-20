#Input of students
stufreq=int(input('Please enter the number of students: '))+1
L=list(range(stufreq))
for x in range(len(L)):
    L[x]=list(range(4))

L[0][0]='NAME'
L[0][1]='EMAIL'
L[0][2]='DOB'
L[0][3]='ID'

for x in range(1, stufreq):
    L[x][0]=input("Please enter Student's Name:  ")
    L[x][1]=input(f"Please enter {L[x][0]}'s Email:  ")
    L[x][2]=input(f"Please enter {L[x][0]}'s DOB:  ")
    L[x][3]=input(f"Please enter {L[x][0]}'s Student ID:  ")
print("Please look at the following options")
print("Enter 1 for searching data")
print("Enter 2 for finding email")
print("Enter 3 for deleting data")
a=int(input("Please enter your choice: "))

#Search all info using the first Alphabet of the name(Please note if data is entered in uppercase then it should be searched in uppercase)
if (a==1):
    search=input('Please enter the alphabets: ')
    los=len(search)
    mainfound=False
    for x in L:
        name=x[0]
        z=0
        partname=name[z:z+los]
        while search!= partname and z<(len(name)-los):
            z=z+1
            partname=name[z:z+los]
        if search==partname:
            mainfound=True
            found=True
            print(x)
    if mainfound==False:
        print('Invalid Search')
elif (a==2):
    #Email finder

    search=input("Enter the name: ")
    for x in range(1, len(L)):
        if L[x][0]==search:
            print (L[x][1])
elif (a==3):
    #Delete data

    indexdel=int(input("Enter the index of data you want to delete: "))
    for x in range(4):
        L[indexdel][x]=None

        
    for x in L:
        if x[0]!=None:
            print(x)
