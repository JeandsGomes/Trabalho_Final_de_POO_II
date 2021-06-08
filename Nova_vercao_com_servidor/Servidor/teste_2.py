lista = [1,2,3]
string = ''
for elemento in lista:
    string = string + '//' + str(elemento)
print(string)
print(string.split('//')[1:])