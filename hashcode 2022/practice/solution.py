###############################
# *****       *****   * *     #
# *     *     *   *   *   *   #
# *  *        *****   *     * #
# *    *      *   *   *   *   #
# *       *   *   *   * *     #
###############################################
# Name: solution                              #
# Author: team RAD CODERS                     #
# purpose: resolve the hashcode 2022 problems #
###############################################

######## DON'T DELETE #########
from classes.base import Base #
rad_print = Base.rad_print    #
###############################

from classes.client import Client

samples = {"A": "testcase/a_an_example.in", "B": "testcase/b_basic.in", "C": "testcase/c_coarse.in", "D": "testcase/d_difficult.in", "E": "testcase/e_elaborate.in"}
# samples is a dict to store the path of the testcases

def get_entries(source, filepath=None):
	""" 
	Get the entries of the test case and return them
	source: a string to specify if entries come from input or a textfile
	filepath: a string to indicate the location of the file containing the entries 
	Need to be adapt to the problem
	"""
	#### Here goes the logic to retrieve the problem input #####
	
	if source.upper() == "INPUT":
		C = int(input())
		P = []
		for i in range(C):
			L = input().split(" ")
			L[0] = int(L[0])
			D = input().split(" ")
			D[0] = int(D[0])
			P.append([L,D])
	else:
		with open(filepath, "r") as file:
			
			
			C = int(file.readline().split("\n")[0])
			P = []
			for i in range(C):
				L = (file.readline().split("\n")[0]).split(" ")
				L[0] = int(L[0])
				D = (file.readline().split("\n")[0]).split(" ")
				D[0] = int(D[0])
				P.append([L,D])
		
	return C, P

def solution(C, P, filepath):
### Your code goes here ##
# use rad_print instead of print with filepath as first argument
# ex:	rad_print(filepath, C, P)
	
	clients = []
	for L, D in P:
		client = Client(L,D)
		clients.append(client)
	ingredients = set()
	for client in clients:
		ingredients.update(client.L)
		ingredients = ingredients - client.D
	rad_print(filepath, len(ingredients), *ingredients)

##### DON'T ADD OR DELETE LINE #####################
#     JUST UNCOMMENT THE CALLED METHOD YOU NEED    #
#     AND CHANGE THEIR ARGUMENTS TO MEET YOUR NEED #
def main():                                        #
	### Here goes the action you want to do ########  
	base = Base(samples, get_entries, solution)    #
	# base.create_submissions()                    #
	# base.execute_solution(("A"))                 #
                                                       #
if __name__ == "__main__":                             #
	main()                                         #
########################################################
