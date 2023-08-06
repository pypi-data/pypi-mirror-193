#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
import math
from itertools import product


######################################################################
# GLOBAL CONSTANTS 
# default values for k and n used in the computation of score threshold
# from a P-value
N_DEF = 4
K_DEF = 0.05

######################################################################
# Class diPwm
class diPWM:
    """ A class to represent a diPWM

    Attributes :
        value : list of dictionaries
            values of the diPWM for each position and di-symbol
        alphabet : list of char
            symbols of the alphabet
        alphabet_size : int
            size of the alphabet
        length : int
            size of the diPWM
        LAM : list of dictionaries
            LookAheadMatrix : to estimate maximum full score from a prefix
        min : float
            score minimum of the diPWM
        max : float
            score maximum of the diPWM

    Methods :
        __len__():
            returns length of the diPWM object, ie length lenght of diPWM.value
        __str__():
            returns string to print the diPWM object
        __eq__(diP_other):
            returns boolean to compare if 2 diPWM object have same values
        make_look_ahead_matrix():
            returns the lookAheadMatrix of the diPWM object
        find_min_diPwm():
            returns the score min of the diPWM object
        find_max_diPwm():
            returns  the score max of the diPWM object
        make_look_back_matrix():
            returns the lookBackMatrix of the diPWM object
        make_look_ahead_table():
            returns lookAheadTable of the diPWM object
        make_look_back_table():
            returns the lookBackTable of the diPWM object
        set_threshold_from_ratio(ratio):
            returns the score threshold calculated from the given ratio threshold
        set_threshold_from_pvalue(self, pvalue, k = 16, n = 4):
            returns the score threshold calculated from the given pvalue threshold
            k and n parameters serve to control the precision of the approximation
    """    
    def __init__(self, diPwm_list, alphabet_choice = 'DNA'):
        """ Constructs all the necessary attributes for the diPWM object.

        Args:
            diPwm_list (list of lists): list of list of values at each position for each di-symbol in lexicographic order

            alphabet_choice (str, optional): choice of alpahbet between 'DNA, 'RNA' and 'Protein'. Defaults to 'DNA'.

        Raises:
            NameError: wrong alphabet choice

            NameError: length of diPwm is zero

            NameError: numbers of values at a position doesn't match the number of di-symbols
        """        
        if alphabet_choice == 'DNA':
            self.alphabet = ['A', 'C', 'G', 'T']
        elif alphabet_choice == 'RNA':
            self.alphabet = ['A', 'C', 'G', 'U']
        elif alphabet_choice == "Protein":
            self.alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
        else:
            raise NameError(f'The alphabet "{alphabet_choice}" is not known, please use "DNA", "RNA" or "Protein"!')

        self.alphabet_size = len(self.alphabet)

        list_diNT = ["".join(x) for x in product(self.alphabet, repeat =2)]
        self.value = [ {list_diNT[i] : x for i,x in enumerate(liste)} for liste in diPwm_list]

        # Check that the list is not empty
        if len(self.value) == 0:
            raise NameError('Length of diPwm is zero')

        self.length = len(self.value)

        # Check and update the alphabet_size
        for (i,diP_column) in enumerate(self.value):
            if self.alphabet_size != math.sqrt(len(diP_column)):
                raise NameError(f'Number of lines of the column {i} of the diPwm is not good.')

        self.LAM = self.make_look_ahead_matrix()

        self.min = self.find_min_diPwm()

        self.max = self.find_max_diPwm()


    # Others operators
    # use len(diP)
    def __len__(self):
        """ Defines length of diPWM object as length of diPWM.value

        Returns:
            int: length of diPWM
        """        
        return self.length

    # use print(diP)
    def __str__(self):
        """ Defines string to print for a diPWM object

        Returns:
            str: print the diPWM.value in a matrix format
        """        
        output_string = 'diPwm:'  + '\n'
        output_string += '\t' + '\t'.join([str(x) for x in self.value[0].keys()]) + '\n'
        for (i,lines) in enumerate(self.value):
            output_string += str(i) + ':\t' + '\t'.join([str(round(x,2)) for x in lines.values()]) + '\n'
        return output_string

    # use diP1 == diP2
    def __eq__(self,diP_other):
        """ Check if deux different objects diPWM have same values

        Args:
            diP_other (diPWM): other object diPWM we want to compare to

        Returns:
            boolean: True if values are equal
        """        
        return [{k : round(v,6) for k,v in diP.items()} for diP in self.value] == [{k : round(v,6) for k,v in diP.items()} for diP in diP_other.value]

    # Auxiliary functions
    # use make_look_ahead_matrix(diP)
    def make_look_ahead_matrix(self):
        """ Builds LookAheadMatrix for a diPWM object.
        Values are estimate of the max reachable score of a suffix starting at a position with a specific symbol

        Returns:
            list of dictionaries: a list of values of size of the alphabet per position
        """

        # initialize matrix of size : lines = length of diPWM , columns = alphabet size        
        matrix = [{j:-math.inf for j in self.alphabet} for i in range(self.length)]

        # case of the last position
        for d in self.alphabet:
            maxi = (-math.inf)
            for b in self.alphabet:
                score = self.value[self.length - 1][d+b]
                if (score > maxi):
                    maxi  =  score
            matrix[self.length-1][d] = maxi

        # fill matrix recursively from end to start
        for i in range(self.length-2,-1,-1):
            for d in self.alphabet:
                maxi = (-math.inf)
                for b in self.alphabet:
                    score = self.value[i][d+b] + matrix[i+1][b]
                    if score > maxi:
                        maxi = score
                matrix[i][d] = maxi

        return matrix + [{i:0 for i in self.alphabet}]

    def find_min_diPwm(self):
        """ Computes minimum score of the diPWM object

        Returns:
            float: minimum score that can be reached for a word with the diPWM object
        """        
        # initialize matrix of size : lines = length of diPWM , columns = alphabet size        
        matrix = [{j:-math.inf for j in self.alphabet} for i in range(self.length)]

        # case of the last position
        for d in self.alphabet:
            mini = (math.inf)
            for b in self.alphabet:
                score = self.value[self.length-1][d+b]
                if (score < mini):
                    mini = score
            matrix[self.length-1][d] = mini

        # fill matrix recursively from end to start
        # values are min score of suffix starting with symbol
        for i in range(self.length-2,-1,-1):
            for d in self.alphabet:
                mini=(math.inf)
                for b in self.alphabet:
                    score = self.value[i][d+b] + matrix[i+1][b]
                    if score < mini:
                        mini = score
                matrix[i][d] = mini


        min_diPwm = min(matrix[0].values())
        return min_diPwm
    
    ########################################
    def find_max_diPwm(self):
        """ Computes the maximum score of the diPWM object
            use the LAM and look at the maximum in the first column of the LAM

        Returns:
            float: maximum score that can be reached for a word with the diPWM object
        """        
        matrix = self.LAM
        max_diPwm = max(matrix[0].values())
        return max_diPwm

    def make_look_back_matrix(self):
        """Builds LookBackMatrix for a diPWM object
        Values are estimate of the max reachable score of a prefix ending at a position with a specific symbol

        Returns:
            list of dictionaries: a list of values of size of the alphabet per position
        """        
        # initialize matrix of size : lines = length of diPWM , columns = alphabet size        
        matrix = [{j:-math.inf for j in self.alphabet} for i in range(self.length)]

        # case of the first position
        for b in self.alphabet:
            maxi = (-math.inf)
            for d in self.alphabet:
                score = self.value[0][d + b]
                if (score > maxi):
                    maxi = score
            matrix[0][b] = maxi

        # fill matrix recursively
        # values are max score of prefix ending with symbol
        for i in range(1,self.length):
            for b in self.alphabet:
                maxi = (-math.inf)
                for d in self.alphabet:
                    score = self.value[i][d + b] + matrix[i-1][d]
                    if score > maxi:
                        maxi = score
                matrix[i][b] = maxi

        return matrix

    def make_look_ahead_table(self):
        """ Builds LookAheadTable for a diPWM object.
        Values are estimate of the max reachable score of a suffix starting at a position

        Returns:
            list: a value for each position
        """        
        # intialize table of length of diPWM with -infinite value
        table = [(-math.inf)]*self.length

        # case of the last element of the table = max of values at the last position
        table[-1] =  max(self.value[self.length-1].values())

        # computes recursively elements of the table
        for i in range((self.length-2),-1,-1):
            table[i] = max(self.value[i].values()) + table[i+1]

        return table

    def make_look_back_table(self):
        """ Builds LookBackTable for a diPWM object
        Values are estimate of the max reachable score of a prefix ending at a position

        Returns:
            list: a value for each position
        """        
        # intialize table of length of diPWM with -infinite value
        table = [(-math.inf)]*self.length

        # case of the first element of the table = max of values at the first position
        table[0] =  max(self.value[0].values())

        # computes recursively elements of the table
        for i in range(1,self.length):
            table[i] = max(self.value[i].values()) + table[i-1]

        return table
    
    ########################################
    def set_threshold_from_ratio(self, ratio):
        """Computes the score threshold from the input ratio threshold and the diPWM

        Args:
            ratio (float): float or int. From 0 to 1

        Returns:
            float: value of the threshold for the diPWM
        """        
        threshold = self.min + (self.max-self.min)*ratio
        return threshold

    ######################################################################
    # BASTIEN new 06.02.2023 ; update ER 13-20/02/2023
    # functions for computing a score threshold from a pvalue
    ##############################
    # comp_prefix_score : for compute prefix score
    # used twice in set_borne_from_str
    def set_score_from_str(self, m):
        """For the current diPWM, computes the score of a given string m
           that is a prefix of full length word (extended k-mer)

        Args:
            m (string): String

        Returns:
            float: value of the score of the given string on the diPWM
        """
        score = 0
        for i in range(len(m)-1):
            score += self.value[i][m[i:i+2]]
        return score

    ##############################
    # count_words_starting_with_prefix
    # fn used three times: once in get_recu; twice in set_threshold_from_pvalue
    
    def set_nb_from_str(self, m):
        """Computes the number of extended k-mers which have the given string as prefix

        Args:
            m (string): String

        Returns:
            int: number of extended k-mers which have the given string as prefix
        """
        return pow(self.alphabet_size,self.length - len(m)+1)

    ##############################
    # comp_score_bounds_words_starting_with_prefix
    # fn used once in get_recu
    def set_borne_from_str(self,m,matrix_min,matrix_max):
        """Computes the minimum and maximum scores of extended k-mers which have the given string as prefix

        Args:
            m (string): String

        Returns:
            float, float: minimum and maximum score of extended k-mers which have the given string as prefix
        """
        if len(m) > 0:
            return self.set_score_from_str(m) + matrix_min[len(m)-1][m[-1]],self.set_score_from_str(m) + matrix_max[len(m)-1][m[-1]]
        else:
            return min(matrix_min[0].values()),max(matrix_max[0].values())

    ##############################
    # count_words_starting_with_prefix
    def get_recu(self,m,L,matrix_min,matrix_max,N,T):
        """Computes recursively the list L

        Args:
            m (string): String
            L (list): list of triplets (number of words, minimum score, maximum score)
            N : max nb of words in a bloc (nb max du bloc pour stop)
            T : maximum difference of score for words in a block

            in french:
            N : nb max du bloc pour stop
            T : threshold pour interval

        Returns:
            void
        """
        for a in self.alphabet:
            # extend current prefix m with letter a
            m2 = m + a
            # compute a nb of extended words starting with prefix m2
            # could be done only once before the loop (because length(m2) = length(m)+1
            nb = self.set_nb_from_str(m2)
            borne_min,borne_max = self.set_borne_from_str(m2,matrix_min,matrix_max)
            # if we reach the limits of a block
            if (nb <= N) or ( (borne_max-borne_min) <= T):
                # then append the block to L
                L.append([nb,borne_min,borne_max])
            else:
                # else: recurse to extend the current prefix m2
                self.get_recu(m2,L,matrix_min,matrix_max,N,T)


    ##############################
    # set_threshold_from_pvalue
    # default values for k and n are defined in the header of this file
    # N_DEF = 4
    # K_DEF = 0.05
    
    def set_threshold_from_pvalue(self, pvalue, k = K_DEF, n = N_DEF):
        """
        Given a pvalue threshold, computes a score threshold corresponding to this pvalue
        The algorithm yields an approximate value in general.

        Args:
            pvalue (float): p-value threshold
            k (float): between 0 and 1; to determine the maximum difference of score for words in a block
            n (integer): control the max nb of words in a block (log_4 of this number); minimum is 1
        
        Remark:
            - k and n control the precision of the pvalue computation
            - the smaller k is, the more accurate the threshold is
            - the smaller n is, the more accurate the threshold is
            - k and n are used only once to determine the parameters N and T before launching the recursive computation of list of block with get_recu

        Returns:
            a score threshold: float
        """
        # control parameters n and k
        if (k < 0):
            # set k to its default value
            k = K_DEF
        if (n < 1):
            # set n to its default value
            n = N_DEF
            
        matrix = [{j:-math.inf for j in self.alphabet} for i in range(self.length)]

        # case of the last position
        for d in self.alphabet:
            mini = (math.inf)
            for b in self.alphabet:
                score = self.value[self.length-1][d+b]
                if (score < mini):
                    mini = score
            matrix[self.length-1][d] = mini

        # fill matrix recursively from end to start
        # values are min score of suffix starting with symbol
        for i in range(self.length-2,-1,-1):
            for d in self.alphabet:
                mini=(math.inf)
                for b in self.alphabet:
                    score = self.value[i][d+b] + matrix[i+1][b]
                    if score < mini:
                        mini = score
                matrix[i][d] = mini

        matrix_min = matrix + [{i:0 for i in self.alphabet}]
        matrix_max = self.LAM

        L = []
        # Bastien : Si on veut associer une limite qui ne garde que des prefixes de longueur n
        # N = self.set_nb_from_str("")/pow(4,n)
        N = pow(4,n)
        T = k*(self.max-self.min)
        self.get_recu("",L,matrix_min,matrix_max,N,T)

        # initialize nb_aux used in the computation of good_bmin
        nb_aux = self.set_nb_from_str("")
        
        # compute the number of words that should have a score below the threshold to be determined
        nb_pvalue = (1-pvalue) * nb_aux
        # nb_pvalue = (pvalue)*self.set_nb_from_str("")

        # computation of good_bmin
        L.sort(key=lambda x: x[1],reverse=True)

        for nb,bmin,bmax in L:
            nb_aux -= nb
            if nb_aux <= nb_pvalue:
                good_bmin = bmin
                break

        # computation of good_bmax
        L.sort(key=lambda x: x[2])

        # re-initialize nb_aux
        nb_aux = 0
        for nb,bmin,bmax in L:
            nb_aux += nb
            if nb_aux >= nb_pvalue:
                good_bmax = bmax
                break
        
        # return the average of good_bmax and good_bmin
        return (good_bmax+good_bmin)/2

    # BASTIEN Fin Nouveau
    ######################################################################

def create_diPwm(pathDiPwm, alphabet_choice = 'DNA'):
    """ Build a diPWM object from a file.

    Args:
        pathDiPwm (string): path of the diPwm file

    Returns:
        diPWM object
    """    
    #Read diPWM in a tabulated format
    with open(pathDiPwm) as file:
        # User list comprehension to create a diPWM object
        diPwm_matrix = diPWM([[float(y) for y in x.strip().split('\t')] for x in file.readlines() if x[0] != '>'], alphabet_choice)
        return diPwm_matrix
