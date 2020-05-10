list=["security",'computers','networks']

for count,item in enumerate(list,start=1):
    print(count,item)

list_to_strings='-'.join(list)

print(list_to_strings)

print(list_to_strings.split('-'))
print("Working on methods which alters or not")
print(list.sort())
print(list)
print(list.reverse())
print(list)

print(list.sort(reverse=True))
print(list)


name=list.pop(1)
print(name)

print(list)


print(list[0:1:1])

list.append('BigData')
print(list)

list.append('Schema')
print(list)

list.insert(4,"python")
print(list)

list.extend(['Network','Database'])
print(list)

x=list.index("Network")
print(x)
print(len(list))

