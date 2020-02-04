# Conjunto de puntos discretos
xpt = [(0.0,0.0),(0.5,0.1),(0.6,-0.1),\
        (-0.1,0.2),(0.2,0.4),(0.1,0.8),\
        (0.6,0.4),(0.3,0.1),(0.5,0.6),\
        (0.1,0.2),(0.35,0.55),(0.,0.35),\
        (0.37,0.32),(0.02,0.13),(0.14,0.71)]
x,y = zip(*xpt)

# Anillo convexo
from scipy.spatial import ConvexHull
conv = ConvexHull(xpt)

# Crear graficos matplotlib
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#fig=plt.figure(figsize=(10,6))
#ax1 = fig.add_subplot(1,1,1)
plt.figure()
plt.axis('off')

# graficar dominio
plt.scatter(x,y,color='black')

# graficar dominio convexo
for pos in conv.simplices:
    xpos = [ x[pos[0]] , x[pos[1]] ]
    ypos = [ y[pos[0]] , y[pos[1]] ]
    plt.plot(xpos,ypos,color='green')
    plt.scatter(x[pos[0]],y[pos[0]],color='red')
    plt.scatter(x[pos[1]],y[pos[1]],color='red')

#fig.suptitle(r'Funcion de forma test '+test+' npts '+npts+\

#plt.subplots_adjust(left=0.125,bottom=0.1,right=0.9,top=0.9,wspace=0.2,hspace=0.2)


#ax1.text(0.01,0.75, r"Tolerancia solicitada : "+str(errtol0)+'\n'\


plt.savefig('./convex_example.pdf')
plt.savefig('../Imagenes/03/convex_example.pdf')
plt.show()
