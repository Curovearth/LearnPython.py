import pylab
class Mortgage(object):                                         
    '''
    Abstract class for building different kinds of mortgages                                                                                            
    '''
    def __init__(self,loan,annRate, months):
        self.loan = loan                                                   
        self.annRate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]                            
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1]-reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend
    
    def plotPayments(self,style):
        pylab.plot(self.paid[1:],style,label=self.legend)

    def plotBalance(self,style):
        pylab.plot(self.outstanding,style,label=self.legend)

    def plotTotPd(self,style):
        totPd = [self.paid[0]]
        for i in range(1,len(self.paid)):
            totPd.append(totPd[-1]+self.paid[i])
        pylab.plot(totPd,style,label=self.legend)

    def plotNet(self,style):
        totPd = [self.paid[0]]
        for i in range(1,len(self.paid)):
            totPd.append(totPd[-1]+self.paid[i])
        pylab.plot(totPd,style,label=self.legend)
        equityAcquired = pylab.array([self.loan]*len(self.outstanding))
        equityAcquired = equityAcquired - pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net,style,label=self.legend)