# python_project
This is a Python program that calculates the efficiency of a transformer. The program uses the tkinter library to create a graphical user interface (GUI) that allows users to input the transformer's rating, power factor, copper loss, and iron loss. Once the user clicks the "Calculate" button, the program calculates the transformer's efficiency using the following formula:
Efficiency = (Rating * Power Factor) / (Rating * Power Factor + Copper Loss + Iron Loss) * 100
The program then displays the efficiency in the GUI.
The program creates an instance of the Tk class and initializes the GUI elements using the MyWindow class. The add() method is called when the "Calculate" button is clicked, which extracts the input values from the GUI, performs the calculation, and displays the result in the GUI.
Overall, this program provides a simple and user-friendly way to calculate the efficiency of a transformer, and it can be used by engineers or technicians working in the electrical or electronics industry
