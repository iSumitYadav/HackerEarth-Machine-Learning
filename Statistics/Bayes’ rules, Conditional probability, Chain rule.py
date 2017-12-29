# https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/bayes-rules-conditional-probability-chain-rule/tutorial/

pct = float(input())
pot = float(input())
n = int(input())
ans = (pct*2/n) + pot*(1-pct)
print('{0:.6f}'.format(round(ans, 6)))