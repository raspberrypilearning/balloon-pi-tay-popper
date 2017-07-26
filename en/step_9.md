## Add the balloon to the code

Now we've completed our circuit we'll need to change our code to trigger the transistor, allowing current to flow through the resistor, which will pop the balloon.

- First, you're going to need an `OutputDevice` to trigger the transistor, and you'll need the `sleep` method from the `time` library.  Add `OutputDevice` and import the `sleep` method at the beginning of your code:

    ```python
	from gpiozero import Button, OutputDevice
	from time import sleep
	```

- Where you previously declared `button = 14`, add a line to declare `balloon = 2`:

    ```python
    button = Button(14)
    balloon = OutputDevice(2)
    ```

   This will designate GPIO 2 as what we'll use to pop the balloon.

- Now comes the code to pop the balloon. Earlier, we used `button.wait_for_press()` to wait for a button press, then we just printed `Pop!`. Add the following lines before the `Pop!` line:

    ```python
    balloon.on()
    sleep(10)
    balloon.off()
    ```

    This means "Turn the balloon pin on for 10 seconds, then turn it off".
    
    Depending on the thickness of your balloon and how much it has been blown up and stretched, this may take five seconds or more. If your balloon does not pop, you can increase the length of the `sleep` time accordingly.

- Now save your code with `Ctrl + S`, check everything's wired up as it should be, then run your code with `F5`. When you see `Ready...`, press the button and your balloon should burst!

