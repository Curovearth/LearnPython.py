import pylab

principal = 1000
interestRate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate

pylab.title('5% growth, compounded annually')
pylab.xlabel('Years of compounding')
pylab.ylabel('Value of principal')
pylab.plot(values)
pylab.savefig('03-compound growth')
pylab.show()
