import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sympy as sp


# Définition des symboles
# ax1, ax2, ax3, ax4 = sp.symbols("ax1 ax2 ax3 ax4")
# ay1, ay2, ay3, ay4 = sp.symbols("ay1 ay2 ay3 ay4")
# bx1, bx2, bx3, bx4 = sp.symbols("bx1 bx2 bx3 bx4")
# by1, by2, by3, by4 = sp.symbols("by1 by2 by3 by4")
# rteta, teta = sp.symbols("rteta teta")
# x, y = sp.symbols("x y")
ax1=-4;ax2=4;ax3=4;ax4=-4
ay1=4;ay2=4;ay3=-4;ay4=-4
bx1=-0.5;bx2=0.5;bx3=0.5;bx4=-0.5
by1=0.5;by2=0.5;by3=-0.5;by4=-0.5
teta=0
x=0;y=0
# Matrices symboliques
# Matrice rotationnel
rteta = sp.Matrix([[sp.cos(teta), -sp.sin(teta), 0], [sp.sin(teta), sp.cos(teta), 0], [0, 0, 1]])
# Coordonnée du repère mobile p
p = sp.Matrix([[x,x,x,x], [y,y,y,y], [0,0,0,0]])
ai = sp.Matrix([[ax1, ax2, ax3, ax4], [ay1, ay2, ay3, ay4], [0, 0, 0, 0]])
bi = sp.Matrix([[bx1, bx2, bx3, bx4], [by1, by2, by3, by4], [0, 0, 0, 0]])
B = p + rteta @ bi #@ produit matricielle
print(B)
# Calcul de la distance symbolique
r = (ai[0, :] - B[0, :]).applyfunc(lambda element: element**2) + (ai[1, :] - B[1, :]).applyfunc(lambda element: element**2)
print("\n\n\nDistance r:\n\n", r)
# Calcul de la longueur symbolique
li = r.applyfunc(lambda elem: sp.sqrt(elem))
Li=np.transpose(li)
print("\n\n\nLongueur li:\n\n", Li)


# Calcul de W matrice jacobienne transposée

W=-np.transpose(B-ai)/Li
print("\n\n\nMatrice W:\n\n", W)

# Calcul de l'angle de Tau

#alpha = sp.symbols("alpha")

aii=np.array(ai)
bii=np.array(B)
ABy=np.array(aii[1, :] - bii[1, :])
ABx=np.array(aii[0, :] - bii[0, :])
#alpha=np.arctan2(ABy,ABx)*180
#alpha = ((ai[1, :] - B[1, :])/(ai[0, :] - B[0, :])).applyfunc(lambda le: sp.atan2(le,0))
alpha = [sp.atan2(aby, abx) for aby, abx in zip(ABy, ABx)]# print("\n\n\nAlpha :\n\n", alpha)

print("\n\n\nAngle alpha en rad:\n\n", alpha)
print("\n\n\nAngle alpha en degrés:\n\n", [float(sp.deg(a.evalf())) for a in alpha])
# angle_radians = alpha

# # Évaluation numérique
# angle_numerical = sp.N(angle_radians)

# print("\n\n\nAngle en radians:\n\n", angle_radians)
# print("\n\n\nAngle en degrés:\n\n", sp.deg(angle_numerical))



# Coordonnées de la ligne l1
x_l1 = [ax1,-ax1-li[0]]
y_l1 = [ay1,by1]

# # Coordonnées de la ligne l2
x_l2=[ax2,li[1]-ax2]
y_l2=[ay2,by2]

# # Coordonnées de la ligne l3
x_l3=[ax3,li[2]-ax3]
y_l3=[ay3,by3]

# # Coordonnées de la ligne l4
x_l4=[ax4,-ax4 - li[3]]
y_l4=[ay4,by4]


# Affichage des points fixes (A1,A2,A3,A4)
plt.scatter(ax1,ay1, color='red')
plt.scatter(ax2,ay2, color='red')
plt.scatter(ax3,ay3, color='red')
plt.scatter(ax4,ay4, color='red')

# Affichage des points fixes (B1,B2,B3,B4)
plt.scatter(bx1,by1, color='red')
plt.scatter(bx2,by2, color='red')
plt.scatter(bx3,by3, color='red')
plt.scatter(bx4,by4, color='red')


plt.text(ax1,ay1, "a1",color="green")
plt.text(ax2,ay2, "a2",color="green")
plt.text(ax3,ay3, "a3",color="green")
plt.text(ax4,ay4, "a4",color="green")

# Afficher le point centrale 0(x,y)
plt.scatter(x,y, color='blue')



# Afficher la ligne
plt.plot(x_l1, y_l1)
plt.plot(x_l2, y_l2)  
plt.plot(x_l3, y_l3)
plt.plot(x_l4, y_l4)  


