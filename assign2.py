#Write new code:
#1. Write code that calculates the daily cumulative returns for a portfolio composed of 30% XOM and 70% GOOG. Create a figure that shows the cumulative returns for XOM, GOOG, and your new portfolio, call it XOMGOOGport.pdf
#2. Write code that calculates the correlation between the daily returns of two stocks, creates a scatter plot, and fits a line to the data. Be sure that the slope of the line is displayed on the figure. Run this code for SPY vs XOM, SPY vs GOOG, and SPY vs GLD. Call these files SPYvXOM.pdf, SPYvGOOG.pdf, SPYvGLD.pdf 


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import datetime as dt

data = np.loadtxt('ex.csv',delimiter=',',skiprows=1)
pricedat = data[:,3:]
datesdat = np.int_(data[:,0:3])
pricesnames = ['SPY','XOM','GOOG','GLD']

dates = []
for i in range(0,datesdat.shape[0]):
        dates.append(dt.date(datesdat[i,0],datesdat[i,1],datesdat[i,2]))

dailyrets=()
dailyrets=((pricedat[1:,:]/pricedat[0:-1,:])-1)
dates[0:1]=[]

daily_cum_ret=()
daily_cum_ret=dailyrets+1

for i in range(1,size(dailyrets[:,1])):
	daily_cum_ret[i]=daily_cum_ret[i-1,:] * (1 + dailyrets[i])


#----calculates the daily cumulative returns for a portfolio composed of 30% XOM and 70% GOOG-----

portfolio_daily_rets=0.30 * daily_cum_ret[:,1] + 0.70 * daily_cum_ret[:,2]
plt.clf()
pricesnames = ['XOM','GOOG','New portfolio']
plt.plot(dates,daily_cum_ret[:,1],'r')
plt.plot(dates,daily_cum_ret[:,2],'g')
plt.plot(dates,portfolio_daily_rets,'b')
plt.legend(pricesnames)
plt.ylabel('Cumulative Daily returns')
plt.xlabel('Date')
savefig("XOMGOOGport.pdf", format='pdf')


#------calculates the correlation between the daily returns of SPY and XOM-------------
plt.clf()
plt.scatter(dailyrets[:,0],dailyrets[:,1],c='green')
polycoeffs = np.polyfit(dailyrets[:,0],dailyrets[:,1], 1)
y = np.polyval(polycoeffs, dailyrets[:,0])
plt.plot(sort(dailyrets[:,0]),sort(y),'r-')
pricesnames = ['corr=' + str('%.3f' % (polycoeffs[0],)),'SPY vs XOM']
plt.legend(pricesnames)
savefig("SPYvsXOM.pdf", format='pdf')

#------calculates the correlation between the daily returns of SPY and GOOG-------------
plt.clf()
plt.scatter(dailyrets[:,0],dailyrets[:,2],c='green')
polycoeffs = np.polyfit(dailyrets[:,0],dailyrets[:,2], 1)
y = np.polyval(polycoeffs, dailyrets[:,0])
plt.plot(sort(dailyrets[:,0]),sort(y), 'r-')
pricesnames = ['corr=' + str('%.3f' % (polycoeffs[0],)),'SPY vs GOOG']
plt.legend(pricesnames)
savefig("SPYvsGOOG.pdf", format='pdf')

#------calculates the correlation between the daily returns of SPY and GLD-------------
plt.clf()
plt.scatter(dailyrets[:,0],dailyrets[:,3],c='green')
polycoeffs = np.polyfit(dailyrets[:,0],dailyrets[:,3], 1)
y = np.polyval(polycoeffs, dailyrets[:,0])
plt.plot(sort(dailyrets[:,0]),sort(y), 'r-')
pricesnames = ['corr=' + str('%.3f' % (polycoeffs[0],)),'SPY vs GLD']
plt.legend(pricesnames)
savefig("SPYvsGLD.pdf", format='pdf')

