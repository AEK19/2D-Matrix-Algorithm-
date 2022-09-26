# In this example we are going to be creating a matrix that gets input from the user
# each list will act as a row

# the problem when you input this function initially is that 'l' the local list is not getting emptied so after the
# .... first iteration, the local list is still accepting 4 , 5 , 6 , 7-9
# the goal is to try and empty the 'l' to avoid iteration
# to fix this delete the 'l' list in the top and put this in the functiom
# now to get a specific # within a list you can do another line of print but you set the index in it to '[1][1]'
# essentially it is list within a list and you have
# if you put 'print(m[1][3])' and you enter in row and column inputs of '3' with numbers listed from 1-9
# you get an output of out of range, so the max you can put is 0-2 because that is the range compared to the rows





r = int(input("Enter rows: "))
c = int(input("Enter column: "))

m = []

for i in range(r):
    l = []
    for j in range(c):
        v = int(input("Enter rows: "))
        l.append(v)
    m.append(l)

print(m)
print(m[1][2])














