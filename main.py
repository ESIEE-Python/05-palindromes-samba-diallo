#### Fonction secondaire


def ispalindrome(p):

  # votre code ici
    accents = str.maketrans("éèêëàâäîïôöûùü", "eeeeaaaiioouuu")
    p = p.translate(accents).lower()  # Supprimer les accents et convertir en minuscule
    p = p.replace(" ", "")

    p=""
    n=len(p)
    for i in range(n//2):
      if p[i]!=p[n-i+1]:
        return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for p in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(p, ispalindrome(p))


if __name__ == "__main__":
    main()