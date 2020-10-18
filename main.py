#%% VALEUR PAR DEFAUT ######################################################################

import numpy as np 
#import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

numpion_ia = 1
numpion_joueur = 2

nbColonnes = 12
nbLignes = 6

#%% FONCTIONS ######################################################################

# affiche la grille d'entier avec les pions correspondant. (dans notre code,  0 equivaut à une case vide, 1 au joueur 1, 2 au joueur 2)
def affichage(t):
	
	for j in range(nbColonnes):
		print(" ({})".format(j+1), end='')
	print(" \n");
	
	for i in range(nbLignes):
		for j in range(nbColonnes):
			print("+---", end='')
		print("+\n")
		for j in range(nbColonnes):
			if t[i][j] == 1:
				print("| O ", end=''),
			elif t[i][j] == 2:
				print("| X ", end=''),
			else:
				print("| . ", end=''),
		print("|\n")
	for j in range(nbColonnes):
		print("+---", end='')
	print("+\n")

#jouer() permet à un joueur de poser son pion (avec t la grille, num_j le numéro du joueur et c la numéro de la colonne)
def jouer(t,num_j,c):
	
	ok = 1 #booléen qui vaut 1 si il ny a pas de probleme
	if((c > nbColonnes-1) or (c < 0) or (c == '')):
		ok = 0
		print(" ! Celle colonne existe pas..")
	else:	
		i = 0
		
		#on fait glisser le pion
		if((t[i][c] == 0) and (ok == 1)):
			while ((t[i][c] == 0) and (i < nbLignes-1)):
				i += 1
			
			if not(t[i][c] == 0):
				i -= 1
			t[i][c] = num_j 
			
		else:
			ok = 0
			print(" ! Cette colonne est rempli..")
	return ok # si ok vaut 0 alors on demandera plutard au jouer de resaisir une colonne


# aGagne() : permet de verifier si dans la grille un joueur a aligner 4 pion et renvoie le numero du joueur, avec t la grille
def aGagne(t):
	int_gagnant = 0 # on suppose au debut que la match est nul
	
	# scan de ligne
	for i in range(nbLignes):
		for k in range(3,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i][k-1] and x == t[i][k-2] and x == t[i][k-3]):
				int_gagnant = x
	
	# scan de colonnes
	for i in range(nbColonnes):
		for k in range(3,nbLignes):
			x = t[k][i]
			if (x != 0 and x == t[k-1][i] and x == t[k-2][i] and x == t[k-3][i]):
				int_gagnant = x
                
      # scan sur les diagonales 1 (/)
	for i in range(nbLignes):
		for k in range(3,nbColonnes):
			x = t[i][k-3]
			if (x != 0 and x == t[i-1][k-2] and x == t[i-2][k-1] and x == t[i-3][k]):
				int_gagnant = x          
    
    # scan sur les diagonales 2 (\)
	for i in range(nbLignes):
		for k in range(3,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i-1][k-1] and x == t[i-2][k-2] and x == t[i-3][k-3]):
				int_gagnant = x
                
				
	#scan pour verifier si il reste des cases vide (et donc il ce n'est pas un match nul mais un jeu ene cours')			
	for i in range(nbLignes):
		for k in range(nbColonnes):
			if (t[i][k] == 0 and int_gagnant != 1 and int_gagnant != 2):
				int_gagnant = -1
	
	return int_gagnant # -1 : jeu en cours / 0 : match nul / 1 : joueur 1 gagne / 2 : joueur 2 gagne

# align3() : de même que aGagne mais pour 6 pion (cette fonction est utile à l'IA') 	
def align3(t):
	int_gagnant = 0
	
	# scan de ligne
	for i in range(nbLignes):
		for k in range(2,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i][k-1] and x == t[i][k-2] ):
				int_gagnant = x
	
	# scan de colonnes
	for i in range(nbColonnes):
		for k in range(2,nbLignes):
			x = t[k][i]
			if (x != 0 and x == t[k-1][i] and x == t[k-2][i] ):
				int_gagnant = x
                
      # scan sur les diagonales 1 (/)
	for i in range(nbLignes):
		for k in range(2,nbColonnes):
			x = t[i][k-2]
			if (x != 0 and x == t[i-1][k-1] and x == t[i-2][k]):
				int_gagnant = x          
    
    # scan sur les diagonales 2 (\)
	for i in range(nbLignes):
		for k in range(2,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i-1][k-1] and x == t[i-2][k-2] ):
				int_gagnant = x

	for i in range(nbLignes):
		for k in range(nbColonnes):
			if (t[i][k] == 0 and int_gagnant != 1 and int_gagnant != 2):
				int_gagnant = -1
	
	return int_gagnant
	
def align2(t):
	int_gagnant = 0
	
	# scan de ligne
	for i in range(nbLignes):
		for k in range(1,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i][k-1]):
				int_gagnant = x
	
	# scan de colonnes
	for i in range(nbColonnes):
		for k in range(1,nbLignes):
			x = t[k][i]
			if (x != 0 and x == t[k-1][i]):
				int_gagnant = x
                
      # scan sur les diagonales 1 (/)
	for i in range(nbLignes):
		for k in range(1,nbColonnes):
			x = t[i][k-1]
			if (x != 0 and x == t[i-1][k]):
				int_gagnant = x          
    
    # scan sur les diagonales 2 (\)
	for i in range(nbLignes):
		for k in range(1,nbColonnes):
			x = t[i][k]
			if (x != 0 and x == t[i-1][k-1]):
				int_gagnant = x

	for i in range(nbLignes):
		for k in range(nbColonnes):
			if (t[i][k] == 0 and int_gagnant != 1 and int_gagnant != 2):
				int_gagnant = -1
	
	return int_gagnant

#%%  IA  ######################################################################
def Terminal_Test(t): #return (findujeu,gagnant)
	a = aGagne(t)
	# pas de gagnant et colonne restante
	if a == 1:
		return True,1 #match fini, joueur 1 gagnant
	elif a == 2:
		return True,2
	elif a == 0:
		return True,0 #match fini, match nul
	else:
		return False,-1 #match pas fini, match en cours
		
def Utility(t): #return (la recompense)
	val = 0
	game_over,win=Terminal_Test(t)

	# si le jeu est fini (4 alignement) alors
	if game_over:
		if win == numpion_ia:
			val += 110
		elif win == numpion_joueur:
			val += -100
		else:
			val = 0
			
	else:
		#si le jeu est pas fini et 3 alignement alors 
		win = align3(t)
		if win == numpion_ia:
			val += 30
		elif win == numpion_joueur:
			val += -25
		else:
			#si personne na aligné 3 le jeu est pas fini et 2 alignement alors 
			win = align2(t)
			if win == numpion_ia:
				val += 8
			elif win == numpion_joueur:
				val += -5
			
		
		#si le jeu est pas fini et 2 alignement alors 
	
	return val

def Actions(t): #return (liste des colonnes jouable)       
	actions=[]          
	if Terminal_Test(t)[0] == False: #si le jeu n'est pas fini
		for j in range(nbColonnes):
			if (t[0][j]==0):
				actions.append(j+1) 
		return actions     

# (semblable à Actions() mais utile à l'IA)
def CoordonneesActions(t): 
	actions=[]        
	if Terminal_Test(t)[0] == False: #si le jeu n'est pas fini
		for j in range(nbColonnes):
			if (t[0][j]==0):
				(x,y) = Tomber(1,t,j)
				t[x][y] = 0
				actions.append((x,y))
				
		return actions 

# Tomber() : (semblable à jouer() mais utile à l'IA) avec c la colonne voulu
def Tomber(numjoueur,t,c): #Pose le pion
	i = 0
	#print("*tomber* TERMINAL  : ", Terminal_Test(t))	
	if Terminal_Test(t)[0] != True:
		while ((t[i][c] == 0) and (i < nbLignes-1)):
			i += 1
			#print("**t[{}][{}] : {} // {} {}".format(i,c,t[i][c],(t[i][c] == 0),(i < 5)))
				
		if not(t[i][c] == 0):
			i -= 1
		
		if t[i][c] == 0:
			t[i][c] = numjoueur
		else:
			print(" ERREUR Tomber()")
	return (i,c) #return les coordonnée du pion posé

def min_max_value4_AB(t,prof,MAXI,alpha,beta):
	
	if Terminal_Test(t)[0] or prof > 3:
		#affichage(t)
		#print(" PROF {} // TERMINAL-TEST {} // UTILITY {} *---------------------------------*".format(prof,Terminal_Test(t)[0],Utility(t)))
		return Utility(t)
	
	if MAXI:
		meilleurscoremgl = -100000
		actionspossible = CoordonneesActions(t) 

		for (i,j) in actionspossible: #pour toute les actions possible
			t[i][j] = numpion_ia #faire tomber le pion			
			
			scoreee = min_max_value4_AB(t,prof+1,False,alpha,beta) #recursion
			#print("MAXI SCORE {} // PROF {} // ALPHA BETA {} {} **".format(scoreee ,prof+1,alpha,beta)) # affichage des infomartion (faire ça nous a donné un meilleur vision de notre code et nous a aidé au debbug)
			
			t[i][j] = 0 #remise à l'état
			meilleurscoremgl = max([scoreee,meilleurscoremgl]) # le MAX veut maximiser sa 'recompense' donc il cherche le meilleur coup
			if meilleurscoremgl >= beta:
				return meilleurscoremgl
			
			alpha = max([alpha,meilleurscoremgl])
			if alpha >= beta:
				print("*")
				break
		return meilleurscoremgl
	
	else:
		meilleurscoremgl = 100000
		actionspossible = CoordonneesActions(t)
		for (i,j) in actionspossible:
			t[i][j] = numpion_joueur #faire tomber
			
			scoreee = min_max_value4_AB(t,prof+1,True,alpha,beta) #recursion
			#print("MINI SCORE {} // PROF {} // ALPHA BETA {} {} **".format(scoreee ,prof+1,alpha,beta))
			
			t[i][j] = 0 #reset
			meilleurscoremgl = min(scoreee,meilleurscoremgl)
			if meilleurscoremgl <= alpha:
				return meilleurscoremgl
			beta = min([beta,meilleurscoremgl])
			
			if alpha >= beta:
				break
		return meilleurscoremgl
	
		
 
def MiniMax_Decision4_AB(t):
	global currentplayer
	meilleurscoremgl = -100000
	
	actionspossible = CoordonneesActions(t)
		
	for (i,j) in actionspossible: #On va voir quel et la meilleur colonne à choisir, en donnant un score à chaque colonne. On choisira celle le meilleur score
		#si la colonne n'est pas rempli
		t[i][j] = numpion_ia
		# alors on pose puis on minmax
		score = min_max_value4_AB(t,0,False,-1000,1000)
		t[i][j] = 0
		
		if score > meilleurscoremgl:
			meilleurscoremgl = score
			decision = (i,j)
	t[decision[0]][decision[1]]=numpion_ia
	print("l'IA a joué sur la colonne",decision[1]+1)
	return t

######################################################################################################

#t0 = np.zeros((nbLignes,nbColonnes))

#affichage(t0)
#print(align2(t0))
#t0 = MiniMax_Decision4(t0)

#a = min_max_value4(t0,0,False)
quijoueenpremier = 1
encore = 'y'
while encore == 'y':
	tour = 0 #nombre de tour, il incremente et permet de changer de joueur
	winner = -1 # numero du joueur gagnant
	modevs = 2 
	game_over = False
	
	print("///////////////////////////////")
	print("///////////////////////////////")
	print("/////// * PUISSANCE 4 * ///////")
	print("///////////////////////////////")
	print("////// JOUEUR 1 : 'O'  ////////")
	print("//////// JOUEUR 2 : 'X'  //////")
	print("///////////////////////////////")
	print("/////  1 - Parametre   ////////")
	print("///  2 - JOUER    /////////////")
	print("///////////////////////////////")
	print("///////////////////////////////")
	
	# Petit Menu
	choix = 0
	while choix < 1 or choix > 2:
	    choix = int(input("> "))
	    
	if choix == 1:
		print("///////////////////////////////")
		print("//// Qui joue en premier ? ///")
		print("( 1 : L'iA')         (2 : VOUS) ")
		quijoueenpremier = 0
		while quijoueenpremier < 1 or quijoueenpremier > 2:
			quijoueenpremier = int(input("> "))
		
	else:
		#Initialisation de la grille
		tab = np.zeros((nbLignes,nbColonnes)) 
		
		# Lancement de la partie qui ne s'arretera pas tant que le jeu sera en cours (tantquil nya pas de gagnant ni match nul)
		while (winner == -1):
			
			#jour actuel
			if quijoueenpremier == 1:
				currentplayer = 1 + (tour % 2)
			else:
				currentplayer = 2 - (tour % 2)
				
			
			#symboles des joueurs
			if currentplayer == 1:
				symbole = 'O'
			else:
				symbole = 'X'
			
			# A chaque tour, avant de demander au joueur suivant de jouer, on teste la grille pour savoir si il ya un gagnant ou un match nul
			game_over,winner = Terminal_Test(tab)
			
			if (currentplayer == 2)and not(game_over): 
				affichage(tab)
			
				print(" * ACTIONS : ", Actions(tab))
				
				#demande saisie de colonne
				ok = 0
				while (ok == 0):
					print(" * {}-JOUEUR {:d} : ".format(symbole,int(currentplayer)))
					c = int(input("> "))
					ok = jouer(tab,currentplayer,c-1)

				tour += 1 #on passe au tour de lautre joueur
				
			elif (currentplayer == 1)and not(game_over):
				print("l'IA joue...")
				tab=MiniMax_Decision4_AB(tab)
				tour += 1
				#affichage(tab)
				#print("*** {}-JOUEUR {:d} : ".format(symbole,int(currentplayer)))
				
		if winner != 0 or game_over: #si le match est fini et qu'il nya pas de match nul (donc il ya un gagnant)'
			affichage(tab)
			print("\n JOUEUR {:d} GAGNE LA PARTIE : ".format(winner))
			
		else:
			print("\n MATCH NUL")
				
		print("\n\n///// RECOMMENCER UNE PARTIE ? (y/n) ")
		encore = input("> ")
	
	
	

			
			
