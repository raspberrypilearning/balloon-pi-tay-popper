## Test the button with code

Now we've connected a button, we'll activate it with some Python code.

---- task ---

Open Thonny by clicking on **Menu** > **Programming** > **Thonny**

--- /task ---

---- task ---

To save, go to `File -> Save As`, then type in `balloon.py` and click `Save`. Now you can get coding!

--- /task ---

---- task ---

Start by importing the `gpiozero` library. Write the following line in your Python file:

```python
from gpiozero import Button
```

--- /task ---

---- task ---


- Next, leave a new line space to separate your imports from your main code, and add a line to set up a button on pin 14:

```python
button = Button(14)
```

--- /task ---

---- task ---

Now add the following lines:

```python
print("Ready...")
button.wait_for_press()
print("Pop!")
```

This will print "Ready", wait for the button to be pressed, and then print "Pop!" which will be the point when our balloon pops later!

Click **Run** to see `Pop!` being printed.
--- /task ---

