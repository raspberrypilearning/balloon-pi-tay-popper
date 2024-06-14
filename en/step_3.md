## Test the button with code

Now we've connected a button, we'll activate it with some Python code.

- Open IDLE by clicking on **Menu** > **Programming** > **Python 3 (IDLE)** to open a Python shell.

- In this shell, go to `File -> New File` to open a new Python file.

- It's good practice to save this file before you type anything important. To save, go to `File -> Save As`, then type in `balloon.py` and click `Save`. Now you can get coding!

- Start by importing the `gpiozero` library. Write the following line in your Python file:

    ```python
    from gpiozero import Button
    ```

- Next, leave a new line space to separate your imports from your main code, and add a line to set up a button on pin 14:

    ```python
    button = Button(14)
    ```

- Now add the following lines:

    ```python
    print("Ready...")
    button.wait_for_press()
    print("Pop!")
    ```

    This will print "Ready", wait for the button to be pressed, and then print "Pop!" which will be the point when our balloon pops later!

- Save the code with `Ctrl + S` and run with `F5`. When you see `Ready...` on the screen, press the button, and you should see `Pop!` printed to the screen.

