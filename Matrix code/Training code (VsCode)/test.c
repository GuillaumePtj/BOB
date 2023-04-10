/**

@file main.c
@brief Ce programme calcule les angles q1, q2, q3 d'un bras robotique en fonction de sa position spatiale.
@author [Carton Clément]
*/

#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

/**

@brief Cette fonction calcule les angles q1, q2, q3 en fonction d'une position donnée.
@param position un tableau contenant les coordonnées de la position spatiale du bras robotique
@param degres un tableau où seront stockées les valeurs des angles q1, q2 et q3 en degrés
@return void
*/

void position2deg(int position[], int degres[]){
    int px = position[0];
    int py = position[1];
    int pz = position[2];

    int q1, q2, q3;

    int d1 = 50.0;
    int d2 = 300.0;
    int d3 = 200.0;

    //calcul de l'angle q1
    q1 = atan2f(py,px);

    //calcul de l'angle q2 q3
    int z1 = cosf(q1)*px + sinf(q1)*py;
    int z2 = pz - d1;
    q2 = atan2(sqrt(1.0-(pow((pow(z1,2)+pow(z2,2)-pow(d2,2)-pow(d3,2))/(2*d2*d3),2))),(pow(z1,2)+pow(z2,2)-pow(d2,2)-pow(d3,2))/(2*d2*d3));

    int b1 = d2+d3*cos(q2);
    int b2 = d3*cos(q2);

    q3 = atan2((b1*z2-b2*z1)/(pow(b1,2)+pow(b2,2)),(b1*z1+b2*z2)/(pow(b1,2)+pow(b2,2)));

    //convertion des angles en degres 
    int pi = 3.15;
    degres[0] = q1*(180.0 / pi);
    degres[1] = q2*(180.0 / pi);
    degres[2] = q3*(180.0 / pi);
}

int main(){
    int position[3]={-50,-150,150};
    int degres[3];

    position2deg(position, degres);

    printf("q1 = %d°\n", degres[0]);
    printf("q2 = %d°\n", degres[1]);
    printf("q3 = %d°\n", degres[2]);

    int a = cos(2);

    return 0;
}

