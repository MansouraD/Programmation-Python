def main():
    R1 = int(input("Merci de saisir la résistance R1 : "))
    R2 = int(input("Merci de saisir la résistance R2 : "))
    R3 = int(input("Merci de saisir la résistance R3 : "))
    RS = R1 + R2 + R3
    RP = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R1 * R3)
    print("La résistance en série est de : ",RS)
    print("La résistance parralèle est de : ",RP)

if __name__ == '__main__':
    main()
