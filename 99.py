# Write a Program to Print the following Star Pattern.

lines =3
for x in range(lines):
    if x == 0 or x == lines-1:
        print('*'*(lines))
    else:
        print('*',end='')
        print(' '*(lines-2),end='')
        print('*')