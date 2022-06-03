import pylab

principal = 1000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate

pylab.plot(values,linewidth = 30)
pylab.title('5% Growth, Compounded Annually',fontsize='xx-large')
pylab.xlabel('Years of compounding',fontsize='x-small')
pylab.ylabel('Value of principal ($)')
pylab.savefig('04-Strange looking plot')
pylab.show()
