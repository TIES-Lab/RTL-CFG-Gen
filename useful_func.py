def Cmmnt_Fill(a: str = '', ttl_nmbr: int = 116) -> str:
    b = ''
    if a == '':
        for i in range(ttl_nmbr+2):
            b += '='
            c = '# '+ b
        return c
    eq = (ttl_nmbr - len(a))
    for i in range(eq // 2):
        b += '='
    if eq % 2 == 0:
        c = '# ' + b + ' ' + a + ' ' + b
    else:
        c = '# ' + b + ' ' + a + ' ' + b + '='
    return c

print(Cmmnt_Fill())
print(Cmmnt_Fill('Inspect'))
print(Cmmnt_Fill())