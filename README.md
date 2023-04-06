# BOB

This project is carried out by a for students group in second year at ENSEA.

### Principal objectives

This project main goal is to realize a 5-axis robot arm. This robot is a prototype concive to help people with disabilities. 

### Requirement

This project is realized in collaboration with a clinique, and some decision were taken.
The robot need :

  * to draw its power supply from the grid
  * to be able to pick up something from the floor where he stand
  * to be connected at the wheelchair of the patient in bluetooth
  * to be controled by the bluetooth and by a touch interface
  * to be fixed on a table 

Some decision where also taken for some technical reasons.
The robot :

  * contain a raspberry PI 4, and a STM32
  * present a total of 3 servomotors ans 3 steppers

----------

# The realisation

### Mecanics

The majority of the parts are modeled on SOLIDWORKS, and printed in 3D by the school. The mecanical parts (rollings, belt,...) are bought on RScomponents.  
Some other parts are given by the mechanical workshop.

### Hardware

The hardware part is composed by 5 main devices :

 * The STM32
 * The Raspberry PI 4
 * The AC/DC converter
 * The power module
 * The driver module

All those devices are placed in the robot base and connected by cable to each other, and to other parts.  
The Raspberry is needed here because she offer wi-fi, bluetooth, serial connection, and good performances.  
STM32 is used because of his great ability to real time work, which is better for motor control.  
AC/DC converter take the 230V / 50Hz in input and comes out of 24V.  
The power module take the 24V, and divide it to provide 12V, 7.4V, 5V, and 3.3V.  
The driver module contain 4 driver for stepper.

### Software

### Raspberry code

### STM32 code


----------
### Matrix system





----------
here is the datasheet of the [driver](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2225_Datasheet_Rev1.11.pdf) for the steppers.  
here is the datasheet of the [servomotors](https://emanual.robotis.com/docs/en/dxl/x/xl320/).
