def criar_funcao(expressao):
  expressao = expressao.replace("^", "**")
  return lambda x: eval(expressao)

f = input("Digite a função f(x): ")
g = input("Digite a função g(x): ")

f = criar_funcao(f)
g = criar_funcao(g)

gof = lambda x: g(f(x)) # g ° f
gog = lambda x: g(g(x)) # g ° g
fof = lambda x: f(f(x)) # f ° f
fog = lambda x: f(g(x)) # f ° g

x = float(input("Digite um valor de x: "))

print(f"g ° f ({x}) = {gof(x)}")
print(f"g ° g ({x}) = {gog(x)}")
print(f"f ° f ({x}) = {fof(x)}")
print(f"f ° g ({x}) = {fog(x)}")
