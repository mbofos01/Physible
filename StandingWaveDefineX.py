import sys
import matplotlib.pyplot as plt
import numpy as np
import math

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

layout = [  [sg.Text('Enter plots name:         '),sg.InputText('Standing Wave define x example')],
            [sg.Text('Enter Axis X name:       '), sg.InputText('X Axis')],
            [sg.Text('Enter Axis Y name:      '), sg.InputText('Y Axis')],
            [sg.Text('Enter A value:               '), sg.InputText('4')],
            [sg.Text('Enter T value:               '), sg.InputText('1')],
            [sg.Text('Enter x value:               '), sg.InputText('0.2')],
            [sg.Text('Enter λ value:               '), sg.InputText('0.6')],

            [sg.Button('Create Plot'),sg.Button('Close Window'),sg.Text('By Michail-Panagiotis Bofos')]
           ]
# Create the Window
sg.theme("DarkTeal12")
window = sg.Window('Standing Wave define x example', layout).Finalize()
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


        name = values[0]
        A =  check(values[3])
        #print(A)
        #print("AS")
        T =  check(values[4])
        x =  check(values[5])
        l =  check(values[6])
        max_t = 2*T
        yAx = values[2]
        xAx = values[1]
        t2 = np.arange(0.0, max_t,0.002) #max value
        fig = plt.figure()
        plt.Axes.set_frame_on

            #####################################
            #define the function you want to draw
        def f(t):
            return 2 * A * np.sin((2*np.pi*x)/l) * np.cos((2*np.pi*t)/T)
                #####################################


        plt.title(name)
        plt.plot(t2, f(t2) )
        ax = fig.add_subplot(1, 1, 1)

            #####################################
        plt.ylabel(yAx)
        plt.xlabel(xAx)
        plt.grid(True)
        #####################################
            #spine placement data centered
        ax.spines['left'].set_position(('data', 0.0))
        ax.spines['bottom'].set_position(('data', 0.0))
           # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.show()




window.Close()
