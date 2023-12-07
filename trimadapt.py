from iomiso import *
from trim import * 
import argparse 

def parse():
    """
    Programme permettant de faire une ligne de commande avec option.
    """
    parser = argparse.ArgumentParser(description="Programme permettant le nettoyage des reads d'un fichier Fastq, à partir d'adaptateurs donnés dans un fichier fasta. Le programme retourne les reads nettoyés avec un fichier fasta contenant les adaptateurs non trouvés.")
    parser.add_argument('-r', '--fileRead', dest="filein", required=True,
                        help="Le fichier .fastQ dont vous voulez nettoyer les reads.")
    parser.add_argument('-a', '--adapt', dest="fileadapt", required=True,
                        help="Le fichier .fasta contenant 1 ou plusieurs adaptateurs.")
    parser.add_argument('-o', '--outfile"', dest="fileout", required=True,
                        help="Le nom que vous voulez donner a votre fichier trié.")
    parser.add_argument('-t', '--treshold', dest="treshold", required=False, type=int, default= 10,
                        help="Le seuil du treshold, nombre entier. (defaut 10)")
    parser.add_argument('-m', '--maxmiss', dest="maxmiss", required=False, type=int, default= -1,
                        help="Le nombre maximum de mismatchs autorisé, nombre entier. (Defaut -1)")
    parser.add_argument('-n', '--notfount', dest="notfound", required=False, default="notfound.fasta",
                        help="Le nom du fichier fasta contenant les adaptateurs non trouvés. (defaut notfound.fasta)")
    return parser.parse_args()


#Programme Principale:
if __name__ == "__main__":
    OPTIONS = parse()
    file = OPTIONS.filein
    adapt = OPTIONS.fileadapt
    fileout = OPTIONS.fileout #On récupère les données mises dans la commande sous forme de variables.
    maxmiss = OPTIONS.maxmiss
    treshold = OPTIONS.treshold
    notfound = OPTIONS.notfound

    reads = read_fastQC(file) #On lit le fichier fastq.
    adapts = read_fasta(adapt) #On lit le fichier fasta.
    nfound = [] #Initialisation de la liste de dictionnaires Nfound

    for a in adapts: #Pour tout les adaptateurs,
        print(f"nettoyage avec l'adaptateur {a['nameAdap']} en cours... ") #on affiche la progression avec leur nom,
        for r in reads: #et pour toutes les séquences, on cherche la position de l'adaptateur.
            pos = search_for_approximate_occurrence(r['seq'], a['adap'], maxmiss, treshold )
            if pos != -1 : #Si la position est = -1 on ne modifie pas la séquence, sinon on enlève l'adaptateur grâce à la position, et on réduit la qualité de la même manière, on rajoute aussi plus 1 au "found" de l'adaptateur pour noter qu'il a été trouvé.
                r['seq'] = remove_adapt(r['seq'], pos)
                r['qual'] = remove_qual(r['qual'], pos)
                a['found'] += 1


        if a['found'] == 0 : #Tous les dictionnaires d'adaptateurs qui n'ont jamais été trouvés sont mis dans la liste Nfound. 
            nfound.append(a)
    create_fastQ(fileout, reads) #On crée le fichier avec les reads filtrés.
    print(f"le fichier contenant les reads nettoyés a bien ete créé : {fileout}")
    create_fasta(notfound, nfound) #On crée le fichier avec les adaptateurs non trouvés.
    print(f"Si des adaptateurs n'ont pas ete trouvé ils ont ete mis dans le fichier : {notfound}") #On affiche le résultat de la commande avec les fichiers créés.