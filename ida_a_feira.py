n = int(input())
while n > 0:
    d = {}
    l = {}
    fruits = int(input())
    for t in range(fruits):
        fruta, preço = input().split()
        d.update({fruta : float(preço)})
    total = int(input())
    gasto = 0
    for frutas in range(total):
        fruta1, quantidade = input().split()
        gasto += d.setdefault(fruta1) * int(quantidade)
    print(f'R$ {gasto:.2f}')
    n -= 1
