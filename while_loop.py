#simple 'WHILE' loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

print("")

#my while loop

i = 0
v = 10
while i <= v:
    i += 1
    if i == v:
        print("Amazing it works!")
    elif i != v+1:
        print("invalid")
    else:
        break
