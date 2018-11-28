#Install packages
import pandas as pd
import numpy as np
import scipy
from scipy.optimize import minimize
import scipy.integrate as spint
from scipy.stats import norm
from scipy.stats import chi2
from scipy import stats
from plotnine import *
! pip install scikit-misc

#Creating model and parameters
def rosenmacSim(y,t,b,e,s,w,d,a,H,P):
# "unpack" lists containing state variables (y)
    H=y[0]
    P=y[1]
#Calculate change in state variables with time, give parameter values and current value of state variables
    dHdt=(b*H*(1-(a*H)))-(w*P*(H/(d+H)))
    dPdt=(e*w*P*(H/(d+H)))-(s*P)
#Return list containing change in state variables with time
    return [dHdt, dPdt]

#Define parameters, initial values for state variables, and time steps
params=(0.8,0.07,0.2,5,400,0.001,500,120)
y0=[0.5,0.5]
times=range(0,500)
sim=spint.odeint(func=rosenmacSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"Time":times,"Hare":sim[:,0],"Lynx":sim[:,1]})
ggplot(simDF,aes(x="Time",y="Hare"))+geom_line()+geom_line(simDF,aes(x="Time",y="Lynx"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
