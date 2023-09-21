from sympy import *

x = Symbol('x')
f = expand(input("Insira f(x): "))
g = expand(input("Insira g(x): "))
quest = input("Deseja substituir o x por um número? ")

if (quest.lower == "sim"):
    num = input("Insira um número: ")

    fog = f.subs(x, g.subs(x, num))
    gof = g.subs(x, f.subs(x, num))
    gog = g.subs(x, g.subs(x, num))
    fof = f.subs(x, f.subs(x, num))
else:
    fog = f.subs(x, g)
    gof = g.subs(x, f)
    gog = g.subs(x, g)
    fof = f.subs(x, f)

print(f"f o g  = ", fog)
print(f"g o f = ", gof)
print(f"g o g = ", gog)
print(f"f o f = ", fof)
