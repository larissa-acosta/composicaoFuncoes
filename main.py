from sympy import *

x = Symbol('x')
f = expand(input("Insira f(x): "))
g = expand(input("Insira g(x): "))
quest = input("Deseja substituir o x por um número? ")

if (quest.lower() == "sim"):
    num = input("Insira um número: ")

    fog = f.subs(x, g.subs(x, num))
    gof = g.subs(x, f.subs(x, num))
    gog = g.subs(x, g.subs(x, num))
    fof = f.subs(x, f.subs(x, num))
else:
    fog = str(f.subs(x, g)).replace("**", "^")
    gof = str(g.subs(x, f)).replace("**", "^")
    gog = str(g.subs(x, g)).replace("**", "^")
    fof = str(f.subs(x, f)).replace("**", "^")

print(f"f o g  = ", fog)
print(f"g o f = ", gof)
print(f"g o g = ", gog)
print(f"f o f = ", fof)
