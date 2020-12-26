import sys
import matplotlib.pyplot as plt
import numpy as np
import math
def checkP(s):
    print("run check p")
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

    print(k)
    return k

def checkE(s):
    print("run check e")
    k = 2222222222222222222
    if s.find("e") == 1 or s == "e":
        s = s.replace("e"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
        else:
            k = np.exp(1)

    print(k)
    return k

def checkEP(s):
    print("run check ep")
    k = 2222222222222222222
    if (s.find("pe") == 1 or s.find("ep") == 1) :
        print("in here")
        s = s.replace("e"," ")
        s = s.replace("p"," ")
        if len(s) != 1:
            k = float(s)
        if len(s) != 1:
            k *= np.exp(1)
            k *= np.pi
        else:
            k = np.exp(1)*np.pi
    print(k)
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
    return float(s)

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [  [sg.Text('Enter plots name:   '), sg.InputText()],
            [sg.Text('Enter Axis X name: '), sg.InputText()],
            [sg.Text('Enter Axis Y name: '), sg.InputText()],
            [sg.Text('Enter max ω value:       '), sg.InputText()],
            [sg.Text('Enter m value:       '), sg.InputText()],
            [sg.Text('Enter F0 value:       '), sg.InputText()],
            [sg.Text('Enter k ω value:       '), sg.InputText()],
            [sg.Text('Enter b1 value:       '), sg.InputText()],
            [sg.Text('Enter b2 value:       '), sg.InputText()],
            [sg.Text('Enter b3 value:       '), sg.InputText()],
            [sg.Button('Create Plot')],[sg.Button('Close Window')]
           ]
# Create the Window
sg.theme("DarkTeal12")
window = sg.Window('Degressive Oscillation', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break

    if event in (None,'Create Plot'):
        how_many = len(values)
        maxx = check(values[3])
        t2 = np.arange(0.0, maxx, 0.02)
        fig = plt.figure()
        plt.Axes.set_frame_on
        first = 1
        second = 8
        third = 9
        Fo = check(values[5])
        m = check(values[4])
        k = check(values[6])
        b = check(values[7])
        if values[8] != '':
            b1 = check(values[8])
        if values[9] != '':
            b2 = check(values[9])

        ##################################### api-ms-win-core-path-l1-1-0.dll
        #define the function you want to draw
        def f(w,b):
            return (Fo/m)/((w*w - k/m)*(w*w - k/m) + (b*w/m)*(b*w/m) )
        #####################################
        text = "B:{}"
        plt.title((values[0]))
        plt.plot(t2, f(t2,b) )
        if values[8] != '':
            plt.plot(t2, f(t2,b1), color = 'red' )
        if values[9] != '':
            plt.plot(t2, f(t2,b2), color = 'green' )

        #####################################
        plt.ylabel((values[1]))
        plt.xlabel((values[2]))
        plt.grid(True)
        ax = fig.add_subplot(1, 1.0, 1)



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
        if values[8] != '':
            plt.legend([text.format(b),text.format(b1)], loc='best')
        if values[9] != '':
            plt.legend([text.format(b),text.format(b1),text.format(b2)], loc='best')
        plt.show()

window.Close()
