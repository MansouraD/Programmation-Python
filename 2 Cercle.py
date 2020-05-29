def main():
    rayon = int(input("Merci de saisir le rayon : "))
    Pi = math.atan(1) * 4
    surface = rayon * rayon * Pi
    perimetre = rayon * Pi * 2
    print("la surface est de : ", surface)
    print("le périmétre est de : ", perimetre)


if __name__ == '__main__':
    main()
