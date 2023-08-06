#!/usr/bin/env python3
#_*_ coding:utf-8 _*_


"""Main Function of the module dipwmsearch
   search for occurrences of the di-PWM contained in file <pathDiPwm>
   in the sequence contained the FASTA file <pathFasta>
   using the threshold ratio <ratio> the default ratio is 0.95
   print occurrences found on standard output, in tabulated format
"""
 
import statistics, sys, os
import ahocorasick
from Bio import SeqIO
from Bio.Seq import Seq

from .diPwm import diPWM, create_diPwm
from .Block import search_block_optimized

######################################################################
# GLOBAL CONSTANTS 
RETURN_OK = 0
RETURN_BAD = 1

# #####################################################################
# Main function so that the module can be used as script

# dummy main function
def test_main() -> int:
    """Dummy main function (only for debug purposes)       
       Echo the input arguments to standard output
    """

    phrase = ""
   
    for i in range( len(sys.argv) ):
            phrase = phrase + " " + sys.argv[i]
    print(phrase)
    return RETURN_BAD

######################################################################
# default search function: simply called search
def search(pathDiPwm, pathFasta, ratio) -> int:

    """search for occurrences of the di-PWM contained in file <pathDiPwm>
       in the sequence contained the FASTA file <pathFasta>
       using the threshold ratio <ratio> the default ratio is 0.95
       """

    
    # Creation objet diPwm
    diP = create_diPwm(pathDiPwm)
    nameDiPwm = os.path.basename(pathDiPwm)
    sys.stderr.write( f'diPWM: {nameDiPwm}\n' )

    # Threshold défini en fonction du ratio
    threshold = diP.set_threshold_from_ratio(ratio)

    # Ouverture du fichier Fasta et conversion en objet seqIO
    file = open(pathFasta)
    seqRecord = SeqIO.read(file, "fasta")
    # DEBUG:
    # print( seqRecord.id, os.path.basename(pathFasta), os.path.basename(pathFasta)[:-3] )
    seq_name = os.path.basename(pathFasta)[:-3]
    # Convert sequence text in uppercase
    text = str(seqRecord.seq.upper())

    # Create seq Reverse Complement et convert in text
    seqRC = seqRecord.seq.reverse_complement()
    textRC = str(seqRC.upper())

    # Recherche dnas le brin +
    for position, word, score in search_block_optimized(diP, text, threshold):
        # print(f'{position} \t {score} \t +')
        print(f'{position}\t{word}\t{score}\t+')
    # Recherche dans le brin -
    for position, word, score in search_block_optimized(diP, textRC, threshold):
        # print(f'{position} \t {score} \t -')
        print(f'{position}\t{word}\t{score}\t-')

    return RETURN_OK

######################################################################
# top level code
# check command line parameters
# check file availability
# check threshold range
# execute a default search using function search

if __name__ == '__main__':
    
    sys.stderr.write(__doc__)

    # default threshold ratio value
    DEF_RATIO = 0.95
    # minimum threshold ratio value
    MIN_RATIO = 0.80
    # min number of arguments for this script (script name included)
    MIN_ARG = 3
    
    # process parameters
    argc = len(sys.argv)
    # check correct arguments
    if ( argc < MIN_ARG ):
        sys.stderr.write("Usage: {0}\n 1st argument : filename of a di-PWM\n 2nd argument: filename of a FASTA file\n 3rd argument: a threshold ratio (between 0.8 and 1; default: 0.95)\n".format( sys.argv[0] ) )
        exit( RETURN_BAD )
    else: 
        dipfile = sys.argv[1]
        seqfile = sys.argv[2]
        
    # second parameter : add visualisation of plots
    if ( argc > MIN_ARG ):
        ratio_thr = float(sys.argv[3])
        if (ratio_thr < MIN_RATIO):
            sys.stderr.write( f"Input ratio threshold {ratio_thr} is too low. This threshold must be in the range [0.8, 1]\n" )
            sys.exit( RETURN_BAD )
            
    else:
        ratio_thr = DEF_RATIO
        
    ##############################
    # test if dipfile is present and readable
    try:
        f = open( dipfile )
        f.close()
    except FileNotFoundError:
        sys.stderr.write( "Input file {0} cannot be found\n".format( dipfile ) )
        exit( RETURN_BAD )
    except PermissionError:
        sys.stderr.write( "You need read access to file {0}. Change your access rights and relaunch program.\n".format( dipfile ) )
        sys.exit( RETURN_BAD )

    ##############################
    # test if seqfile is present and readable
    try:
        f = open( seqfile )
        f.close()
    except FileNotFoundError:
        sys.stderr.write( "Input file {0} cannot be found\n".format( seqfile ) )
        exit( RETURN_BAD )
    except PermissionError:
        sys.stderr.write( "You need read access to file {0}. Change your access rights and relaunch program.\n".format( seqfile ) )
        sys.exit( RETURN_BAD )

    ## CONTROL MESSAGE with parameters
    sys.stderr.write( f'Search call: {dipfile} {seqfile} {ratio_thr}\n' )
    
    sys.exit( search( dipfile, seqfile, ratio_thr) )

# END of MAIN
######################################################################
