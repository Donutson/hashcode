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


class Client:
    """
    Represent a client with his likes and dislikes
    """
    def __init__(self, l, d):
        self.L = 0
        self.D = 0
        self.set_L(l)
        self.set_D(d)

    def set_L(self,l):
        self.L = set(l[1:])

    def set_D(self,d):
        self.D = set(d[1:])

    def __str__(self):
        if self.L == set():
            self.L = "nothing"
        if self.D == set():
            self.D = "nothing"
        return "He likes {} and dislikes {}".format(self.L, self.D)
