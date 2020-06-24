import argparse
import ast

parser = argparse.ArgumentParser(description= 'Cyclic Rotation')
parser.add_argument('a',  help='input an array', type=ast.literal_eval)
parser.add_argument('--k', help='number of times the numbers will get shifted', default=0, type=int)

args = parser.parse_args()

A = args.a
K = args.k

def solution(A, K):
    
    if len(A) != 0:
        standardize = K % len(A)
        new = A[-(standardize):] + A[:-(standardize)]
            
    else:
        new = A
        
    return new

if __name__ == '__main__':
	print('Here is the solution: ', solution(A,K))
