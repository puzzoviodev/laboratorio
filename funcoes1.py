def Myfun(x,y=4,prompt=True):
    res = x*y
    if prompt:
        print("resposta é %i", res)

    return res

Myfun(3)
Myfun(3,prompt=False)
Myfun(3,5,True)

