string1 = 'mama'
string2 = 'tata'

sklejone_stringi = string1 + string2
print(sklejone_stringi)

dedykowany_string = string1 + ' oraz ' + string2
print(dedykowany_string)

print(dedykowany_string[ 2 : 8 ])
print(dedykowany_string[  : 8 ])
print(dedykowany_string[ 7 :  ])
print(dedykowany_string[ 2 : -3 ])

lista = ['mama', 'pieseczek', 'wakacje', 345, 34.44]
print(lista[1:3])
print(lista[2:-1])
print(lista[2:])

print(lista[1][2:5])

print(  lista[1][2:5]   +  lista[0][:2]  )