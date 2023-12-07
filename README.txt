Le programme trimadapt.py est un programme qui permet, à partir d'un fichier FastQ contenant des reads et d'un fichier Fasta contenant des séquences d'adaptateurs, de filtrer les reads pour retirer les adaptateurs. Le programme retire les adaptateurs qui sont les préfixes des reads.

Pour utiliser le programme, faite la commande 'python3 trimadapt.py' ajoutez -h pour obtenir de l'aide. Vous y trouverez les différents paramètres obligatoires et les paramètres optionnels : python3 trymadapt -h.

Le programme est divisé en 3 fichiers Python différents :
Le fichier trimadapt.py, c'est le programme principal qui exécute le programme global en appelant les différentes fonctions des autres fichiers.

Le fichier trim.py contient les fonctions de filtrage. Il est composé de 5 fonctions fonctionnelles : 

 - search_for_approximate_occurrence(seq, adapt, max_mismatches, threshold): Cette fonction permet de trouver la position d'un adaptateur dans une séquence en se basant sur un seuil de similarité défini par le threshold, tout en prenant en compte les "N" dans les séquences. La fonction est capable de chercher une occurrence approximative de l'adaptateur en se basant sur la distance de Hamming. Vous pouvez définir une distance maximale avec la variable max_mismatches. Si la valeur de max_mismatches est inférieure ou égale à 0, la fonction n'effectuera pas le calcul de la distance de Hamming.
 - remove_adapt(seq, position) et remove_qual(qual, position): Ces fonctions qui permettent de retirer l'adaptateur de la séquence s'il est présent, ainsi que la partie de qualité associée.
 - hammming_dist(seq, adapt): Cette fonction qui calcule la distance de Hamming entre deux séquences de même longueur.
 - no_N(seq, adapt): Cette fonction qui remplace les bases "N" dans une séquence par les bases correspondantes de l'adaptateur.

Le fichier iomiso.py contient les fonctions de lecture et d'écriture de fichiers au format Fasta et FastQ :

 - read_fasta(file): Cette fonction est capable de lire un fichier multi-fasta et de retourner ses données sous forme de liste de dictionnaires.
 - read_fastQC(file): Cette fonction est capable de lire un fichier fastQ et de retourner ses données sous forme de liste de dictionnaires.
 - create_fasta(file, dico): Cette fonction est capable, à partir d'un nom de fichier donné et d'une liste de dictionnaires, de créer un fichier multi-fasta..
 - create_fastQ(file, dico): Cette fonction est capable, à partir d'un nom de fichier donné et d'une liste de dictionnaires, de créer un fichier fastQ.

Le programme est completement fonctionnel : 
 - Programme capable de lire un fichier fastQ et fasta ✅
 - Programme capable d'écrire un fichier fastQ et fasta ✅
 - Programme capable de filtrer les adaptateurs des reads :
  - En s'adaptant avec les "N" ✅
  - En prenant en compte les mismatchs ✅
  - En prenant en compte plusieurs adaptateurs, et en retournant ceux qui n'ont pas été trouvés ✅

Exemples d'utilisations :

  Voici des exemples d'utilisation :


    Le fichier ./Exemples/notfound.fasta contient un adaptateur introuvable dans les échantillons: Sample.fastq, Sample0.fastq et sample1.fastq.

        python3 trimadapt.py -r ./Exemples/Sample.fastq -a ./Exemples/Exemple_1.fasta -o out.fastq -t 10
        Le programme retourne un fichier : out.fastq. Cet exemple reprend les 3 séquences présentes dans le projet, dont la séquence avec les 'N'.
    
        python3 trimadapt.py -r ./Exemples/Sample.fastq -a ./Exemples/Exemple_1.fasta -o out3.fastq -t 6 -m 0
        Le programme retourne un fichier : out3.fastq. Cet exemple reprend les 3 séquences présentes dans le projet. En réduisant le seuil du threshold à 6, nous trouvons aussi l'adaptateur dans la troisième séquence.
    
        python3 trimadapt.py -r ./Exemples/Sample.fastq -a ./Exemples/Exemple_0.fasta -o out2.fastq -t 6 -m 3 -n pastrouve.fasta
        Le programme retourne deux fichiers : out2.fastq contenant les reads filtrés et pastrou.fasta l'adaptateur 2 non trouvé.
    
        python3 trimadapt.py -r ./Exemples/Sample0.fastq -a ./Exemples/Exemple_0.fasta -o sample.fastq -t 10 -n introuvable.fasta
        Le programme retourne deux fichiers : sample.fastq (fichier sample0.fastq non modifié) et introuvable.fasta contient l'adaptateur introuvable.

        python3 trimadapt.py -r ./Exemples/Sample0.fastq -a ./Exemples/Exemple_0.fasta -o sampletest.fastq -t 10 -n notfound2.fasta
        Le programme retourne deux fichiers : sampletet.fastq (modifié) et notfound2.fasta contient 3 adaptateurs non trouvés.

        python3 trimadapt.py -r ./Exemples/SRR1972920.fastq -a ./Exemples/Exemple_2.fasta -o clear_SRR1972920.fastq -n notfound_E1.fasta
        Le programme retourne un fichier : clear_SRR1972920.fastq (~155 Mo), pas de notfound_E1.fasta car notre échantillon contient trop de base 'N' l'adaptateur est donc de nouveau reconnu lors du deuxième passage.


        En faisant varier les paramètres, et en rendant notre programme plus sensible, nous pouvons avoir un résultat avec aucun adaptateur, mais avec une sensibilité accrue, il est possible que des bouts de séquence qui n'étaient	pas des adaptateurs ont été retirés. La modification de ces paramétres nous permet d'obtenir le meilleur résultat, mais ce dernier n'est peut-être pas objectif. 
        
        python3 trimadapt.py -r ./Exemples/SRR1972920.fastq -a ./Exemples/Exemple_2.fasta -o clear_SRR1972920.fastq -n notfound_E1.fasta -m 14 -t 20
        Le programme retourne un fichier : clear_SRR1972920.fastq (~126 Mo), pas de notfound_E1.fasta car notre échantillon contient trop de base 'N' l'adaptateur est donc de nouveau reconnu lors du deuxième passage.
