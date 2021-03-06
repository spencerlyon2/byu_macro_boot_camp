X0=sp.array([[-.1,0.]])
Z0=-math.sqrt(.004)
Y0=0
Xbar=sp.mat([[ks,ls]])
Zbar=0
Mu=0
Var=.0004 #note shocks of .004 cause negative consumption
alpha=.4
delta=.1
reps=1000
T=250
GDP,I,C= MonteCarlo(P,Q,R,S,NN,X0,Y0,Z0,Xbar,Zbar,Mu,Var,alpha,delta,reps,T)


X0=sp.array([[0.,0.]])
shock=-.005
Y0=0
Xbar=sp.mat([[ks,ls]])
Zbar=0
alpha=.4
delta=.1
T=40
GDP_s, invest_s, consumption_s=impulseResponse(P,Q,R,S,NN,X0,Y0,shock,Xbar,Zbar,alpha,delta,T)

# <codecell>

P

# <codecell>

Q


# <codecell>

R

# <codecell>

S

# <codecell>

#Timothy Hills
#Correlation

import scipy as sp
from scipy import linalg as la
import sympy as sym
from sympy import symbols, nsolve, Symbol
import math
import numpy as np
from numpy.matlib import repmat
from RBCnumerderiv import numericalDerivatives

def Corr(GDP,I,C):
	m = sp.shape(GDP)[1]
	GDPIcorr = []
	GDPCcorr = []
	for i in range(0, m):
		gdp = GDP[:,i]
		inv = I[:,i]
		con = C[:,i]
		#Correlation between output and investment for each series
		gdpi = sp.corrcoef(gdp,inv)
		GDPIcorr.append(gdpi[0,1])
		#Correlation between output and consumption for each series
		gdpc = sp.corrcoef(gdp,con)
		GDPCcorr.append(gdpc[0,1])
	#Mean and standard deviation of correlation between GDP and
	#Investment and Consumption over total number of simulations
	GDPICORR = sp.array(GDPIcorr)
	gdpimean = sp.mean(GDPICORR)
	gdpistdev = sp.std(GDPICORR)
	GDPCCORR = sp.array(GDPCcorr)
	gdpcmean = sp.mean(GDPCCORR)
	gdpcstdev = sp.std(GDPCCORR)
	sp.savetxt('GDPICORR.csv',GDPICORR)
	sp.savetxt('GDPCCORR.csv',GDPCCORR)
	print "The mean and standard deviation between GDP and"
	print "Investment and GDP and Consumption followed by"
	print "The lists of each correlation coefficient for"
	print "each series are saved in csv files"
	return gdpimean, gdpistdev, gdpcmean, gdpcstdev

# <codecell>

#Timothy Hills
#Autocorrelation and Correlation
import scipy as sp
from scipy import linalg as la
import sympy as sym
from sympy import symbols, nsolve, Symbol
import math
import numpy as np
from numpy.matlib import repmat
from RBCnumerderiv import numericalDerivatives

def Autocorr(GDP,I,C):
	m = sp.shape(GDP)[1]
	GDPauto = []
	Iauto = []
	Cauto = []
	for i in range(0,m):
		#GDP autocorrelation coefficients for each series appended
		#to the empty GDPauto list
		gdp = GDP[:,i]
		gauto = sp.corrcoef(gdp[0:-1],gdp[1:])
		GDPauto.append(gauto[0,1])
		#Investment autocorrelation coefficients for each series
		#appended to the empty Iauto list
		invest = I[:,i]
		iauto = sp.corrcoef(invest[0:-1],invest[1:])
		Iauto.append(iauto[0,1])
		#Consumption autocorrelation coefficients for each series
		#appended to the empty Cauto list
		consum = C[:,i]
		cauto = sp.corrcoef(consum[0:-1],consum[1:])
		Cauto.append(cauto[0,1])
	#Calculate the mean and standard deviation of these moments
	#across the total number of simulations
	GDPAUTO = sp.array(GDPauto)
	gdpsimmean = sp.mean(GDPAUTO)
	gdpsimstdev = sp.std(GDPAUTO)
	IAUTO = sp.array(Iauto)
	isimmean = sp.mean(IAUTO)
	isimstdev = sp.std(IAUTO)
	CAUTO = sp.array(Cauto)
	csimmean = sp.mean(CAUTO)
	csimstdev = sp.std(CAUTO)
	sp.savetxt('GDPAUTO.csv',GDPAUTO)
	sp.savetxt('IAUTO.csv',IAUTO)
	sp.savetxt('CAUTO.csv',CAUTO)
	print "GDP/Investment/Consumption Simulations Mean/Standard Deviation"
	print "of Autocorrelation. The Autocorrelation Coefficients"
	print "of GDP,Investment,Consumption for each series have been saved"
	print "separately in csv files"
	return gdpsimmean, gdpsimstdev, isimmean, isimstdev, csimmean, csimstdev

# <codecell>

Autocorr(GDP,I,C)
Corr(GDP,I,C)

# <codecell>


# <codecell>
