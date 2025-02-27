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

def GS_etu(etu,spe):
    etu=lectureFichierEtu(etu)
    spe=lectureFichierSpe(spe)
    nb = int(etu[0][0]) #on recupere le nombre d'etudiants
    etuM = []
    mariage=[]
    for i in range(0,nb):
        mariage.append([etu[i+1][1]])
    while len(etuM) < nb:  #tant que il existe un etudiant libre
        for i in range(0,nb):   #pour chaque etudiant
            if i not in etuM:  #si il est libre
                
                for j in range(2,len(etu[i+1])):  #pour chaque preference de l'etudiant
                    cap = int(spe[1][int(etu[i+1][j])+1])  #on recupere la capacite de la specialite
                    for k in range(0,len(mariage)):     #on parcourt la liste des maries
                        if etu[i+1][j] in mariage[k]:      #si la spe est presente dans la liste des maries
                            cap = cap - 1
                    if cap > 0:     #si la specialite n'est pas pleine
                        etuM.append(i) #on le maries
                        mariage[i].append(etu[i+1][j])  #on ajoute la spe a l'etudiant
                        break
                    else:
                        spei = spe[int(etu[i+1][j])+2]  #on recupere la liste des preferences de la specialite
                        for s in reversed(spei):  #on parcourt la liste des preferences de la specialite dans l'ordre inverse
                            if i == int(s): #si l'etudiant libre est le dernier de la liste des preferences de la specialite
                                break # proposition rejetee
                            if int(s) in etuM and etu[i+1][j] in mariage[int(s)]: # si le dernier etudiant choisi dans la specialite est celui qui est marie
                                etuM.remove(int(s)) #on le supprime de la liste des etudiants maries
                                mariage[int(s)].remove(etu[i+1][j]) #on supprime son affectation a la specialite
                                #print("on supprime l'etudiant",s,"de la specialite",spe[j][1],"et on le remplace par l'etudiant",i,"qui est libre")
                                etuM.append(i) #on marie l'etudiant libre
                                mariage[i].append(etu[i+1][j]) #on ajoute la specialite a l'etudiant libre
                                break
                        if i in etuM: 
                            break #si l'etudiant a ete marie, on passe a l'etudiant suivant

    return mariage

def GS_spe(etu,spe):
    etu=lectureFichierEtu(etu)
    spe=lectureFichierSpe(spe)
    nbE = int(etu[0][0]) #on recupere le nombre d'etudiants
    nbS = len(spe[1])-1 #on recupere le nombre de specialites
    etuM = []
    speM = []
    mariage=[]
    for i in range(0,nbS):
        mariage.append([spe[i+2][1]])
    while len(speM) < nbS:  #tant que il existe un parcours libre
        for i in range(0,nbS):   #pour chaque parcours
            if i not in speM:  #si il est libre
                cap = int(spe[1][i+1])  #on recupere la capacite de la specialite
                for j in range(2,len(spe[i+2])):  #pour chaque preference du parcours
                    if spe[i+2][j] not in etuM:      #si l'etu n'est pas marie
                        etuM.append(spe[i+2][j]) #on le maries
                        mariage[i].append(spe[i+2][j])  #on ajoute l'etudiant à la specialite
                    else: #si l'etudiant est deja marie
                        etui = etu[int(spe[i+2][j])+1]  #on recupere la liste des preferences de l'etudiant
                        for e in reversed(etui):  #on parcourt la liste des preferences de l'etudiant dans l'ordre inverse
                            capE = int(spe[1][int(e)+1]) #on recupere la capacite de la specialite e
                            if i == int(e): #si la spe libre est la derniere de la liste des preferences de l'etudiant
                                break # proposition rejetee
                            if spe[i+2][j] in mariage[int(e)]: # si la derniere spe choisie par l'etudiant est celle qui est marie
                                if capE == (len(mariage[int(e)]) - 1 ): #si la specialite e est pleine
                                    speM.remove(int(e)) #on la supprime de la liste des specialites mariees
                                mariage[int(e)].remove(spe[i+2][j]) #on supprime son affectation a la specialite e
                                mariage[i].append(spe[i+2][j]) #on ajoute l'etudiant a la spe libre
                                break
                    if cap == (len(mariage[i]) - 1): #si la specialite est pleine
                        speM.append(i) #on la met dans la liste des specialites mariees
                        break #on passe a la specialite suivante

    return mariage

print("\nGale Shapley côté étudiant:\n", GS_etu("PrefEtu.txt","PrefSpe.txt"),"\n")

print("Gale Shapley côté parcours:\n", GS_spe("PrefEtu.txt","PrefSpe.txt"),"\n")