#! usr/bin/env python

import os
import specialInput

fileName = raw_input("What file should I destroy?")

while True:
	time = specialInput.int_input("How many times should I overwrite it?")
	
	if time > 26:
		print("The time should be less than 26.")
	else:
		break 
		
print("WARNING: This will destroy all data in {}".format(fileName))

while True:
	configuration = raw_input("Are you sure to continue?")
	
	if configuration.lower() == "yes":
		f = open(fileName, "r+")
		
		currentTime = 0
		while currentTime < time:
			f.write(chr(65 + currentTime)*len(f.read()))
			print("Overwriting the file with {}.".format(chr(65 + currentTime)))
			currentTime += 1
			
		os.remove(fileName)
		print("{} has been destroyed.".format(fileName))
		
		quit()
		
	elif configuration.lower() == "no":
		print("Operation canceled.")
		
		quit()
	
	else:
		print("You should type 'yes' or 'no'.")