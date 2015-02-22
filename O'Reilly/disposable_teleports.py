#def checkio(teleports_string):
    


teleports_string = "12,23,34,45,56,67,78,81,17,28"
t = teleports_string.replace(",", " ")
current_string = t.split()

i = 1
k = 0
numbs = []
while True:
    for index, element in enumerate(t.split()):
        if str(i) in element:
            k = element.replace(str(i),"")
#            current_string[index] = element.replace(str(i),"")
            numbs.append(k)
    print(numbs)
    
    break
#    i += 1

a = ['12', '34']
a.remove(a[0])
