#! usr/bin/env python

import os

fileName = raw_input("What file should I destroy?")

print("WARNING: This will destroy all data in {}".format(fileName))

while True:
	configuration = raw_input("Are you sure to continue?")
	
	if configuration.lower() == "yes":
		os.remove(fileName)
		print("{} has been destroyed.".format(fileName))
		quit()
		
	elif configuration.lower() == "no":
		print("Operation canceled.")
		quit()
	
	else:
		print("You should type 'yes' or 'no'.")