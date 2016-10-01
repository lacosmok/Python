#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import exit
import random
import time

import pygame
from pygame.locals import *

SCREEN_SIZE = (900, 700)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

class Smiec():
	#wczytanie obrazków do zmiennych, ustawienie pozycji
    def __init__(self, x_coord, y_coord, zmienna, material, charakter, zuzycie):
        self.x = x_coord
        self.y = y_coord
        self.image = pygame.image.load('trash2.png')
	self.image2 = pygame.image.load('trash3.png')
	self.zm = zmienna
	self.m = material
	self.zu = zuzycie
	self.ch = charakter
	self.odp = 0
        return
	#wczytywanie odpowiedniej grafiki do gry
    def update(self, surface):
	if (self.zm == 1):
	     surface.blit(self.image, (self.x, self.y))
	else:
	     surface.blit(self.image2, (self.x, self.y))
        return

#kolizje (zebrany smiec)
def check_collision(object1_x, object1_y, object2_x, object2_y):
    if ((object1_x + 25 > object2_x) and (object1_x + 25 < object2_x + 35) and 
        (object1_y + 25 > object2_y) and (object1_y + 25 < object2_y + 35)
    ):
        return True
    if ((object1_x > object2_x) and (object1_x < object2_x + 35) and 
        (object1_y > object2_y) and (object1_y < object2_y + 35)
    ):
        return True
    if ((object1_x + 50 > object2_x) and (object1_x + 50 < object2_x + 35) and 
        (object1_y + 50 > object2_y) and (object1_y + 50 < object2_y + 35)
    ):
        return True
    return False

#sprawdza czy dany obiekt jest do zabrania
tablica = []
drzewo = {
           'True':{'gdzie': 1},
           'False':{ 
			   'True':{
				     'True':{'gdzie': 2},
					 'False':{'gdzie': 2}}, 
		       'False':{
				     'gdzie':3}}}
drzewo2 = {
           'True':{'gdzie': 1},
           'False':{ 
			   'True':{
				     'True':{'gdzie': 2},
					 'False':{'gdzie': 2}}, 
		       'False':{
				     'gdzie':3}}}					 
def dodajSlownik(kl,war,kl2 = 'inny', war2 = 0,d=drzewo):
	
    if kl == 'True' or kl == 'False':
	     tablica.append(kl)	 
    if len(tablica) == 0:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo[kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo[kl] = war
	         drzewo[kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo[kl] = war
	         drzewo[kl2] = war2
    if len(tablica) == 1:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo[tablica[0]][kl]=war			 
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo[tablica[0]][kl] = war
	         drzewo[tablica[0]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo[tablica[0]][kl] = war
	         drzewo[tablica[0]][kl2] = war2
    if len(tablica) == 2:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo[tablica[0]][tablica[1]][kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo[tablica[0]][tablica[1]][kl] = war
	         drzewo[tablica[0]][tablica[1]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo[tablica[0]][tablica[1]][kl] = war
	         drzewo[tablica[0]][tablica[1]][kl2] = war2
    if len(tablica) == 3:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo[tablica[0]][tablica[1]][tablica[2]][kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo[tablica[0]][tablica[1]][tablica[2]][kl] = war
	         drzewo[tablica[0]][tablica[1]][tablica[2]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo[tablica[0]][tablica[1]][tablica[2]][kl] = war
	         drzewo[tablica[0]][tablica[1]][tablica[2]][kl2] = war2
    if ((kl == 'tak' or kl == 'nie') and tablica[len(tablica)-1] == "True") or ((kl == 'tak' or kl == 'nie') and (tablica[len(tablica)-1] == "False") and (len(tablica) == 1)):
         tablica.pop()
    elif (kl == 'tak' or kl == 'nie') and (tablica[len(tablica)-1] == "False") and (len(tablica) > 1):
	     tablica.pop()
	     tablica.pop()
   #print tablica
def dodajSlownik2(kl,war,kl2 = 'inny', war2 = 0,d=drzewo2):
	
    if kl == 'True' or kl == 'False':
	     tablica.append(kl)	 
    if len(tablica) == 0:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo2[kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo2[kl] = war
	         drzewo2[kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo2[kl] = war
	         drzewo2[kl2] = war2
    if len(tablica) == 1:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo2[tablica[0]][kl]=war			 
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo2[tablica[0]][kl] = war
	         drzewo2[tablica[0]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo2[tablica[0]][kl] = war
	         drzewo2[tablica[0]][kl2] = war2
    if len(tablica) == 2:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo2[tablica[0]][tablica[1]][kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo2[tablica[0]][tablica[1]][kl] = war
	         drzewo2[tablica[0]][tablica[1]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo2[tablica[0]][tablica[1]][kl] = war
	         drzewo2[tablica[0]][tablica[1]][kl2] = war2
    if len(tablica) == 3:
	     
       if 'Column' in kl:  #gdy mamy jakąś wartość dalszą. 
	         drzewo2[tablica[0]][tablica[1]][tablica[2]][kl]=war
       if kl == 'tak':   # gdy kończymy
	         kl2 = 'nie'
	         drzewo2[tablica[0]][tablica[1]][tablica[2]][kl] = war
	         drzewo2[tablica[0]][tablica[1]][tablica[2]][kl2] = war2
       if kl == 'nie':
	         kl2 = 'tak'
	         drzewo2[tablica[0]][tablica[1]][tablica[2]][kl] = war
	         drzewo2[tablica[0]][tablica[1]][tablica[2]][kl2] = war2
    if ((kl == 'tak' or kl == 'nie') and tablica[len(tablica)-1] == "True") or ((kl == 'tak' or kl == 'nie') and (tablica[len(tablica)-1] == "False") and (len(tablica) == 1)):
         tablica.pop()
    elif (kl == 'tak' or kl == 'nie') and (tablica[len(tablica)-1] == "False") and (len(tablica) > 1):
	     tablica.pop()
	     tablica.pop()
   #print tablica

my_data2=[['jednorazowe', 'szklo', 'duze','tak'],
        ['jednorazowe', 'plastik', 'male','tak'],
		['wielorazowe', 'szklo', 'duze','tak'],
		['wielorazowe', 'szklo', 'male','nie'],
		['wielorazowe', 'szklo', 'duze','tak'],
		['wielorazowe', 'plastik', 'duze','nie'],
		['wielorazowe', 'plastik', 'duze','nie'],
		['wielorazowe', 'plastik', 'male','nie']]
list = [['srednia', 'duza', 'srednia', 'tak'],
    ['duza', 'mala', 'duza', 'nie'],
    ['duza', 'srednia', 'duza', 'nie'],
    ['mala', 'srednia', 'mala', 'tak'],
    ['mala', 'duza', 'mala', 'tak'],
    ['duza', 'mala', 'mala', 'nie'],
    ['duza', 'mala', 'mala', 'nie'],
    ['duza', 'duza', 'mala', 'tak'],
    ['mala', 'srednia', 'duza', 'tak'],
    ['mala', 'srednia', 'srednia', 'nie'],
    ['srednia', 'srednia', 'srednia', 'nie'],
    ['srednia', 'duza', 'mala', 'tak'],
    ['srednia', 'mala', 'mala', 'nie'],
    ['srednia', 'duza', 'duza', 'tak'],
    ['srednia', 'duza', 'srednia', 'tak']]

		
'''clf = linear_model.SGDRegressor() # Instantiating SGDRegressor as clf 
clf.fit(X, y) # using clf's (an instance of SGDRegressor) fit method on some data
'''
class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col # column index of criteria being tested
        self.value=value # vlaue necessary to get a true result
        self.results=results # dict of results for a branch, None for everything except endpoints
        self.tb=tb # true decision nodes 
        self.fb=fb # false decision nodes
# Divides a set on a specific column. Can handle numeric or nominal values

def divideset(rows,column,value):
    # Make a function that tells us if a row is in the first group 
    # (true) or the second group (false)
    split_function=None
    # for numerical values
    if isinstance(value,int) or isinstance(value,float):
        split_function=lambda row:row[column]>=value
    # for nominal values
    else:
        split_function=lambda row:row[column]==value
   
   # Divide the rows into two sets and return them
    set1=[row for row in rows if split_function(row)] # if split_function(row) 
    set2=[row for row in rows if not split_function(row)]
    return (set1,set2)
	
'''print divideset(my_data2,1,'USA')'''

# Create counts of possible results (last column of each row is the result)
def uniquecounts(rows):
    results={}
    for row in rows:
        # The result is the last column
        r=row[len(row)-1]
        if r not in results: results[r]=0
        results[r]+=1
    return results

from collections import defaultdict
def uniquecounts_dd(rows):
    results = defaultdict(lambda: 0)
    for row in rows:
        r = row[len(row)-1]
        results[r]+=1
    return dict(results)

#print uniquecounts(my_data2),'Same output', uniquecounts_dd(my_data2)	


def entropy(rows):
    from math import log
    log2=lambda x:log(x)/log(2)  
    results=uniquecounts(rows)
    # Now calculate the entropy
    ent=0.0
    for r in results.keys():
        # current probability of class
        p=float(results[r])/len(rows) 
        ent=ent-p*log2(p)
    return ent
	
def buildtree(rows, scorefun=entropy):
    if len(rows) == 0: return decisionnode()
    current_score = scorefun(rows)

    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1	# last column is result
    for col in range(0, column_count):
        # find different values in this column
        column_values = set([row[col] for row in rows])

        # for each possible value, try to divide on that value
        for value in column_values:
            set1, set2 = divideset(rows, col, value)

            # Information gain
            p = float(len(set1)) / len(rows)
            gain = current_score - p*scorefun(set1) - (1-p)*scorefun(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)

    if best_gain > 0:
        trueBranch = buildtree(best_sets[0])
        falseBranch = buildtree(best_sets[1])
        return decisionnode(col=best_criteria[0], value=best_criteria[1],
                tb=trueBranch, fb=falseBranch)
    else:
        return decisionnode(results=uniquecounts(rows))
 

#print divideset(my_data2,3,'tak')

def printtree(tree,indent=''):
   
	# Is this a leaf node?
	
    if tree.results!=None:
	    cos = str(tree.results)
	    if len(cos) > 10:
	      print cos
	      dodajSlownik(cos[2:5], int(cos[8]), cos[12:15], int(cos[18]))		 
	    else:
		  print cos
		  dodajSlownik(cos[2:5], int(cos[8]))
	     
    else:
        # Print the criteria
        print 'Column ' + str(tree.col)+' : '+str(tree.value)+'? '
        dodajSlownik('Column', str(tree.value))
        # Print the branches
        print indent+'True->',
        dodajSlownik('True', 'nic')
        printtree(tree.tb,indent+'  ')
        print indent+'False->',
        dodajSlownik('False','nic')
        printtree(tree.fb,indent+'  ') 

def printtree2(tree,indent=''):
   
	# Is this a leaf node?
	
    if tree.results!=None:
	    cos = str(tree.results)
	    if len(cos) > 10:
	      print cos
	      dodajSlownik2(cos[2:5], int(cos[8]), cos[12:15], int(cos[18]))		 
	    else:
		  print cos
		  dodajSlownik2(cos[2:5], int(cos[8]))
	     
    else:
        # Print the criteria
        print 'Column ' + str(tree.col)+' : '+str(tree.value)+'? '
        dodajSlownik2('Column', str(tree.value))
        # Print the branches
        print indent+'True->',
        dodajSlownik2('True', 'nic')
        printtree2(tree.tb,indent+'  ')
        print indent+'False->',
        dodajSlownik2('False','nic')
        printtree2(tree.fb,indent+'  ') 		
		

		
str(printtree(buildtree(my_data2)))
str(printtree2(buildtree(list)))
#print drzewo1
#drzewo1 = str(printtree(buildtree(list)))
#print drzewo

#print str(drzewo['Column'])
def sprawdz(object_ch, object_m, object_zu):
	if (object_ch or object_m or object_zu) == drzewo['Column']: #gdy się zgadza to idziemy do true. Jednorazowe
	     if 'tak' in drzewo['True'].keys(): # tzn że to koniec
		     if drzewo['True']['tak'] > drzewo['True']['nie']:
				 #print 'Tak! jednorazowe'
				 return True
	     else:
		     if (object_ch or object_m or object_zu) == drzewo['True']['Column']:
			    if 'tak' in drzewo['True']['True'].keys(): # tzn że to koniec
		             if drzewo['True']['True']['tak'] > drzewo['True']['True']['nie']:
			             #print 'Tak!'
						 return True				 
	else:
	     if 'tak' in drzewo['False'].keys(): # tzn że to koniec
		     if drzewo['False']['tak'] > drzewo['False']['nie']:
			     #print 'Tak wielorazowe!'
				 return True
	     else:
		    if object_m == drzewo['False']['Column']:  # czy szklo?
			    if 'tak' in drzewo['False']['True'].keys(): # tzn że to koniec
		             if drzewo['False']['True']['tak'] > drzewo['False']['True']['nie']:
			             #print 'Tak! wielorazowe, duze'
						 return True
			    else:
				    if(object_zu) == drzewo['False']['True']['Column']: #czy zuzycie
				         if 'tak' in drzewo['False']['True']['True'].keys(): # tzn że to koniec
						     if drzewo['False']['True']['True']['tak'] > drzewo['False']['True']['True']['nie']:
							     #print 'tak wielorazowe, duze , szklo'
								 return True
				    else:
					     if 'tak' in drzewo['False']['True']['False'].keys():
						     if drzewo['False']['True']['False']['tak'] > drzewo['False']['True']['False']['nie']:
							     #print 'wielorazowe, duze , nie szklo'
								 return True
		    else: 
	             if 'tak' in drzewo['False']['False'].keys(): # tzn że to koniec
		             if drzewo['False']['False']['tak'] > drzewo['False']['False']['nie']:
			             #print 'Tak! jol'
						 return True
	return False

def sprawdzDroge(object_ch, object_m, object_zu): #Toxic, time, way
	if (object_ch or object_m or object_zu) == drzewo2['Column']: #gdy się zgadza to idziemy do true. Jednorazowe
	     if 'tak' in drzewo2['True'].keys(): # tzn że to koniec
		     if drzewo2['True']['tak'] > drzewo2['True']['nie']:
				 #print 'Tak! jednorazowe'
				 return True
	     else:
		     if (object_ch or object_m or object_zu) == drzewo2['True']['Column']:
			    if 'tak' in drzewo2['True']['True'].keys(): # tzn że to koniec
		             if drzewo2['True']['True']['tak'] > drzewo2['True']['True']['nie']:
			             #print 'Tak!'
						 return True				 
	else:
	     if 'tak' in drzewo2['False'].keys(): # tzn że to koniec
		     if drzewo2['False']['tak'] > drzewo2['False']['nie']:
			     #print 'Tak wielorazowe!'
				 return True
	     else:
		    if object_m == drzewo2['False']['Column']:  # czy szklo?
			    if 'tak' in drzewo2['False']['True'].keys(): # tzn że to koniec
		             if drzewo2['False']['True']['tak'] > drzewo2['False']['True']['nie']:
			             #print 'Tak! wielorazowe, duze'
						 return True
			    else:
				    if(object_zu) == drzewo2['False']['True']['Column']: #czy zuzycie
				         if 'tak' in drzewo2['False']['True']['True'].keys(): # tzn że to koniec
						     if drzewo2['False']['True']['True']['tak'] > drzewo2['False']['True']['True']['nie']:
							     #print 'tak wielorazowe, duze , szklo'
								 return True
				    else:
					     if 'tak' in drzewo2['False']['True']['False'].keys():
						     if drzewo2['False']['True']['False']['tak'] > drzewo2['False']['True']['False']['nie']:
							     #print 'wielorazowe, duze , nie szklo'
								 return True
		    else: 
	             if 'tak' in drzewo2['False']['False'].keys(): # tzn że to koniec
		             if drzewo2['False']['False']['tak'] > drzewo2['False']['False']['nie']:
			             #print 'Tak! '
						 return True
	return False
#generowanie macierzy smieci (losowo zmienne - który obrazek, pozycja x i y)
def generate_trash():
    matrix = []
    for d in range(8):
	zu = random.randrange(2)
	ch = random.randrange(2)
	zm = random.randrange(2) 
        x = random.randrange(850)
        y = random.randrange(625)
        dodaj(x,y)
	if (ch == 1):
         charakter = "jednorazowe" 
        else:
             charakter = "wielorazowe"
	if (zu == 1):
         zuzycie = "duze"
         toxic = "duze"
         dodajWay("srednia", "duza", "mala")		 
        else:
             zuzycie = "male"
             toxic = "srednie"
             dodajWay("mala", "srednia", "duza")			 
	if (zm == 1):
		 material = "szklo"
	else:
		 material = "plastik"	 
        trashes = [Smiec(x, y, zm, material, charakter, zuzycie)]
        matrix.append(trashes)
		
    return matrix

tablicax = []
tablicay = []
tablicaWay = []
tablicaToxic = []
tablicaTime = []

def dodaj(x,y,):
    tablicax.append(x)
    tablicay.append(y)

def dodajWay(way, toxic, time):
    tablicaWay.append(way)
    tablicaToxic.append(toxic)
    tablicaTime.append(time)

class Smieciarka(object):
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode(SCREEN_SIZE, flag)
        self.surface.fill(BLACK)
        myfont = pygame.font.Font(None, 25)
	self.trash_matrix = generate_trash()
	self.score = 0
	self.score_dump = 0

        label = myfont.render(u"Naciśnij ENTER, aby zacząć", 1, YELLOW)
        self.surface.blit(label, (200, 100))
	self.draw_truck()
	self.draw_dump()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.gamestate = 1
                    self.loop()
                if (event.type == QUIT or 
                    (event.type == KEYDOWN and event.key == K_ESCAPE)
                ):
                    exit()

    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()

    def idz(self, i):
	    if len(tablicax) > 0:
	         x=tablicax[len(tablicax)-1]
	         y=tablicay[len(tablicax)-1]
	         odp = sprawdzDroge(tablicaToxic[len(tablicaToxic)-1], tablicaTime[len(tablicaTime)-1], tablicaWay[len(tablicaWay)-1])
	         time.sleep(1)
	         if odp == True:
	             self.move(x,y)
	         tablicax.pop()
	         tablicay.pop()
             			 
    def draw_truck(self):
        self.truck = pygame.image.load("truck2.png")
        self.speed = 1
        self.truck_x = SCREEN_SIZE[0]/2 - 25
        self.truck_y = SCREEN_SIZE[1] - 75

    def draw_dump(self):
	self.dump = pygame.image.load("recycle.png")
	self.dump_x = random.randrange(850)
	self.dump_y = random.randrange(625)

    def move(self, dirx, diry):
        self.truck_x = dirx
        self.truck_y = diry
    

    def loop(self):
        """ glowna petla gry """
        myfont = pygame.font.Font(None, 25)
	self.smiec = myfont.render(u"Co zebrane", 1, BLACK)
        count = 0
        while self.gamestate == 1:
            for event in pygame.event.get():
                if (event.type == QUIT or
                    (event.type == KEYDOWN and event.key == K_ESCAPE)
                ):
                    self.gamestate = 0

	    #obsluga klawiszy (ruch smieciarki)
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT] and self.truck_x < SCREEN_SIZE[0] - 50:
 				 self.idz(1)  

            if keys[K_LEFT] and self.truck_x > 0:
				 time.sleep(2)
				 self.move(-10, 20)
                 

            if keys[K_UP] and self.truck_y > 0:
		              self.move(0,-1)
			
            if keys[K_DOWN] and self.truck_y < SCREEN_SIZE[1] - 100:
                self.move(0, 1)
				

            self.surface.fill(WHITE) #wypelnienie bialym
            self.surface.blit(self.truck, (self.truck_x, self.truck_y)) #rysowanie smieciarki
            self.surface.blit(self.dump, (self.dump_x, self.dump_y))
	    #rysowanie macierzy smieci
            for trashes in self.trash_matrix:
                for trash in trashes:
                    trash.update(self.surface)

            #dodaj(self.dump_x, self.dump_y)
	    #kolizje
            for trashes in self.trash_matrix:
                for trash in trashes:
                    if (check_collision(self.truck_x, self.truck_y, trash.x, trash.y)) and (sprawdz(trash.ch, trash.m, trash.zu)):
					     trash.odp = 1
					     self.score += 1
					     self.score_dump += 1
					     print 'smiec'
					     trashes.remove(trash)
                '''if (trash.odp == 0):
				     self.smiec = myfont.render(u"nie Zbieram: " +u"Materiał "+ trash.m + u" Zużycie " + trash.zu , 1, BLACK)'''
                if (trash.odp == 1):
				     self.smiec = myfont.render(u"Zbieram: "+u"charakter : "+ trash.ch +u" Materiał : "+ trash.m + u" Zużycie : " + trash.zu , 1, BLACK)			
		if(check_collision(self.truck_x, self.truck_y, self.dump_x, self.dump_y)
                    ):
			self.score_dump = 0
            
	    if (self.score == 8):
		self.smiec = myfont.render(u"Zebrałeś wszystkie śmieci!", 1, BLACK)

	    '''
	    if (self.score == 8):
		while (self.truck_x != self.dump_x):
			if (self.truck_x > self.dump_x):
				self.move(-1, 0)
			elif (self.truck_x < self.dump_x): 
				self.move(1, 0)
		while (self.truck_y != self.dump_y):
			if (self.truck_y > self.dump_y):
				self.move(0, -1)
			elif (self.truck_y < self.dump_y): 
				self.move(0, 1)'''

	    self.surface.blit(self.smiec, (185, 75))

            score_label = myfont.render("Zebrane odpady: {}".format(self.score), 1, BLACK)
            self.surface.blit(score_label, (25, 675))

            score_label = myfont.render(u"Aktualna ilość odpadów w śmieciarce: {}".format(self.score_dump), 1, BLACK)
            self.surface.blit(score_label, (385, 675))

            pygame.display.flip()

	self.game_exit()

if __name__ == '__main__':
    Smieciarka()
