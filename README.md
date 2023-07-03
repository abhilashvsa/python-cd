# python-cd
python function overview
Explanation:

First, we define a function called calculator() that will handle the calculator operations.

Inside the function, we display a welcome message to the user.

We ask the user to input two numbers and store them in variables num1 and num2. We convert the input to float so that decimal numbers can be entered.

Next, we display the available operations to the user.

We ask the user to enter the operation number (1 for addition, 2 for subtraction, etc.) and store it in the choice variable.

Based on the user's choice, we perform the selected operation using conditional statements (if, elif, else).

For each operation, we calculate the result and store it in the result variable. We also store the corresponding operator symbol (+, -, *, /) in the operator variable.

If the user chooses division, we check if the second number is not zero before performing the division operation. If the second number is zero, we display an error message and return from the function using the return statement.

If the user enters an invalid operation choice, we display an error message and return from the function.

Finally, we print the result using the print() function, formatting the output to display the input numbers, operator, and result in a readable format.

Outside the function, we call calculator() to start the program.

To use the calculator, simply run the Python script and follow the instructions displayed on the screen. Enter the numbers, select the operation, and the program will calculate and display the result.
