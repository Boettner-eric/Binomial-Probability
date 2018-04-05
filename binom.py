import math

def nCk(n,k):
    f = math.factorial
    return f(n) // f(k) // f(n-k)

def binom_prob(n,k,p):
    bin = 0
    q = 1-p
    while k < n:
		bin += nCk(n,k) * q**(n-k) * p**k
		k += 1
    return bin

def main():
    k = input("Number of Successes      k - ")
    p = input("Probability of Success   p - ")
    while True: ## input validation (p is a probability < 1.0)
        if 1-p < 0:
            print("Invalid input")
            p = input("Probability of Success   p - ")
        else:
            break
    r = input("Odds of Winning          r - ")
    while True:
        if 1-r < 0:
            print("Invalid input")
            r = input("Winning probability      r - ")
        else:
            break
    n = 0
    while True:
        n += 1
        result = binom_prob(n,k,p)
        if result >= r:
            break
        if n > 10000: ## prevents infinite loops
            return none
    q = 1-p
    print(str(n) + " attempts with probability " + str(round(result,4)) + " >= " + str(r))
    print("\nLatex Equations")
    print(" $\sum\limits_{k=1}^{n}{n\choose k}\cdot q^{n-k}*p^{k} \geq r$")
    print(" $\sum\limits_{k="+str(k) +"}^{"+str(n)+"}{"+str(n)+"\choose k}\cdot "+str(q)+"^{"+str(n)+"-k}\cdot" + str(p)+"^{"+str(k) +"}\geq" + str(r)+"$")
main()
