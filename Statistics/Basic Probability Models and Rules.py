'''
https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/basic-probability-models-and-rules/tutorial/
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
pmb = float(input())
pab = float(input())
p1 = float(input())

prs = p1*(pmb*(1-pab) + pab*(1-pmb))
print('{0:.6f}'.format(prs))