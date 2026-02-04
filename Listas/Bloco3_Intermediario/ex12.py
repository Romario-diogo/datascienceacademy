palavras = ["sol", "python", "lua", "dados", "api", "codigo", "web", "teste", "ia", "lista"]
novas_palavras = []
for p in palavras:
    if len(p) >= 5:
        novas_palavras.append(p)

print(novas_palavras)