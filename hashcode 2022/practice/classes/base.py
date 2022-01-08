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


 ########################################################################
########### DON'T MODIFY EXCEPT IF YOU KNOW WHAT YOU ARE DOING ###########
 ########################################################################


from os import makedirs

class Base:
    """
    Let us automate the process of creation submissions for hashcode
    """

    def __init__(self, samples, get_entries, solution):
        self.samples = samples
        self.get_entries = get_entries
        self.solution = solution

    @staticmethod
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


    def create_submissions(self, sample=("A", "B", "C", "D", "E")):
        """ 
        Create the submissions files for the specify tests cases in sample.
        sample: a tuple containing the cases for which we want submissions files 
        """
        
        makedirs("submissions")

        for i in sample:
            filepath = self.samples[i.upper()]
            output = "submissions/"+i
            entries = self.get_entries("FILE",filepath)
            self.solution(*entries, output)
            
        print("All submissions file has been created in a folder call submissions!!")


    def execute_solution(self, sample=("A", "B", "C", "D", "E"), mode="FILE"):
        """ 
        Execute our solution on all the specify tests cases in sample and display the output at standard output,
        we use it to see if our solution do what we expect from it
        sample: a tuple containing all the cases for which we want to execute our solution
        mode: a string specifying the way the entries are retrieve, FILE if it's from a file or INPUT if it's from keyboard typing 
        """
        
        output = None
        
        if mode == "INPUT":
            sample = ()
            entries = self.get_entries(mode)
            self.solution(*entries, output)
            
        for i in sample:
            filepath = self.samples[i.upper()]
            entries = self.get_entries(mode,filepath)
            self.solution(*entries, output)
