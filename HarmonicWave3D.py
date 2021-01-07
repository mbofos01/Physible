import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
def checkP(s):
    #print("run check p")
    k = 2222222222222222222
    if s.find("p") == 1 or s == "p" :
        s = s.replace("p"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.pi
        else:
            k = np.pi
    elif s.find("π") == 1 or s == "π":
        s = s.replace("π"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.pi
        else:
            k = np.pi

    #print(k)
    return k

def checkE(s):
    #print("run check e")
    k = 2222222222222222222
    if s.find("e") == 1 or s == "e":
        s = s.replace("e"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
        else:
            k = np.exp(1)

    #print(k)
    return k

def checkEP(s):
    #print("run check ep")
    k = 2222222222222222222
    if (s.find("pe") == 1 or s.find("ep") == 1) :
        #print("in here")
        s = s.replace("e"," ")
        s = s.replace("p"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
            k *= np.pi
        else:
            k = np.exp(1)*np.pi
    #print(k)
    return k

def check(s):

    flag = checkEP(s)
    if flag != 2222222222222222222:
        return flag
    flag = checkP(s)
    if flag != 2222222222222222222:
        return flag
    flag = checkE(s)
    if flag != 2222222222222222222:
        return flag


    if s.find(","):
    	s = s.replace(",",".")
    return float(s)

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [  [sg.Text('Enter A value:              '), sg.InputText('4')],
            [sg.Text('Enter T value:               '), sg.InputText('1')],
            [sg.Text('Enter λ value:               '), sg.InputText('0.5')],
            [sg.Button('Create Plot') ,sg.Button('Close Window'),sg.Text('By Michail-Panagiotis Bofos')]
           ]
# Create the Window
sg.theme("DarkTeal12")
window = sg.Window('Harmonic Wave 3D example', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
win2_active = False
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break

    if event in (None,'Create Plot'):
        win2_active = True
        layout2 = [
            [sg.Text('The second window'), sg.Text('', key='_OUTPUT_')],
            [sg.Input(do_not_clear=True, key='_IN_')],
            [sg.Button('Show'), sg.Button('Exit')]
            ]

        l = check(values[2])
        T =  check(values[1])
        A =  check(values[0])

        #X = list(np.linspace(0, maxx, 100))
        #t = list(np.linspace(0, maxt, 100))
        X = list(np.linspace(0, 2*l, 100))
        t = list(np.linspace(0, 2*T, 100))
        X, t = np.meshgrid(X, t)


        Z = A * np.sin(2*np.pi*(t/T + X/l))
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_wireframe(X, t, Z, rstride=1, cstride=1, cmap=cm.viridis)
        plt.show()



window.Close()
