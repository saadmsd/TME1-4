def lectureFichierEtu(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    nbetu=contenu[0].split()  # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    for i in range(0,int(nbetu[0])): #Boucle i variant de 0 a contenue[0]
        contenu[i]=contenu[i].split()
    contenu=contenu[0:int(nbetu[0])] #On ne garde que les lignes contenant les preferences
    monFichier.close() #Fermeture du fichier
    return contenu


def lectureFichierSpe(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    nbetu=contenu[0].split(" ")  # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    for i in range(0,9): #Boucle i variant de 0 a contenue[0]
        contenu[i]=contenu[i+1].split()
    contenu=contenu[0:9] #On ne garde que les lignes contenant les preferences
    monFichier.close() #Fermeture du fichier
    return contenu

def GS(etu,spe):
    etu=lectureFichierEtu(etu)
    spe=lectureFichierSpe(spe)
    nb = int(etu[0][0])
    mariage=[[]]
    while len(mariage) < nb:  #tant que il existe un etudiant libre
        for i in range(1,nb):   #pour chaque etudiant
            if etu[i][1] not in mariage[i-1]:    #si l'etudiant est libre
                mariage.append([etu[i][1]])     #on lajoute a la liste des maries
                for j in range(2,len(etu[i])):  #pour chaque preference de l'etudiant
                    cap = int(spe[0][int(etu[i][j])+1])  #on recupere la capacite de la specialite
                    for k in range(0,len(mariage)):     #on parcourt la liste des maries
                        if etu[i][j] in mariage[k]:      #si la spe est presente dans la liste des maries
                            cap = cap - 1
                    if cap > 0:     #si la specialite n'est pas pleine
                        mariage[i].append(etu[i][j])  #on ajoute la spe a l'etudiant
                        break
                    """else:
                        for l in range(2,len)):
                            if etu[i][j] in mariage[l]:
                                mariage.remove(mariage[l])
                                mariage[i].append(etu[i][j])
                                break"""
    mariage.remove(mariage[0])
    return mariage


print(GS("PrefEtu.txt","PrefSpe.txt"))
