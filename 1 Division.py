def main():
    a = int(input("Entrer le valeur de a : "))
    b = int(input("Entrer le valeur de b : "))
    quotient = math.floor(a/b)
    reste = a%b
    ratio = a/b
    print("le quotient est :", quotient)
    print("le reste est : ", reste)
    print("le ratio est : ", ratio)
if __name__ =='__main__':
    main()
