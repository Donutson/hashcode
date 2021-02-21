###############################
# *****       *****   * *     #
# *     *     *   *   *   *   #
# *  *        *****   *     * #
# *    *      *   *   *   *   #
# *       *   *   *   * *     #
###############################################
# Name: base                                  #
# Author: team RAD CODERS                     #
# purpose: resolve the hashcode 2021 problems #
###############################################

samples = {"A": "testcase/a_example", "B": "testcase/b_little_bit_of_everything.in", "C": "testcase/c_many_ingredients.in", "D": "testcase/d_many_pizzas.in", "E": "testcase/e_many_teams.in"}
# samples is a dict to store the path of the testcases


def get_entries(source, filepath=None):
	""" Get the entries of the test case and return them
	source: a string to specify if entries come from input or a textfile
	filepath: a string to indicate the location of the file containing the entries """
	
	if source.upper() == "INPUT":
		M, T2, T3, T4 = list(map(int, input().split(" ")))
		D = []
		for i in range(M):
			D.append(input())
	else:
		with open(filepath, "r") as file:
			M, T2, T3, T4 = list(map(int, file.readline()[:-2].split(" ")))
			D = []
			for i in range(M):
				D.append(file.readline())
		
	return M, T2, T3, T4, D


def rad_print(filepath=None, *params, **params_dict):
	""" Work as the built-in print,the difference is that we first give a filepath where the output will be stock. If you want to display the output at screen just set filepath to None """
	
	if filepath:
		with open(filepath, "w") as file:
			print(file=file, *params, **params_dict)
	else:
		print(*params, **params_dict)


def create_submissions(sample=("A", "B", "C", "D", "E")):
	""" Create the submissions files for the specify sample.
	sample: a tuple containing the cases for which we want submissions files """
	
	for i in sample:
		filepath = samples[i.upper()]
		output = "submissions/"+i
		entries = get_entries("FILE",filepath)
		solution(*entries, output)
		
	print("All submissions file has been created in a folder call submissions!!")


def execute_solution(sample=("A", "B", "C", "D", "E"), mode="FILE"):
	""" Execute our solution on all the specify sample
	sample: a tuple containing all the cases for which we want to execute our solution
	mode: a string specifying the way the entries are retrieve, FILE if it's from a file or INPUT if it's from keyboard typing """
	
	output = None
	
	if mode == "INPUT":
		sample = ()
		entries = get_entries(mode)
		solution(*entries, output)
		
	for i in sample:
		filepath = samples[i.upper()]
		entries = get_entries(mode,filepath)
		solution(*entries, output)


def solution(M, T2, T3, T4, D, filepath):
### Your code goes here##
# use rad_print instead of print with filepath as first argument
# ex:	rad_print(filepath, M, T2, T3, T4)
	pass
	
def main():
	###Here goes the action you want to do###
	# create_submissions()
	# execute_solution()
	pass

if __name__ == "__main__":
	main()