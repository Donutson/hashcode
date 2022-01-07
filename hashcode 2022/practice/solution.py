###############################
# *****       *****   * *     #
# *     *     *   *   *   *   #
# *  *        *****   *     * #
# *    *      *   *   *   *   #
# *       *   *   *   * *     #
###############################################
# Name: base                                  #
# Author: team RAD CODERS                     #
# purpose: resolve the hashcode 2022 problems #
###############################################

samples = {"A": "testcase/a_an_example.in", "B": "testcase/b_basic.in", "C": "testcase/c_coarse.in", "D": "testcase/d_difficult.in", "E": "testcase/e_elaborate.in"}
# samples is a dict to store the path of the testcases


def get_entries(source, filepath=None):
	""" 
	Get the entries of the test case and return them
	source: a string to specify if entries come from input or a textfile
	filepath: a string to indicate the location of the file containing the entries 
	Need to be adapt to the problem
	"""
	
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


def rad_print(filepath=None, *params, **params_dict):
	""" 
	Work as the built-in print,the difference is that we first give a filepath where the output will be stock. 
	If you want to display the output at screen just set filepath to None 
	"""
	
	if filepath:
		with open(filepath, "w") as file:
			print(file=file, *params, **params_dict)
	else:
		print(*params, **params_dict)


def create_submissions(sample=("A", "B", "C", "D", "E")):
	""" 
	Create the submissions files for the specify tests cases in sample.
	sample: a tuple containing the cases for which we want submissions files 
	"""
	
	for i in sample:
		filepath = samples[i.upper()]
		output = "submissions/"+i
		entries = get_entries("FILE",filepath)
		solution(*entries, output)
		
	print("All submissions file has been created in a folder call submissions!!")


def execute_solution(sample=("A", "B", "C", "D", "E"), mode="FILE"):
	""" 
	Execute our solution on all the specify tests cases in sample and display the output at standard output,
	we use it to see if our solution do what we expect from it
	sample: a tuple containing all the cases for which we want to execute our solution
	mode: a string specifying the way the entries are retrieve, FILE if it's from a file or INPUT if it's from keyboard typing 
	"""
	
	output = None
	
	if mode == "INPUT":
		sample = ()
		entries = get_entries(mode)
		solution(*entries, output)
		
	for i in sample:
		filepath = samples[i.upper()]
		entries = get_entries(mode,filepath)
		solution(*entries, output)


def solution(C, P, filepath):
### Your code goes here##
# use rad_print instead of print with filepath as first argument
# ex:	rad_print(filepath, C, L, D)
	pass
	
def main():
	###Here goes the action you want to do###
	# create_submissions()
	# execute_solution()
	pass

if __name__ == "__main__":
	main()