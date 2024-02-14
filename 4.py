from random import *
import string
s = 'йцукенгшщзхъфывапролджэячсмитьбюё'
sn = s + s.upper() + string.digits
print(sn)
a = ''.join([choice(sn) for x in range(10)])
print(a)