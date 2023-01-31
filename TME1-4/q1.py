def lectureFichierEtu(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    for i in range(len(contenu)): #Boucle i variant de 0 a contenue[0]
        contenu[i]=contenu[i].split()
    monFichier.close() #Fermeture du fichier
    return contenu


def lectureFichierSpe(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    for i in range(len(contenu)): #Boucle i variant de 0 a contenue[0]
        contenu[i]=contenu[i].split()
    monFichier.close() #Fermeture du fichier
    return contenu

def GS(etu,spe):
    etu=lectureFichierEtu(etu)
    spe=lectureFichierSpe(spe)
    nb = int(etu[0][0])
    mariage=[]
    while len(mariage) < nb:  #tant que il existe un etudiant libre
        for i in range(1,nb+1):   #pour chaque etudiant
            marie = False
            for couple in mariage: #on verifie si il est deja marie
                if etu[i][1] in couple:
                    marie = True
                    break
            if not marie:  #si il est libre
                mariage.append([etu[i][1]])     #on lajoute a la liste des maries
                for j in range(2,len(etu[i])):  #pour chaque preference de l'etudiant
                    cap = int(spe[1][int(etu[i][j])+1])  #on recupere la capacite de la specialite
                    for k in range(0,len(mariage)):     #on parcourt la liste des maries
                        if etu[i][j] in mariage[k]:      #si la spe est presente dans la liste des maries
                            cap = cap - 1
                    if cap > 0:     #si la specialite n'est pas pleine
                        mariage[i-1].append(etu[i][j])  #on ajoute la spe a l'etudiant
                        break
                    #else:
                        #for s in reversed(spe[j]):  #on parcourt la liste des preferences de la specialite
                            #if etu[s+1][1] in mariage[i]:
                                #break
                            
    #mariage.remove(mariage[0])
    return mariage
print(GS("PrefEtu.txt","PrefSpe.txt"))
