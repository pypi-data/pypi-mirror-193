#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import statistics, sys
import math
import ahocorasick
from .diPwm import diPWM, create_diPwm
from .SemiNaive import search_semi_naive_LAM_window, search_semi_naive_LAM


def compute_positions_kept(diP, k):
	""" Compute the list of positions of the diPWM object where the standard deviation is more than `k`.

	Args:
		diP (diPWM): object diPWM

		k (float): threshold given to select the position of the diPWM object

	Return:
		list of int: a list of positions of the diPWM object
	"""

	list_positions_kept = []
	for i in range(diP.length):
		dico = diP.value[i]
		standard_dev = statistics.stdev(list(dico.values()))
		if standard_dev > k :
			list_positions_kept.append(i)
	# FR version # print(f'Liste des positions gardées : {list_positions_kept}', file=sys.stderr)
	print(f'List of kept positions : {list_positions_kept}', file=sys.stderr)
	return list_positions_kept


def make_blocks(list_positions_kept):
	""" Translate a list of position in a list of blocks.

	Args:
		list_positions_kept (list of int): list of positions

	Return:
		list of int: a list of blocks
	"""

	list_blocks = []
	for i in range(len(list_positions_kept)):
		if i == 0 or list_positions_kept[i] != list_positions_kept[i - 1] + 1:
			list_blocks.append([])
			list_blocks[-1].append(list_positions_kept[i])
		else:
			list_blocks[-1].append(list_positions_kept[i])
	# FR version # print(f'Liste des blocs : {list_blocks}', file=sys.stderr)
	print(f'List of blocks: {list_blocks}', file=sys.stderr)
	return list_blocks


def get_longest_block(list_blocks):
	""" Give the longest block of a list of blocks.

	Args:
		list_blocks (list of int): list of blocks

	Return:
		list of int: list of successive positions (a block)
	"""

	list_length = []
	for block in list_blocks:
		list_length.append(len(block))
	index_longest_block = (-max((x,-i) for i,x in enumerate(list_length))[1])
	# FR version # print(f'Plus long bloc : {list_blocks[index_longest_block]}, taille bloc : {len(block)}', file=sys.stderr)
	# ER comment: error when printing the length of the longest block. Currently block is the last block of the list, not the longest one. Corrected below 22.08.22.
	print(f'Longest block: {list_blocks[index_longest_block]},  bloc length: {list_length[index_longest_block]}', file=sys.stderr)
	return list_blocks[index_longest_block]


def enumerate_block(diP, block, threshold):
	""" This function enumerates words of length of `block + 1` which scores are in the total diPWM >= to `threshold`.
	To estimate score, this function uses LAM and LBM to extend the score on the right and on the left.

	Args:
		diP (diPWM): object diPWM

		block (list of int): list of successive positions (a block)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: word, score
	"""

	LBM = diP.make_look_back_matrix()
	stack = []

	# for root, child and parent : [0]:level, [1]:score, [2]:prefix
	# one root per symbol of the alphabet
	for nt in diP.alphabet:
		root = (block[0], LBM[block[0]][nt],nt)
		stack.append(root)

	while stack:
		parent = stack.pop()

		for d in diP.alphabet:
			child = (
				parent[0] + 1,
				parent[1] + diP.value[parent[0]][parent[2][-1] + d],
				parent[2] + d
			)
			if child[1] + diP.LAM[child[0]][d] >= threshold :
				if parent[0] == block[-1] :
					yield child[2], child[1] + diP.LAM[child[0]][d]		# generate word, score
				else :
					stack.append(child)

######################################################################
# search using the longest core block

def search_block(diP, text, threshold):
	""" Search of a set of subwords through a text using Aho-Corasick algorithm for a given threshold and check the windows by using LAM.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: starting_position, word, score
	"""

	list_positions_kept = compute_positions_kept(diP,1)
	list_blocks = make_blocks(list_positions_kept)
	block = get_longest_block(list_blocks)


	autom = ahocorasick.Automaton()
	for word, score in enumerate_block(diP, block, threshold):
		autom.add_word(word, (word,score))
	autom.make_automaton()

	for (position, (word, score)) in autom.iter(text):
		start_position = position - (block[-1] + 1)
		if position < len(text) - diP.length + block[-1]:
			score = search_semi_naive_LAM_window(diP, start_position ,text, threshold)
			if score:
				yield start_position,text[start_position:start_position+diP.length+1], score


######################################################################
# search_block_ratio
# takes a diP, a text, and a ratio:
# 1. convert the ratio in threshold and
# 2. call search_block with this threshold
                                
def search_block_ratio(diP, text, ratio):
	""" Search of a set of subwords through a text using Aho-Corasick algorithm for a given threshold and check the windows by using LAM. From the ratio is calculated the threshold.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: starting_position, word, score
	"""

	# calculate threshold from ratio
	threshold = diP.set_threshold_from_ratio(ratio)
	for position, word, score in search_block(diP, text, threshold):
		yield position, word, score

############################################################
def get_block_optimized(diP):
	""" Compute a block of the diPWM object by a heuristic.

	Args:
		diP (diPWM): object diPWM

	Return:
		list of int: list of successive positions (a block)
	"""

    # Computes standard deviation for each position of the diPWM
	li_sd = [statistics.stdev(list(dico.values())) for dico in diP.value]

    # Computes mean of standard deviation for possible blocks
	li_interval_possible = [(list(range(i,j+1)),statistics.mean(li_sd[i:j+1])) for i in range(len(diP)) for j in range(i,len(diP)) if j - i + 1 >= min(len(diP)-3,10)]
	
    # Sort by decreasing value of mean
	li_interval_possible.sort(key=lambda x:x[1],reverse=True)

    # Return list of positions for the block with highest mean
	return li_interval_possible[0][0]

######################################################################
# similar to search_block but using the optimized core block

def search_block_optimized(diP, text, threshold):
	"""Find in the sequence <text>, all occurrences of the di-PWM <diP> whose score is greater than the minimum score threshold <threshold>. Done using a core block optimized strategy: the core block is a reduced di-PWM with selective positions. The search is done for the core block and core occurrences are extended to full length word occurrences. See the article for details.

           Other description: Search of a set of subwords through a text using Aho-Corasick algorithm for a given threshold and check the windows by using LAM. The subwords are compute with a heuristic.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: starting_position, word, score
	"""
        # compute the core block of the di-PWM
        # this defines - a reduced di-PWM containing only the columns for core
        #              - and a core length that is shorter compared to the initial di-PWM
        
	block = get_block_optimized(diP)

        # enumerate the core valid words for the core length and build an Aho_Corasick automaton for them

	autom = ahocorasick.Automaton()
	for word, score in enumerate_block(diP, block, threshold):
		autom.add_word(word, (word,score))
	autom.make_automaton()
        
        # search for occurrences of core valid words
        # then check the window centered on the core valid word
        # to verify if there is a full-length occurrence

	for (position, (word, score)) in autom.iter(text):
		start_position = position - (block[-1] + 1)
		if position < len(text) - diP.length + block[-1]:
			score = search_semi_naive_LAM_window(diP, start_position ,text, threshold)
			if score:
				yield start_position,text[start_position:start_position+diP.length+1], score

############################################################
######################################################################
# search_block_optimized_ratio
# takes a diP, a text, and a ratio:
# 1. convert the ratio in threshold and
# 2. call search_block_optimized with this threshold
# remark: similar to search_block_ratio but with optimized core block

def search_block_optimized_ratio(diP, text, ratio):
	""" Find occurrences of the di-PWM <diP> in the sequence <text> for a ratio threshold <ratio>
            1. computes a score threshold from the ratio
            2. call function search_block_optimized to perform the search of the occurrences in the sequence

	Other description:
              Search of a set of subwords through a text using Aho-Corasick algorithm for a given threshold and check the windows by using LAM. The subwords are compute with a heuristic. From the ratio is calculated the threshold.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: starting_position, word, score
	"""
	# calculate threshold from ratio
	threshold = diP.set_threshold_from_ratio(ratio)
	for position, word, score in search_block_optimized(diP, text, threshold):
		yield position, word, score


######################################################################
# search_block_optimized_pvalue
# takes a diP, a text, and a pvalue threshold:
# 1. convert the pvalue threshold  in a score threshold and
# 2. call search_block_optimized with this threshold
# remark: similar to search_block_ratio but with a pvalue threshold instead
##########
# fn added 10.02.23
# good default pvalue threshold ? here 10^-6

def search_block_optimized_pvalue(diP, text, pvalue = 0.000001 ):
	""" Find occurrences of the di-PWM <diP> in the sequence <text>  for the pvalue threshold <pvalue>
            1. computes a score threshold from the pvalue
            2. call function search_block_optimized to perform the search of the occurrences in the sequence

        Remark: it is difficult to find a good pvalue threshold ; we advise to make several trials starting with very low (restrictive) threshold values. Otherwise, use the function search_block_optimized_ratio instead.

	Other description:
              Search of a set of subwords through a text using Aho-Corasick algorithm for a given threshold and check the windows by using LAM. The subwords are compute with a heuristic. From the ratio is calculated the threshold.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		pvalue (float): pvalue threshold given to select the occurrences.
                                Between 0 and strictly less to 1.

	Yields:
		tuple: starting_position, word, score
	"""
        
	# calculate threshold from pvalue
	threshold = diP.set_threshold_from_pvalue( pvalue )
        # perform the search
	for position, word, score in search_block_optimized(diP, text, threshold):
		yield position, word, score


#
