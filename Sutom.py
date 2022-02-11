from random import randint

def affichage():
    s = ""
    for k in range(5):
        for j in range(n):
            s += "+" + correction[k][j]
        s += "+\n"
        for j in range(n):
            s += "|"
            if len(tentatives) > k:
                s += tentatives[k][j]
            else:
                s += " "
        s += "|\n"
    s += "+" + "-+" * n + "\n"
    print(s)

def demander_mot():
    valid = False
    while(not valid):
        valid = True
        s = input("Que proposez vous? (" + str(n) + " lettres)")
        if(len(s) > len(key)):
            print("Votre proposition n'a pas le bon nombre de lettres")
            valid = False
        if(not s in words):
            print("Votre proposition n'est pas dans le dictionnaire")
            valid = False
    return s

def corriger(s):
    corr = ["-"] * n
    for c in range(len(s)):
        if s[c] in key:
            corr[c] = "o"
        if s[c] == key[c]:
            corr[c] = "v"
        correction[i] = corr

def main():
    global i
    global n
    global key
    global tentatives
    global correction
    global words

    # Choix du mot
    #--------------
    dico = open("dict_fr.txt", 'r')
    words = dico.read().splitlines()
    dico.close()
    key = words[randint(0, len(words))]

    # Initialisation des variables
    #------------------------------
    done = False
    n = len(key)
    tentatives = []
    correction = [["-"] * n] * 5
    i = 0

    print("\n\n        =============================")
    print("            Bienvenue dans SUTOM!")
    print("        =============================\n\n")
    print("Trouvez le mot mystère en proposant des mots!\nUn 'o' sera affiché au dessus des lettres qui sont présentes dans le mot,\net un 'v' au dessus de celles qui sont à la bonne place!\n\n")
    print("Le mot à trouver est en " + str(n) + " lettre.\n")
    #print(key)

    # Boucle de jeu
    #---------------
    while i < 5 and not done:
        affichage()
        s = demander_mot()
        tentatives.append(s)
        corriger(s)
        i += 1
        if(s == key):
            done = True
        s = ""

    # Affichage de la victoire
    #--------------------------
    affichage()
    if done:
        print("Vous avez gagné!")
    else:
        print("Vous avez perdu!")
        print("Le mot était: " + key)

if __name__ == "__main__":
    main()
