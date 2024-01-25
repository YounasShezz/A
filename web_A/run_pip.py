import os
import pip

f = open('requirments-u.txt', 'r')
er = open('requirments-error.txt', 'w+')

for i in f.readlines():
    for ii in i:
        if i !='\n':
            try:
                pip.main(["install",ii])
            except Exception as e:
                er.write(f'{e} \n')
            else:
                pass