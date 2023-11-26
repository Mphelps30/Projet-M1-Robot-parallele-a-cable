import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def afficher_schema(x, y, teta):
    ax1 = -4; ax2 = 4; ax3 = 4; ax4 = -4
    ay1 = 4; ay2 = 4; ay3 = -4; ay4 = -4
    bx1 = -0.5; bx2 = 0.5; bx3 = 0.5; bx4 = -0.5
    by1 = 0.5; by2 = 0.5; by3 = -0.5; by4 = -0.5

    # Matrices symboliques
    rteta = sp.Matrix([[sp.cos(teta), -sp.sin(teta), 0], [sp.sin(teta), sp.cos(teta), 0], [0, 0, 1]])
    p = sp.Matrix([[x, x, x, x], [y, y, y, y], [0, 0, 0, 0]])
    ai = sp.Matrix([[ax1, ax2, ax3, ax4], [ay1, ay2, ay3, ay4], [0, 0, 0, 0]])
    bi = sp.Matrix([[bx1, bx2, bx3, bx4], [by1, by2, by3, by4], [0, 0, 0, 0]])
    B = p + rteta @ bi

    # Calcul de la distance symbolique
    r = (ai[0, :] - B[0, :]).applyfunc(lambda element: element**2) + (ai[1, :] - B[1, :]).applyfunc(lambda element: element**2)

    # Calcul de la longueur symbolique
    li = r.applyfunc(lambda elem: sp.sqrt(elem))
    Li = np.transpose(li)

    # Calcul de W matrice jacobienne transposée
    W = -np.transpose(B - ai) / Li

    # Calcul de l'angle de Tau
    aii = np.array(ai)
    bii = np.array(B)
    ABy = np.array(aii[1, :] - bii[1, :])
    ABx = np.array(aii[0, :] - bii[0, :])
    alpha = [sp.atan2(aby, abx) for aby, abx in zip(ABy, ABx)]

    # Coordonnées de la ligne l1
    x_l1 = [ai[0, 0], B[0, 0]]
    y_l1 = [ai[1, 0], B[1, 0]]

    # Coordonnées de la ligne l2
    x_l2 = [ai[0, 1], B[0, 1]]
    y_l2 = [ai[1, 1], B[1, 1]]

    # Coordonnées de la ligne l3
    x_l3 = [ai[0, 2], B[0, 2]]
    y_l3 = [ai[1, 2], B[1, 2]]

    # Coordonnées de la ligne l4
    x_l4 = [ai[0, 3], B[0, 3]]
    y_l4 = [ai[1, 3], B[1, 3]]

    # Coordonnées pour relier les points B et former le rectangle
    x_rect = [B[0, 0], B[0, 1], B[0, 2], B[0, 3], B[0, 0]]
    y_rect = [B[1, 0], B[1, 1], B[1, 2], B[1, 3], B[1, 0]]

    # Affichage des points fixes (A1,A2,A3,A4)
    plt.scatter(ai[0, :], ai[1, :], color='red')

    # Affichage des points fixes (B1,B2,B3,B4)
    plt.scatter(B[0, :], B[1, :], color='red')

    for i in range(4):
        plt.text(ai[0, i], ai[1, i], f'a{i+1}', color='green')
        plt.text(B[0, i], B[1, i], f'b{i+1}', color='black')

    # Afficher le point central (x,y)
    plt.scatter(x, y, color='blue')

    # Affichage des lignes
    plt.plot(x_l1, y_l1, linestyle='dashed', color='gray')
    plt.plot(x_l2, y_l2, linestyle='dashed', color='gray')
    plt.plot(x_l3, y_l3, linestyle='dashed', color='gray')
    plt.plot(x_l4, y_l4, linestyle='dashed', color='gray')

    # Relier les points B pour former le rectangle
    plt.plot(x_rect, y_rect, linestyle='solid', color='black')

    # Affichage des longueurs au milieu des câbles
    for i in range(4):
        xmilieu = (B[0, i] + ai[0, i]) / 2
        ymilieu = (B[1, i] + ai[1, i]) / 2
        plt.text(xmilieu, ymilieu, f'{li[i]:.2f}', color='blue', fontsize=8, ha='center', va='center')

    # Affichage de la matrice des longueurs sur la console
    print("Matrice des longueurs des câbles L :\n", Li)
    
    plt.title("Schéma robot parallèle à câbles")

    plt.show()

# Réglages de x,y et teta
nouveau_x = 0
nouveau_y = 0
angle_rotation = np.radians(0)
afficher_schema(nouveau_x, nouveau_y, angle_rotation)
