"""Kalkulators ar 4 darb."""

def sas(a,b):
    return a+b

def atn(a,b):
    return a-b

def kap(a,b):
    return a**b

def dal(a,b):
    try:
        return round(a/b, 5)
    except ZeroDivisionError:
        return "idiots"

def rei(a,b):
    return round(a*b, 5)

def main():
    sk1 = float(input("Skaitlis1: "))
    sk2 = float(input("Skaitlis2: "))
    print("""
        1-sask
        2-atne
        3-reiz
        4-dal""")

    darb=int(input("darbība: "))

    if darb==1:
        print(sas(sk1,sk2))
    elif darb==2:
        print(atn(sk1,sk2))
    elif darb==3:
        print(rei(sk1,sk2))
    elif darb==4:
        print(dal(sk1,sk2))
    else:
        print("idiots")

if __name__=="__main__":
    main()