# Exercice 1

# Explication
# 	les chiffres lus de gauche a droite sont croissants
#	est equivalent a 
#	les chiffres lus de droite a gauche sont decroissants
#	L'algorithme se basera sur une boucle ou a chaque repetition
#		le nombre est divise par 10 (on decale les chiffres)
#		On regarde le dernier digit de la fonction

def incrdigits(n):
	if n < 0:
		n = -n 	# Sans cela, au dernier passage dans la boucle le reste sera negatif 
			# et toujours plus petit que le plus petit

	plus_petit_nombre = 9
	while n != 0:
		reste = n%10
		if reste <= plus_petit_nombre:
			plus_petit_nombre = reste
			# si le i-eme chiffre est plus petit que le plus petit, on remplace
		else :
			# Sinon les chiffres ne sont pas dans l'ordre decroissant
			return False
		n = n//10
	
	return True

# commentaire : Très bien ! Le code est clair et documenté. Le choix des noms de variables est pertinent.
# La solution proposée est conforme aux attentes.


# Exercice 2

# Explication :
#	Dans un premier temps, il faut s'assurer que le nombre entre est superieur ou egal a 0
#	Puis pour determiner les espaces on utilise la formule nbre_espace(i) = 2i-1 pour i la distance au centre
#	Enfin il faut tout afficher en prenant soin de mettre les espaces avant la premiere croix avec le formule nbre_espace_avant(i) = n-i avec n la hauteur totale et i l'etage ou nous sommes

#	On peut simplifier ces formules en utilisant la relation : nbre_espace(i+1) = nbre_espace(i)+2 et nbre_espace_avant(i+1) = nbre_espace_avant(i)-1 (pour la descente, inverser + et - pour la remontee)

class negativeNumber(Exception):
	pass

def cross_layer(nbre_espace, nbre_espaces_avant):
	i = 0
	while i < nbre_espaces_avant:
		i = i+1
		print(' ', end = '')

	print('*',end='')

	i = 0
	while i < nbre_espace :
		i = i+1
		print(' ', end='')

	print('*')


def cross(n):
	if n<0:
		raise negativeNumber(n)

	nbre_espace = 2*n-1
	nbre_espace_avant = 0

	# Descente
	while nbre_espace_avant < n:
		cross_layer(nbre_espace, nbre_espace_avant)
		nbre_espace = nbre_espace-2
		nbre_espace_avant = nbre_espace_avant+1
	
	# Cas du milieu
	i = 0
	while i<n:
		print(' ', end='')
		i = i+1
	print('*',)	
	
	# Remontee
	while nbre_espace_avant > 0:
		nbre_espace = nbre_espace+2
		nbre_espace_avant = nbre_espace_avant-1
		cross_layer(nbre_espace, nbre_espace_avant)
		
# commentaire: Très bien ! Code clair, bien commenté, avec des variables nommées avec justesse !


# Exercice 3:

# Explications:
# 	Entree : tableau
#	Sortie : booleen

#	La ligne finale 'END' permet de determiner la fin de la boucle tant que
#	Il sera necessaire de faire un compteur pour avoir le nombre de zones pleines

#	A chaque iteration de la boucle, on compare la ligne i avec la ligne i-1
#	Il faut bien prendre en compte que les lignes ne sont pas toujours de longueur egale


# Compare les longueurs et indique si la premiere ligne est la plus longue
def comparer_longueur(longueur1, longueur2):
	if longueur1 > longueur2:
		longueur_min = longueur2
		ligne1_plus_longue = True
	else:
		longueur_min = longueur1
		ligne1_plus_longue = False

	return longueur_min, ligne1_plus_longue




def good_histo(nom_fichier):
	fichier = open(nom_fichier, 'r')
	
# regarde le nombre de zones pleines annoncees et cree le compteur
	nbre_zones_pleines_annonce = int( fichier.readline() )
	nbre_zones_pleines_effectif = 0

# tant que le contenu de la ligne est different de 'END', fait les calculs
	ligne_avant = fichier.readline()
	long_ligne_avant = len(ligne_avant)
# Ne pas oublier la premiere ligne (sinon il peut manquer des etoiles dans le traitement)
	prim_ligne = True

	ligne = fichier.readline()
	while ligne.split() != ['END']:

# regarde si le contenu de la ligne est coherent avec celui de la ligne avant
	# determine la longueur minimale pour eviter de depasser les tableaux
		long_ligne = len(ligne)
		longueur_min, l1_plus_long = comparer_longueur(long_ligne_avant, long_ligne)

	# compare les deux tableaux
		count = 0
		while count < longueur_min:
			if ligne_avant[count] == '*':
				if prim_ligne:
					nbre_zones_pleines_effectif = nbre_zones_pleines_effectif + 1
					prim_ligne = False
				if ligne[count] != '*':
					return False
			if ligne[count] == '*':
				nbre_zones_pleines_effectif = nbre_zones_pleines_effectif+1
			count = count+1

	# Si l'ancienne ligne est la plus longue, verifie qu'il n'y avait pas d'incoherence
		if l1_plus_long:
			while count < long_ligne_avant:
				if ligne_avant[count] == '*':
					return False
				count = count+1
	# Sinon, il ne faut pas oublier les etoiles de la nouvelle ligne
		else:
			while count < long_ligne:
				if ligne[count] == '*':
					nbre_zones_pleines_effectif = nbre_zones_pleines_effectif + 1
				count = count + 1
	
	# Tous les tests sont effectues, on reitere la boucle
		ligne_avant = ligne
		long_ligne_avant = long_ligne
		
		ligne = fichier.readline()
		
	fichier.close()

# Enfin, on verifie s'il y a autant de zones pleines annoncees qu'en realite
	return nbre_zones_pleines_effectif == nbre_zones_pleines_annonce

# commentaire: La solution proposée n'est pas juste, mais de peu. Son problème vient du traitement particulier qui est fait de la première ligne après la déclaration du nombre d'étoiles.
# A cause de cette particularité non nécessaire et qui complexifie l'entièreté du code, le programme ne termine pas sur certain exemple (en particulier h6.txt qui est un histogramme valide ne 
# contenant aucune étoile) et en classifie un autre de travers.
# Les open et close ne sont pas bons non plus. Dans l'open, vous avez oublié de spécifier comment vous vouliez ouvrir le fichier (en lecture ou en écriture), ce qui revient à utiliser le réglage 
# par défaut de Python. Le close quant à lui n'est pas présent.


# Exercice 4:

# Explication :
#	Par hypothese, on a l'ordre croissant strict et des entiers naturels, donc on n'a pas besoin de verifier cela
#	Entree : tableau
#	Sortie : valeur booleenne : True ou False
#
#	Il y a croissance stricte donc si a un seul indice T[i] > i, alors aucun point fixe n'est possible
#	En effet, T[i+1] >= T[i]+1, donc si il existe i tel que T[i]>i, alors pour tout j>i, T[j]>=T[i] + j-i > i + j-1 = j

#	Ainsi, l'algorithme est rapide : si en T[0] on n'a pas 0, alors il n'y aura aucun point fixe (car tous les elements du tableau sont positifs)
#	Sinon, il y a un point fixe : 0

def fixpt(tableau):
	return tableau[0]==0

# commentaire: Vous avez oublié de vérifier que le tableau n'est pas vide avant de faire un accès sur sa première case, ce qui peut amener votre solution à planter. Sinon le raisonnement est le bon !
