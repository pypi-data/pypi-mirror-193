#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import ahocorasick
from .diPwm import diPWM
from .Enumerate import enumerate_words_LAM, enumerate_words_LAM_ratio

##################################################
def search_aho(diP, text, threshold):
	"""Find in the sequence <text>, all occurrences of the di-PWM <diP> whose score is greater than the minimum score threshold <threshold>
           1. generate the list of valid words for the di-PWM <diP> satisfying the score constraint and build an Aho-Corasick automaton for them
           2. search for occurrences of these valid words in <text> using the Aho-Corasick automaton and report the list of all their occurrences

         Other description: Search of a set of words through a text using Aho-Corasick algorithm for a given threshold.

	Args:
		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		threshold (float): threshold given to select the windows

	Yields:
		tuple: starting_position, word, score
	"""

	# create empty automaton
	autom = ahocorasick.Automaton()

	# fill automaton with words and scores
	for word, score in enumerate_words_LAM(diP, threshold):
		autom.add_word(word, (word,score))
	autom.make_automaton()

	# search with the automaton through the text : yields starting position in the text, word, score
	for (position, (word, score)) in autom.iter(text):
		yield position-diP.length, word, score

##################################################
def search_aho_ratio(diP, text, ratio):
	""" Find occurrences of the di-PWM <diP> in the sequence <text> for a ratio threshold <ratio>
            1. computes a score threshold from the ratio
            2. call function search_aho to perform the search of the occurrences in the sequence

            Other description: 
              Search of a set of words through a text using Aho-Corasick algorithm for a given ratio.
              From the ratio is calculated the threshold.

	Args:
 		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		ratio (float): float or int. From 0 to 1

	Yields:
		tuple: starting_position, word, score
	"""
	threshold = diP.set_threshold_from_ratio(ratio)
	for position, word, score in search_aho(diP, text, threshold):
		yield position, word, score


##################################################
# fn added 10.02.23
# good default pvalue threshold ? here 10^-6

def search_aho_pvalue(diP, text, pvalue = 0.000001 ):
	""" Find occurrences of the di-PWM <diP> in the sequence <text> for the pvalue threshold <pvalue>
            1. computes a score threshold from the pvalue
            2. call function search_aho to perform the search of the occurrences in the sequence

        Remark: it is difficult to find a good pvalue threshold ; we advise to make several trials starting with very low (restrictive) threshold values. Otherwise, use the search_aho_ratio function instead.

	Args:
 		diP (diPWM): object diPWM

		text (string): text to search on the motif (first position = 0)

		pvalue (float): float. pvalue threshold given to select the occurrences.
                                Between 0 and strictly less to 1

	Yields:
		tuple: starting_position, word, score
	"""
        
	# calculate threshold from pvalue
	threshold = diP.set_threshold_from_pvalue( pvalue )
        # perform the search
	for position, word, score in search_aho(diP, text, threshold):
		yield position, word, score

