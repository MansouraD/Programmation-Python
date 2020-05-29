def main():
    R1 = int(input("Merci de saisir la résistance R1 : "))
    R2 = int(input("Merci de saisir la résistance R2 : "))
    R3 = int(input("Merci de saisir la résistance R3 : "))
    RS = R1 + R2 + R3
    RP = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R1 * R3)
    i = int(input("Merci d'entrer 1 si vous voulez la résistance en série et 2 si vous voulez la résistance en parralèle : "))
    if (i == 1):
        print("La résistance en série est de : ", RS)
    if (i == 2):
        print("La résistance parralèle est de : ", RP)
    while (i != 1 & i != 2):
        i = int(input( "Merci d'entrer 1 si vous voulez la résistance en série et 2 si vous voulez la résistance en parralèle : "))
        if (i == 1):
            print("La résistance en série est de : ", RS)
        if (i == 2):
            print("La résistance parralèle est de : ", RP)
if __name__ == '__main__':
    main()
