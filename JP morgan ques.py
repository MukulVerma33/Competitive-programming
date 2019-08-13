# Data Structures in python
sentence = "The lines are printed in reverse order."
sentence = sentence.strip(".")
a = sentence.split()
a[0] = a[0].lower()

length = []

for i in a:
    length.append(len(i))

min_ele = 0

final = []

while(a):
    for i in range(len(a)):
        if(min_ele<=len(a)-1):
            if(len(a[i])<len(a[min_ele])):
                min_ele = i
        else:
            min_ele = 0
    final.append(a.pop(min_ele))

for i in a:
    final.append(i)

final[0] = final[0].capitalize()

print(" ".join(final)+'.')
    

