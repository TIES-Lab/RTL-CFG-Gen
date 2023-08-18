# import os
# import re

def lst2str_con(lst_in: list[str], with_spc: bool = 0) -> str:
    str_out = ''
    # if want space in between words insert 1 as argument
    if with_spc:
        for i in lst_in:
            str_out += ' ' + i
    else:
        for i in lst_in:
            str_out += i
    str_out = str_out.strip()
    return str_out

def str2lst_con(str_in: str):
    lst_out = str_in.split('\n')
    return lst_out

def get_assignment(line: str)-> list[str]:
    if '=' in line:
        temp = [x for x in re.split(r'\(|\)| ', a) if x != '']
        temp2: list = [x for x in temp if '=' in x]
        temp3 = []
        for i, x in enumerate(temp2):
            temp3.append(x.replace('<=', ' <= ') if '<=' in x else x.replace('=', ' = '))
        return temp3
    else:
        print('no assignments here')