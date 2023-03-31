print("Enter the elements via coma without spaces: ")
userList1 = [x for x in input("List 1: ").split(',')]
userList2 = [x for x in input("List 2: ").split(',')]
userList3 = [x for x in input("List 3: ").split(',')]

for userList in [userList1, userList2, userList3]:
    for uniqueEl in set(userList):
        userList.remove(uniqueEl)

print(set(userList1 + userList2 + userList3))
