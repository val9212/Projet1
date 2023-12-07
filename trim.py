
#def search_for_exact_occurrence(seq, adaptateur, threshold):
#  """
#  """
#  adapT = adaptateur[0:threshold]
#  position = -1  
#  i= 0
#  nseq = ''
#  while i < len(seq)-len(adapT) and nseq != adapT:
#    i = i+1 

#    if seq.find('N') != -1 :
#      nseq = no_N(seq[i:i+len(adapT)], adapT) 
#    else: 
#      nseq = seq[i:i+len(adapT)]

#    if nseq == adapT:
#      position = i
#  return(position)

import doctest

def hamming_Dist(seq, adapt):
  """
  Calcule la distance de Hamming entre deux séquences de même longueur.

  Parameters
  ==========
  seq : str
      La première séquence.
  adapt : str
      La deuxième séquence à comparer.

  Returns
  =======
  int
      Le nombre de positions où les séquences diffèrent.

  Exemples
  >>> hamming_Dist('CTGTCTCTNNNNCACATCTGACGCTGCCGACGA', 'CTGTCTCTTATACACATCTGACGCTGCCGACGA')
  4

  >>> hamming_Dist('CTGTCTCTTATACACATCTGACGCTGCCGACGN', 'CTGTCTCTTATACACATCTGACGCTGCCGACGA')
  1
  """
  distance = 0 #Initialisation de la variable distance.
  for s in range(len(seq)): #s prend une valeur de 0 à la longueur de la séquence, à chaque fois, on compare le caractère s de la séquence au caractère s de l'adaptateur.
    if seq[s] != adapt[s]:
      distance += 1 #Si il y a une différence, alors la variable distance augmente de 1.
  return(distance)

def no_N(seq, adap):
  """
  Remplace les bases 'N' dans une séquence par les bases correspondantes de l'adaptateur.

  Parameters
  ==========
  seq : str
      La séquence avec des bases 'N' à remplacer.
  adap : str
      L'adaptateur à utiliser pour le remplacement.

  Returns
  =======
  str
      La séquence résultante après le remplacement des 'N'.
  
  Exemples
  >>> no_N('CTGTCTCTNNNNCACATCTGACGCTGCCGACGA' ,'CTGTCTCTTATACACATCTGACGCTGCCGACGA')
  'CTGTCTCTTATACACATCTGACGCTGCCGACGA'

  >>> no_N('ATNNCG','ATTACG')
  'ATTACG'
  """
  lseq = list(seq) #On reformate la séquence et l'adaptateur en liste.
  ladap = list(adap)
  for s in range(len(lseq)): #s prend une valeur de 0 à la longueur de la séquence, à chaque fois, on compare le caractère s de la séquence, si c'est un N.
    if lseq[s] == 'N': #Alors on remplace le N par le nucléotide de l'adaptateur.
      lseq[s] = ladap[s]
  return(''.join(lseq))

def search_for_approximate_occurrence(seq,adapt,max_mismatches,threshold):
  """
  Trouve la position d'un adaptateur dans une séquence donnée en vérifiant les correspondances et les mismatches.

  Parameters
  ==========
  seq : str
      La séquence dans laquelle on recherche l'adaptateur.
  adapt : str
      L'adaptateur que l'on souhaite trouver dans la séquence.
  max_mismatches : int
      Le nombre maximum de mismatches autorisé pour considérer une correspondance.
  threshold : int
      La longueur du préfixe de l'adaptateur à utiliser pour la recherche.

  Returns
  =======
  int
      La position de l'adaptateur dans la séquence ou -1 si l'adaptateur n'est pas trouvé.
  
  Exemples
  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTNNNNCACATCTGACGCTGCCGACGAGCGATCTAGTGTAG','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 0, 10)
  54

  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGDDDCTGTCTCTNNNNCACATCTGACGCTGCCGACGAGCGATCTAGTGTAG','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 3, 10)
  54

  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTTATACACATCTGACGCTGCCG','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 0, 10)
  54

  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTDDDDCANNNCTGACGCTGCCG','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 4, 10)
  54

  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTTA','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 0, 10)
  54

  >>> search_for_approximate_occurrence('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCT','CTGTCTCTTATACACATCTGACGCTGCCGACGA', 0, 10)
  -1
  """
  #La variable adapT contient le préfixe de l'adaptateur de longueur treshold.
  position = -1  #Position est initialisée à -1 et retournée telle quelle si non trouvée dans la séquence.
  p= 0 #Initialisation de la variable p pour la boucle while 
  nseq = '' 
  diff = max_mismatches + 1
  while p < len(seq) and nseq != adapt and diff > max_mismatches and threshold < len(seq[p:]): #boucle tant que, s'arrête si p > a longueur de la séquence moins celle adapT, que nseq est différent d'adapT et que diff > max_mismactch.
    p = p+1 #On augmente i de 1 à chaque itération de la boucle.

    if len(seq[p:])>=len(adapt): #Si la restante de la séquence est plus longue que celle de l'adaptateur, alors on recherche une occurrence complète de ce dernier.
      if seq[p:p+len(adapt)].find('N') != -1 : #On vérifie si il y a ou non des N dans la séquence.
        nseq = no_N(seq[p:p+len(adapt)], adapt) #Si il y en a, on appelle la fonction no_N pour récupérer la séquence sans N et on met la séquence dans la variable nseq.
      else: 
        nseq = seq[p:p+len(adapt)] #Si il n’y a pas de N on met la variable directement dans nseq.

      if nseq == adapt: #Si nseq est pareil que adapT alors la variable position prend la valeur p.
        position = p
      elif max_mismatches > 0: #Si la tolérance de mismatchs est supérieure à 0, alors on appelle la fonction hamming distance pour calculer la distance de hamming entre l'adaptateur et la séquence.
        diff = hamming_Dist(nseq, adapt)
        if diff <= max_mismatches: #Si la variable diff, qui correspond au nombre de différences entre l'adaptateur et la séquence est inférieure ou égale a mismatchs alors position prend la valeur p.
          position = p
    else: #Autrement, on cherche le préfixe de l'adaptateur contre le suffixe de la séquence.
      adapt = adapt[0:len(seq[p:])]
      if seq[p:].find('N') != -1 : #On vérifie si il y a ou non des N dans la séquence.
        nseq = no_N(seq[p:], adapt) #Si il y en a, on appelle la fonction no_N pour récupérer la séquence sans N et on met la séquence dans la variable nseq.
      else: 
        nseq = seq[p:] #Si il n’y a pas de N on met la variable directement dans nseq.

      if nseq == adapt: #Si nseq est pareil que adapT alors la variable position prend la valeur p.
        position = p
      elif max_mismatches > 0: #Si la tolérance de mismatchs est supérieure à 0, alors on appelle la fonction hamming distance pour calculer la distance de hamming entre l'adaptateur et la séquence.
        diff = hamming_Dist(nseq, adapt)
        if diff <= max_mismatches: #Si la variable diff, qui correspond au nombre de différences entre l'adaptateur et la séquence est inférieure ou égale a mismatchs alors position prend la valeur p.
          position = p

  return(position)


def remove_adapt(seq, position):
  """
  Supprime une portion de séquence jusqu'à une position donnée.

  Parameters
  ==========
  seq : str
      La séquence d'origine.
  position : int
      La position jusqu'à laquelle la séquence doit être tronquée.

  Returns
  =======
  str
      La séquence tronquée.

  Exemples
  >>> remove_adapt('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTNNNNCACATCTGACGCTGCCGACGAGCGATCTAGTGTAG', 54)
  'GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTC'

  >>> remove_adapt('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCTTATACACATCTGACGCTGCCG', 54)
  'GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTC'

  >>> remove_adapt('GCCTATATTTCGTTTTTCTGAGACCTATCCGAGTTCAGTGCGACCGTACAGCTCCTGTCTCT', 2)
  'GC'
  """
  clear = seq[0: position] #La variable clear contient les caractères de la séquence de la position 0 à la valeur de position.
  return(clear)

def remove_qual(qual, position):
  """
  Supprime une portion de données de qualité jusqu'à une position donnée.

  Parameters
  ==========
  qual : str
      Les données de qualité d'origine.
  position : int
      La position jusqu'à laquelle les données de qualité doivent être tronquées.

  Returns
  =======
  str
      Les données de qualité tronquées.
  """
  clear = qual[0:position] #La variable clear contient les caractères de la qualité de la position 0 à la valeur de position.
  return(clear)



doctest.testmod()      
