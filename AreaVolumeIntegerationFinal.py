from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

try:
    def getVolume():
        ad= integrate.quad(fn, l, u)
        print("Volume = " + str(round(np.pi*ad[0],3)))

        x = np.linspace(l, u, 600)
        eq= eval(fnin)
        revolve_steps = np.linspace(0, np.pi*2, 600).reshape(1,600)
        theta = revolve_steps
        eq_column = eq.reshape(600,1)
        z = eq_column.dot(np.cos(theta))
        y = eq_column.dot(np.sin(theta))
        xs, rs = np.meshgrid(x, eq)

        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        fig.tight_layout(pad = 0.0)
        ax.plot_surface(xs.T, y, z, color = 'blue', shade = True )
        plt.show()

    def getArea():
        
        ad= integrate.quad(fn, l, u)
        print("Area = " + str(round(ad[0],3)))
        
        x = np.linspace(l, u, num=1000)
        y = eval(fnin)

        plt.fill_between(x,y)
        plt.show()

    fnin= input("Function:")
    fn= lambda x: (eval(fnin))**2
    l= int(input("From:"))
    u= int(input("To:"))
    req= input( "1)Area Under curve...2) Volume due to rotation around X axis)" )

    if req == "1":
        getArea()
    elif req == "2":
        getVolume()
    else:
        print("Invalid Option")
except KeyboardInterrupt:
    quit()
