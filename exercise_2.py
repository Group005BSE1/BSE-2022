def return_investment(a, b, c, d ):
    return round((a * ((1 + b / d) ** (d * c))), 2)

C = float(input("Initial investment: "))
r = float(input("Rate: "))
t = float(input("time in years"))
n = float(input("No of times interest given per year: "))

print(return_investment(C, r , t, n))
