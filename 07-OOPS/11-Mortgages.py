# To build a program that examines the costs of the three kinds of loans
# - Fixed rate mortgage with no points
# - Fixed rate mortgage with points and
# - A mortgage with an initial teaser rate followed by a higher rate for the duration.

# MORTGAGE BASE CLASS

def findPayment(loan,r,m):
    '''
    Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size loan at a monthly rate of r for m months
    '''
    return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage(object):
    '''
    Abstract class for building different kinds of mortgages
    '''
    def __init__(self,loan,annRate,months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None  # description of mortgage

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        # *return the total amount paid so far
        return sum(self.paid)

    def __str__(self):
        return self.legend

    '''
    NOTE: 
    - makePayment: used to record mortgage payments
    - part of each payment covers the amount of interest due on the outstanding loan balance and the remainder of the payment is used to reduce the loan balance.
    '''

class Fixed(Mortgage):
    def __init__(self,loan,r,months):
        Mortgage.__init__(self,loan,r,months)
        self.legend = 'Fixed'+str(round(r*100,2))+'%'

class FixedwithPts(Mortgage):
    def __init__(self,loan, r, months,pts):
        Mortgage.__init__(self,loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed'+str(round(r*100,2))+'%,'+str(pts)+' points'

class TwoRate(Mortgage):
    def __init__(self,loan,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self,loan,teaserRate,months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12;
        self.legend = str(teaserRate*100)+'% for '+str(self.teaserMonths)+' months,then '+str(round(r*100,2))+'%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths +1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],self.rate,self.months-self.teaserMonths)
        Mortgage.makePayment(self) 

#  * Now a function that computes and prints the total cost of each kind of mortgage for a sample set of parameters. Begins by creating mortgage of each kind. Then makes a monthly payment on each for a given number of years. Finally.prints the total amount of the payments made for each loan

def compareMortgages(amt,years,fixedRate,pts,ptsRate,varRate1,varRate2,varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt,fixedRate, totMonths)
    fixed2 = FixedwithPts(amt,fixedRate, totMonths,pts)
    twoRate = TwoRate(amt,varRate2,totMonths,varRate1,varMonths)
    morts = [fixed1,fixed2,twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
        for m in morts:
            print(m)
            print(' Total payments = $'+ str(int(m.getTotalPaid())))

compareMortgages(amt=200000,years=30,fixedRate=0.07,pts=3.25,ptsRate=0.05,varRate1=0.045,varRate2=0.095,varMonths=48)

'''
End Result

Fixed7.0%,3.25 points
 Total payments = $485517
4.5% for 48 months,then 9.5%
 Total payments = $551444
'''