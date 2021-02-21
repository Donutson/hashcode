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
	filepath: a string to indicate the location of the file containnig the entries """
	
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
		with open(filepath, "a") as file:
			print(file=file, *params, **params_dict)
	else:
		print(*params, **params_dict)


def create_submissions(sample=("A", "B", "C", "D", "E")):
	""" Create the submissions files for the specify sample.
	sample: a tuple containing the cases for which we want submissions files 
	NB: don't forget to delete actual submissions files before making new """
	
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

	class Pizza:
		
		N = 0	# number of Pizza's instance
		
		def __init__(self, n, ingredients):
			self._n = n	# number of ingredients
			self._ingredients = ingredients	# a set of the ingredients in the pizza
			self._pos = Pizza.N	# the pizza's index'
			Pizza.N += 1
			
		def _get_n(self):
			return self._n
			
		def _get_ingredients(self):
			return self._ingredients
			
		def _get_pos(self):
			return self._pos
			
		def __repr__(self):
			me = "Pizza "+str(self._pos)
			me += " , has the following ingredients:\n"
			for ingredient in self._ingredients:
				me += ingredient + "\n"
			
			return me
			
		n = property(_get_n)
		ingredients = property(_get_ingredients)
		pos = property(_get_pos)
		
		
	class Pizzaria:
		N = M	# Total number of available pizza
		
		def __init__(self):
			self._pizzas = []	# the pizzas they have
			
		def _get_pizzas(self):
			return self._pizzas
				
		def _add_pizza(self, pizza):
			self._pizzas.append(pizza)
			
		def rpizzas(self):
			""" Sort the pizzas from the one with the greater number of ingredients to the lowest one"""
			
			self._pizzas = sorted(self._pizzas, key=(lambda pizza: pizza.n), reverse= True)
				
		pizzas = property(_get_pizzas, _add_pizza)
		
	class Team:
			
		def __init__(self, n):
			self._n = n	# number of people in that team
			self.pizzas = []	# the pizzas they've got from the pizzaria'
				
		def _get_n(self):
			return self._n
				
		n = property(_get_n)
		
		
	class Delivery:
		N = 0	# Number of deliveries
		
		def __init__(self):
			self._teams = []	# teams getting a delivery
			
		def _add_team(self, team):
			self._teams.append(team)
			Delivery.N += 1
		
		def _get_teams(self):
			return self._teams
		
		def make_deliveries(self):
			rad_print(filepath, Delivery.N)
			for team in self._teams:
				rad_print(filepath, team.n, end=" ")
				for pizza in team.pizzas:
					rad_print(filepath, pizza.pos, end=" ")
				rad_print(filepath)
		
		teams = property(_get_teams, _add_team)
		
		
	class GroupOfPizza:
		def __init__(self):
			self._pizzas = []	# all the pizzas in that group
			self._n = 0	# the number of pizzas in that groupe
			self._ingredients = set()	# all ingredients in that group
			self._inter = 0	# Number of commons ingredients in the group
			
		def _add_pizza(self,pizza):
			self._pizzas.append(pizza)
			self._n += 1
			self._ingredients.add(pizza.ingredients)
			self._inter = len(self._ingredients & pizza.ingredients)
		
		def _get_pizzas(self):
			return self._pizzas
		
		def _get_n(self):
			return self._n
			
		def _get_ingredients(self):
			return self._ingredients
			
		def _get_inter(self):
			return self._inter
			
		pizzas = property(_add_pizza, _get_pizzas)
		n = property(_get_n)
		ingredients = property(_get_ingredients)
		inter = property(_get_inter)
			
##### Start of the proper code #####
	pizzaria = Pizzaria()
	delivery = Delivery()
	
	for d in D:
		d = d.split(" ")
		d[-1] = d[-1][:-1]
		pizza = Pizza(int(d[0]), set(d[1:]))
		pizzaria.pizzas = pizza
		
	pizzaria.rpizzas()
	pizzas = pizzaria.pizzas
	
	nb = len(pizzas)
	groups = []
	
	while nb > 1:
		n = 0
		pizza0 = pizzas[0]
		pizzas.sort(key=(lambda pizza1: len(pizza0.ingredients & pizza1.ingredients)))
		group = GroupOfPizza()
		group.pizzas = pizza0
		group.pizzas = pizzas[1]
		del pizzas[:2]
		
		for i in range(2):
			if len(pizza[0].ingredients & group.ingredients) > group.inter:
				break
			else:
				group.pizzas = pizza[0]
				del
			
	
	while M >= 4 and T4 != 0:
		team = Team(4)
		team.pizzas = pizzas[:4]
		del pizzas[:4]
		T4 -= 1
		M -= 4
		delivery.teams = team
		
	while M >= 3 and T3 != 0:
		team = Team(3)
		team.pizzas = pizzas[:3]
		del pizzas[:3]
		T3 -= 1
		M -= 3
		delivery.teams = team
		
	while M >= 2 and T2 != 0:
		team = Team(2)
		team.pizzas = pizzas[:2]
		del pizzas[:2]
		T2 -= 1
		M -= 2
		delivery.teams = team
	
	delivery.make_deliveries()
	

def main():
	###Here goes the action you want to do###
	create_submissions()
	# execute_solution()

if __name__ == "__main__":
	main()