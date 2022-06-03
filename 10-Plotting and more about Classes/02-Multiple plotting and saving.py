import pylab

pylab.figure(1)                     # creates figure 1
pylab.plot([1,2,3,4],[1,2,3,4])     # plots (1,1),(2,2) and so on
pylab.figure(2)                     # creates figure 2
pylab.plot([1,4,3,2],[5,6,7,8])     # plots (1,5),(4,6) and so on
pylab.savefig('Figure-Addie')       # saves figure 2 by the name 'Figure-Addie'

pylab.figure(1)                     # to add another plot in figure 1
pylab.plot([5,6,10,3])              # all the values denote y axis and by default the x axis will be whole numbers
pylab.savefig('Figure-Jane')        # saves figure 1 by the name 'Figure-Jane'
