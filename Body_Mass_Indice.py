#Author: red_Ant
#Location: Buja-Burundi
# Menya ubuzima bwawe uko bwifashe bivanye nibiro ufise n'uburebure.

import os
from os import sys

class fg:
	orange     = '\033[33m'
	blue       = '\033[34m'
	purple     = '\033[35m'
	lightgreen = '\033[92m'
	yellow     = '\033[93m'
	pink       = '\033[95m'
	lightcyan  = '\033[96m'

Maigreur 		= fg.blue + "Underweight"
mai = fg.pink + "<18.5>"
Normal 		    = fg.lightcyan + "Normal"
norm = fg.pink + "<24.9>"
surpoids 		= fg.yellow + "Overweight"
surp = fg.pink + "<29.9>"
obese 		= fg.orange + "Obese"
obesi = fg.pink + "<40>"
Obese_morbide = fg.purple + "Extremly Obese"
 


os.system('clear')


print(fg.pink + "\n\t\t  =========== Body Mass Index ==========\n")
print(fg.lightcyan + "\n\t\t\t    Hit 'Enter' to quit.")

print()
print("\t{} {} {} {} {} {} {} {} {}".format(Maigreur, mai, Normal, norm, surpoids, surp, obese, obesi, Obese_morbide))
print()


def calcul():
	
	request_weight = input(fg.lightgreen + "Body mass  (in kg)     = ")
	if request_weight == '':
		print("\n\t\t\t    Coded by red_Ant.")
		print()
		sys.exit()
	request_length = input(fg.lightgreen + "Height     (en meter)  = ")
	if request_length == '':
		print("\n\t\t\t    Coded by red_Ant.")
		print()
		sys.exit()
	
	try:
		calcule = float(request_weight) / (float(request_length) * float(request_length))
		
		print("\nBMI: {}\n".format(calcule))
		
		# ====================================
		if calcule <= 18.5:
			print(fg.blue + "Underweight".title())
		elif calcule <= 24.9:
			print(fg.lightcyan + "normal".title())
		elif calcule <= 29.9:
			print(fg.yellow + "Overweight".title())
		elif calcule <= 40:
			print(fg.orange + "Obese".title())
		elif calcule > 40:
			print(fg.purple + "Extremly Obese".title())
	except ValueError:
		print("\n*** Error! Only numbers. ***")
	# ===================================
while True:
	
	calcul()
	print()
