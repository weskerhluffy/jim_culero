'''
Created on 23/11/2016

@author: ernesto
'''
import logging
import sys


nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def jim_cacas_core(matrix):
    putlas = []
    
    for idx_caca, [a, b] in enumerate(matrix):
        putlas.append((a + b, idx_caca))
    
    logger_cagada.debug("putlas %s" % putlas)
    
    putlas_ord = sorted(putlas)
    
    logger_cagada.debug("putlas ord %s" % putlas)
    
    return putlas_ord

def jim_cacas_main():
    lineas = list(sys.stdin)
    matrix = []
    for linea in lineas[1:]:
        matrix.append([int(x) for x in linea.strip().split()])
        
    logger_cagada.debug("matrix leidas %s" % matrix)
    putlas = jim_cacas_core(matrix)
    
    putlas_str = " ".join([str(x[1]+1) for x in putlas])

    print(putlas_str)
if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    jim_cacas_main()
