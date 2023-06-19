n = int(input())
d ={
    1001 : 1.50,
    1002 : 2.50,
    1003 : 3.50,
    1004 : 4.50,
    1005 : 5.50
    }
c = 0
while n > 0:
    pedido, q = map(int, input().split())
    c += d.setdefault(pedido) * q
    n -= 1
print(f'{c:.2f}')
