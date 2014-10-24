"""
	This is a module written by Adam.
	It is written for inputting numbers
	and other non-string data.
"""





def int_input(prompt):
	"""
		Allows the user to input an integer and allowed them 
		to try again when they did not input an integer.
	"""
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			return answer
		except ValueError:
			print("That's not an integer. Try again.")
		
		
def float_input(prompt):
	"""
		Allows the user to input a float and allowed them 
		to try again when they did not input a float.
	"""
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That's not a real number. Try again.")