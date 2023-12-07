def read_fasta(file):
    """
    Cette fonction permet de lire un fichier au format FASTA et de récupérer les noms (nameAdap) et les séquences (adap) qu'il contient.

    Parameters
    ==========
    fichier : str
        Le nom du fichier FASTA à lire.

    Returns
    =======
    adapt : list
        Une liste de dictionnaires contenant le nom et la séquence de l'adaptateur.
    """
    adapt = [] #Initialisation de la liste de dictionnaires des adaptateurs.
    nom = "" #Initialisation de la variable nom qui contiendra le nom des adaptateurs.
    seq = "" #Initialisation de la variable seq qui contiendra les séquences d'adaptateurs.
    with open(file, 'r') as FileIn: #Ouverture du fichier en lecture 'r'.
        for ligne in FileIn:

            if ligne.startswith('>'): #On prend les lignes qui débutent par '>'.
                if nom and seq: #On vérifie que nom et seq ne soient pas vides.
                    a = { #Création du dictionnaire contenant le nom de l'adaptateur, sa séquence, et le nombre de fois qu'il est trouvé. found est initialisé ici, mais utilisé plus tard.
                        "nameAdap" : nom,
                        "adap" : seq,
                        "found" : 0
                    }
                    adapt.append(a)
                nom = ligne.rstrip()
                seq = "" #On réinitialise la variable séquence.
            else:
                seq += ligne.rstrip()
        if nom and seq: #On vérifie que nom et seq ne soient pas vides, et on prend la dernière séquence.
            a = { #Création du dictionnaire contenant le nom de l'adaptateur, sa séquence, et le nombre de fois qu'il est trouvé. found est initialisé ici, mais utilisé plus tard.
                "nameAdap" : nom,
                "adap" : seq,
                "found" : 0
            }
            adapt.append(a)
    return(adapt)

def read_fastQC(file):
    """
    Cette fonction permet la lecture d'un fichier FASTQ, de récupérer les identifiants (ids), les séquences (seqs) et les qualités (qualites).

    Parameters
    ==========
    file : str
        Le nom du fichier FASTQ à lire.

    Returns
    =======
    sortie : list
        Une liste de dictionnaires contenant les identifiants, les séquences et les qualités.
    """
    reads = [] #Initialisation de la liste "sortie" qui contient une liste de dictionnaires dico.
    with open(file, 'r') as fileIn: #ouverture du fichier en écriture 'r'.
        lignes = fileIn.readlines() #On parcourt les lignes présentes dans le fichier et on les stocks dans la variable ligne.

        l = 0 #Initialisation de l pour la boucle.

        while l <len(lignes):
            id = lignes[l].rstrip() #stockage temporaire de la ligne l représentant l'identifiant dans la variable 'id'.
            seq = lignes[l+1].rstrip() #stockage temporaire de la ligne l+1 représentant la séquence dans la variable 'seq'.
            qualite = lignes[l+3].rstrip() #stockage temporaire de la ligne l+3 (la ligne i+2 contient seulement le '+', nous l'ignorons) représentant la qualité dans la variable 'qualite'.

            r = {
                    "id" : id,
                    "seq" : seq,
                    "qual" : qualite
                }
            reads.append(r)
            l += 4 #Passage au read suivant.

    return(reads)

def create_fasta(file, adapt):
    """
    Cette fonction crée un fichier FASTA nommé avec le nom donné dans 'file' et le remplit avec la liste des noms des adaptateurs et la liste des séquences des adaptateurs.

    Parameters
    ==========
    file : str
        Le nom du fichier à créer ou modifier.
    dico : list
        Une liste de dictionnaires contenant les données des adaptateurs.

    Returns
    =======
    str
        Un message indiquant si le fichier a été créé ou non.
    """
    if len(adapt) != 0:
        with open(file, 'w') as fileOut: #Ouverture du fichier en écriture 'w'.

            for a in adapt:
                fileOut.write(f"{a['nameAdap']}\n") #Ajout de l'id du dictionnaire a de la liste adapt.
                fileOut.write(f"{a['adap']}\n") #Ajout de la seq du dictionnaire a de la liste adapt.


def create_fastQ(file, reads):
    """
    Cette fonction crée un fichier FASTQ nommé avec le nom donné dans 'file' et le remplit avec la liste des identifiants (ids), la liste des séquences (seqs) et la liste des qualités (qualites).

    Parameters
    ==========
    file : str
        Le nom du fichier à créer ou modifier.
    dico : list
        Une liste de dictionnaires contenant les données.

    Returns
    =======
    str
        Le nom du fichier qui a été créé.
    """
    with open(file, 'w') as fileOut: #ouverture du fichier en écriture 'w'.

        for r in reads:
            fileOut.write(f"{r['id']}\n") #Ajout de l'id du dictionnaire r de la liste reads.
            fileOut.write(f"{r['seq']}\n") #Ajout de la seq du dictionnaire r de la liste reads.
            fileOut.write(f"+\n") #Ajout du +
            fileOut.write(f"{r['qual']}\n") #Ajout de la qual du dictionnaire r de la liste reads.

