from random import choice

claves = ('0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz!"·$%&/()=?¿.,-_')

longitud = 10

l = ""

l = l.join([choice(claves) for i in range(longitud)])

print (l)