d = {
        'W' : 1,
        'H' : 1/2,
        'Q' : 1/4,
        'E' : 1/8,
        'S' : 1/16,
        'T' : 1/32,
        'X' : 1/64}  
while 1 > 0:   
    m = input().split('/')
    if m == ['*']:
        break
    co = 0
    for s in m[1:-1]:
        c = 0
        for n in s:
            c += d[n]
        if c == 1:
            co += 1
    print(co)
