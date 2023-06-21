t = int(input())
for cases in range(t):
    d = {}
    M, N = map(int, input().split())
    for linhas in range(M):
        chave = input()
        conteudo = input()
        d.update({chave:conteudo})
    for musica in range(N):
        frase = input().split()
        traducao = []
        for palavra in frase:
            if palavra in d:
                traducao.append(d[palavra])
            else:
                traducao.append(palavra)
        print(*traducao)
    print()
