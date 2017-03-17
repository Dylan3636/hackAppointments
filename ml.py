import pandas as pd
import numpy as np
import sklearn as sk
from scipy import *

def pmf(data,y):
    return np.exp(data[y.Gender][y.Age-6][y.DayOfTheWeek])
def getData(obvs,y):
    database.getFreq(obvs,y,['Appointments'])


raw_data = pd.read_csv('Desktop/No-show-Issue-300k.csv',';')
still_raw_data=raw_data.iloc[:,[0,1,2,4,5]]
val = only_show_up_raw.AppointmentRegistration.apply(lambda x:  x.split('T'))
mat1 = only_show_up_raw.apply(lambda x : np.array(x)).values
hms = m.apply(lambda x: np.array(x[0].split(':')))

f_data = mat[mat[:,1]=='F'] 
m_data = mat[mat[:,1]!='F'] 
y_f = hms[mat[:,1]=='F']
y_m = hms[mat[:,1]!='F']

y_f=[ max(int(x[0])-6,0) if (int(x[1])/30)>0  else max(int(x[0])-7,0) for x in y_f.values]
y_m=[ max(int(x[0])-6,0) if int(x[1])/30>0  else max(int(x[0])-7,0) for x in y_m.values]