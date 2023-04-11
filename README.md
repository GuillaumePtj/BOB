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

---------------

# The realisation

### Mecanics

 The majority of the parts are modeled on SOLIDWORKS, and printed in 3D by the school. The mecanical parts (rollings, belt,...) are bought on RScomponents.  
Some other parts are given by the mechanical workshop.  
Files are available in the Meca branch.

-----
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
All the PCB are designed on kiCad

![Untitled Diagram drawio(2)](https://user-images.githubusercontent.com/114493167/230955787-32642c2e-b8c4-4015-9b7a-c6681a64a51d.png)


-----
### Software

The Python code has been written on VSCode, and C code has been written on STM32CubeIDE.
All the codes are available in Code branch.

### Raspberry code

The Raspberry has already been configurate by activating SSH protocole and Wi-Fi.

**code actually runing into the robot**  
The raspberry and the STM communicate in UART. The raspberry sends the positioning data destined for a single motor to the STM with one single data frame of 7 bytes.
In order we have:  
Start of frame, engine number, engine angle, direction of rotation, rotation Speed, end of frame.
 
**Drafted but needs to be implemented later**  
We take the base of the first code except that this time we seek to direct the motors with the coordinates according to the X, Y, Z positions of our reference.
The frame sent is the following this time made of :  
Start of frame, Position along X and around X, Position along Y and around Y, Position along Z and around Z, End of frame.

More information in the "matrix" section


### STM32 code

Step to receive and use the data frame by UART :
- UART port binary speed: 9600  in interrupt mode 
- In CallBack function : Set a flag then receive the data frame into an integer array
- In the main function : We split the data written in the array
- Send the data to the motors

The datas received are : motor number, wanted angle, direction and speed.
The wrist and the gripper are controlled with servo motors. Shoulder and elbow are controlled by stepper motors.
When the robot is initialized, the servomotors move to their "central" position and their LEDs are green. After a short time they turn purple and the robot is ready to receive instructions.

**Direction control :** 

For both types of motors, the direction is a bit of 0 or 1. The only difference between the two types of motors is that the servos cannot be rotated indefinitely. For each direction it has an angle of action of 150°, so 300° in total.

### Direction of the motors in the state of the pins

Motor 1 (Clamp) : 
 * 0->close
 * 1->open
 * 
Motor 2 (Wirst_Z) : 
 * 0->left
 * 1->right

Motor 3 (Wirst_X) : 
 * 0 -> down
 * 1 -> up

Motor 4 (Elbow) : 
 * 0 -> up
 * 1 -> down
	
				 

-----
### Matrix system

Now that we are controlling the motors 1 by 1 by giving the angle command to each of the motors, it is time to control the motor in position. To put this into practice we have to go through a matrix system.  
The matrix system will allow us to find the angles that each motor must adopt for the robot to reach a desired position.

Ex :  
the Raspberry sends the following instructions to the STM:  
 * X Position
 * Y Position
 * Z Position
 * X orientation
 * Y orientation
 * Z orientation
 
 and with these instructions the robot should be able to get into the desired position.
 
It is necessary to establish the "direct geometric model" (this makes it possible to obtain the final position thanks to the angles of the given motors) and invert this model. In our case, we therefore use the "inverse geometric model" which makes it the opposite of the previous model: from a given position, the model calculates the angles for each motor and that is what we want.

What has already been done:

- The inverse geometry model has been established for the first 3 axes, the equations and the code have been written for the first 3 axes. All that's missing is to take into account the reduction ratios of each engine and add the factors in the code and then test the whole thing.

What remains to be done :

- Establish the inverse geometric model for the remaining 2 axes.

Good to know :

The inverse geometric model of the robot is done in two stages (position part and orientation part). The position part of the robot is done (part which manages the first 3 axes) and the orientation part (orientation of the gripper) which is managed by the remaining axes is to be done. For the resolution of the inverse geometry model of the last axes, it is necessary:

 1) establish the direct geometric model using the Denavit-Hartenberg method
 2) Inverse the model by using PAUL's method
 3) Once the equations of the remaining angles have been found, implement it in the STM
 
----------
### To go further

Some parts needs to be adapted, like the shoulder, the cable management, or the placement of the cards into the basement. 
The driver PCB doesn't work correctly, some debugging is needed.
The robot could be better with a last rotary axis, beetween the elbow and the wrist.  
The contrôle part as begun. But she is not implemented due to a bluetooth probleme and the fact that there is one articulation less.
The code in python need to work with interrupt so that we can use the Raspberry for interfacing while she send data frame.

----------
here is the datasheet of the [driver](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2225_Datasheet_Rev1.11.pdf) for the steppers.  
here is the datasheet of the [servomotors](https://emanual.robotis.com/docs/en/dxl/x/xl320/).  
here is the documentation for the [STM32](https://www.st.com/resource/en/datasheet/stm32l412kb.pdf).
