a=1
b=1.2
c="7"
d=True
e=False

print(a+b)


#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+int(c))


print(str(a)+c)

"""
2.2
8
17

"""

print(d)

print(d and e)

print(d or e)

"""
True
False
True
"""

print(not d)
print(not e)