#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
from src.diPwm import diPWM, create_diPwm
from src.AhoCorasick import search_aho
from math import fabs

DEBUG = False
cumulated_difference_threshold = 0.01

def test_pvalue():
    pathDiPwm = "./data/ATF4_HUMAN.H11DI.0.A.dpwm"
    diP=create_diPwm(pathDiPwm)

    # list of Pvalues thresholds
    L = [ 0.0001, 0.0005, 0.001 ]
    # empty list of score thresholds 
    S= []
    # precision parameters for Pvalue computation
    k = 0.025
    n = 2
    
    for i in L:
        score = diP.set_threshold_from_pvalue( i, k, n )
        print( i, " ", score )
        S.append( score )

    # Check whether values in S are close to those of solutions stored in Scores
    # CACCTGAAGCAATT 9.758137921158239 0.000150576234
    # TTAATAATGAAATG 4.636829825579451 0.000651195645
    # GTTCTGACGCATTG 2.0259309215181425 0.001265782863 
    Scores = [ 9.75813, 4.63682, 2.02593 ]
    diff = 0
    for i,j in zip(Scores,S):
        print( i-j, i, j )
        diff += fabs(i-j)

    print( "The cumulated difference between computed score thresholds and true thresholds is ", diff )
    # test with assert instruction
    assert  diff < cumulated_difference_threshold , "The cumulated difference between computed score thresholds and true thresholds is larger than {0}\n".format( cumulated_difference_threshold )
