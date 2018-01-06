import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol


def f1(x):
    return (2*x-16)/-2.0
def f2(x):
    return (x-12)/-2.0
def f3(x):
    return (4*x- 28)/-2.0
def moveon(event):
    plt.close()



def G1():
        fig = plt.figure()
        x = np.linspace(0,20,500)
        F = fig.add_subplot(111)
        F.plot(x,f1(x),'--')
        cid = fig.canvas.mpl_connect('key_press_event', moveon)
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.show()

def G2():
        fig = plt.figure()
        x = np.linspace(0,20,500)
        F = fig.add_subplot(111)
        F.plot(x,f1(x),'--')
        F.plot(x,f2(x),'--')
        cid = fig.canvas.mpl_connect('key_press_event', moveon)
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.show()
        
def G3():
        fig = plt.figure()
        x = np.linspace(0,20,500)
        F = fig.add_subplot(111)
        F.plot(x,f1(x),'--')
        F.plot(x,f2(x),'--')
        F.plot(x,f3(x),'--')
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        cid = fig.canvas.mpl_connect('key_press_event', moveon)
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.show()
       
def G4():
        fig = plt.figure()
        x = np.linspace(0,20,500)
        F = fig.add_subplot(111)
        F.plot(x,f1(x),'--')
        F.plot(x,f2(x),'--')
        F.plot(x,f3(x),'--')
        X = [0,7,6,4,0,0]
        Y = [0,0,2,4,6,0]
        plt.fill([0,7,6,4,0,0],[0,0,2,4,6,0],'red')
        plt.plot(X,Y)
        for xy in zip(X, Y):                                    
            F.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
            
        cid = fig.canvas.mpl_connect('key_press_event', moveon)
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.show()
try:
    G1()
    G2()
    G3()
    G4()
except KeyboardInterrupt :
    exit()
