# Balloon Pi-tay Popper

To pop balloons use may usually a pin. Here you'll be doing the same, but using a GPIO 'Pin' on your Raspberry Pi, not the pin you might be thinking of!

## Set Up the Balloon Poppers

We're going to be using resistors to make the balloons pop. Resistors are electrical components that reduce the current flowing around a circuit, and in doing so they sometimes get hot. You're going to be taking advantage of this heat and deliberately over-heating a resistor in order to pop a balloon. But, before you can do that you need to wire up the resistor:

1. Inflate a balloon so it's nice and full, then tie a knot in it.

1. Take a 2metre length of 2 core speaker cable and strip both ends of both cores, so that the bare wire is visible. This can be done with wire strippers or (very carefully) with scissors (make sure that you only cut through the insulation and not the wires themselves). You can also split the two cores of the cable a little simply by pulling them apart. At one end of the cable, wrap red electrical tape around one wire (not the part with the exposed wire), and black electrical tape around the other. This is just to label them for later.

1. Take a 12R resistor and the ends of the speaker cable without electrical tape around them. Twist one wire of the cable around one wire coming from the resistor and the other wire around the remaining wire coming from the resistor (it doesn't matter which wire is connected to which).

    Make sure that there is a firm connection, you can even wrap electrical tape around the twisted wire to ensure it stays in place.

1. Now, take some more electrical tape (is doesn't matter what colour) and tape the resistor firmly onto the most stretched part of the balloon (that's the balloon's side, see picture). It's important that this resistor is firmly touching the balloon, so stick it on carefully.

1. Now tie some string onto the knot of your balloon and hang it from the ceiling using tape or tack.

## Wire Up the Low Voltage Circuit

The voltage of a circuit is the amount of 'push' the current has; a higher voltage provides a bigger push, which usually results in more current flowing in the circuit. Here, in order to make the resistors hot enough to pop the balloons, we need to run a higher current through them than the voltage on the Raspberry Pi can provide, and to do this we'll use what's called a Transistor.

A Transistor allows you to 'amplify' a circuit, as they can be switched 'on' by a low voltage circuit, and once 'on' they allow a higher voltage circuit to flow, but it's important that they're wired up correctly.

1. Hold your transistor up and you'll see that it's a semi-circle shape, with three leads coming out the bottom, each of these leads has a different name and role. Hold the transistor with the flat side facing towards you and from left to right the leads are called the Collector, the Base and the Emitter. The middle lead (the Base) controls the transistor and if it receives a signal (a small voltage) it turns the transistor 'on',  allowing current (from a higher voltage circuit) to flow between the Collector (on the left) and the Emitter (on the right).

    [Note: this is true for P2N2222A transistor, but others transistors may have their leads in different positions]

    Pic. like this:

    ![]()

1. Now you know which lead is which, we need to wire up the transistor; gently separating the leads will help with this. Carefully insert the leads into holes in the same column (i.e. column 'i') on your breadboard. Try and leave an empty row between each lead if you can.

1. You now need to wire up your transistor to a GPIO pin on your Raspberry Pi. These pins each have different numbers, so look at the diagram below and figure out which GPIO pin on your Raspberry Pi is which number. We want GPIO pin number 2. So take a male-to-female jumper cable and connect the female end onto GPIO pin number 2 on your Raspberry Pi, then insert the male end into the breadboard. It needs to connect with the Base lead of the transistor, so insert it into the same row as that (remember the Base lead is the middle lead on the transistor).

1. In order to complete the circuit coming from that GPIO pin we need to connect it to ground. So, using a male-to-male jumper cable, insert one end into the same row as the Emitter lead of the transistor and the other to the ground rail on your breadboard (that's the one of the columns that has a '-' sign on it (they're usually at the end of the board, and are usually black). Then take a female-to-male jumper cable and insert one end again into this ground rail and attach the other end onto a ground GPIO pin on your Raspberry Pi (so that's any pin with a '– ' sign or labelled GND - see the earlier diagram). 

    The circuit is now complete between GPIO PIN number 2, through the base lead of transistor, onto the emitter lead and then back to ground. This circuit is our low voltage circuit, but as we said before we also need a high(er) voltage circuit to heat up the resistor enough. . 

## Wire Up the Higher Voltage Circuit

For this high(er) voltage circuit, we're going to use a 9volt battery. 

1. Attach a battery snap onto a 9volt battery and place the black lead into the ground rail (the same one as you used before) and the red lead into the positive rail (is that what it's called?) on your breadboard- that's the red one, also possibly labelled with a '+' sign.

    (NOTE: Please make the red line continuous in this diagram).

1. We want this circuit to go through the resistor that you wired up in Step 1. So, take the wires with the resistor attached and with the free ends, insert the one with the red tape on into the positive (yes, the same one you just put the battery lead in) and insert the lead with the black tape on into the same row as the Collector lead of the transistor.

1. This circuit is now complete, the current will flow from the battery, through the resistor, to the Collector lead of the transistor, out the Emitter lead and then back to ground. As it flows through the resistor it will heat it up so much that the balloon will pop.

## Set Up More Balloons

Popping one balloon is good, but popping three balloons, is so much better!

1. Follow the point in Steps 1-3 for two more balloons. However, miss one the first point in Step 3, as you'll be using the same battery for all three resistors.  Also, use different pin number for these balloons:

    - For balloon 2 use GPIO Pin number 3
    - For balloon 3 use GPIO Pin Number 4

    You can label your balloons with a pen so you know which one is which

## Wire up an Input Button

This will allow you to have control over when the balloons begin popping.

1. The input button has two wires coming out of its base; insert the button into your breadboard (away from the transistors) so that these wires are in different rows.

1. Take a jumper cable and insert one end of it into one of these rows the button has just been placed into and insert the other end of this jumper cable into the ground rail (yes, the same one as before…again!)

1. Take a male-to-female jumper cable and insert one end into other row used by the button and attach the remaining free end of this cable onto GPIO pin number 14.

There you have it; all your hardware is complete. It's now time for the coding!

## Code your Balloon Pi-tay Popper

1. In the desktop area of your Raspberry Pi, open up a LX Terminal, either from the dropdown menu, or by double clicking on the 'LXTerminal' icon.

1. Once the LXTerminal is opened, type in `sudo idle3 &` and press `Enter`. This will (in time) open up a "Python Shell".

1. In this Python Shell go to `File -> New Window`. This opens up a place where you can actually write in your python code. It's called a (what is it called?)

1. It's good practice to save this file before you type anything important. To save go to `File -> Save As`, then type in the name you want to save the file as, such as 'balloon', and click `Save`. Now you can get coding!

1. Start by importing the Raspberry Pi GPIO pin library, to do this simply type:

    ```python
    import RPi.GPIO as GPIO
    ```

1. Now, on a new line, now import the sleep module from the time library of code, by typing:

    ```python
    from time import sleep
    ```

1. Now just leave a blank line of code by pressing enter , this is just for good practice.

1. Next type:

    ```python
    GPIO.setmode (GPIO.BCM)
    ```

And press enter. This sets the Raspberry Pi to note that the GPIO numbering system you'll be using will be the BCM numbering system (there are two different numbering systems for the GPIO pins- the other is called the Board numbering system).

1. Again, for good practice, leave a blank line of code by pressing enter.

1. Now set up your GPIO pin that your push button is connected to(number 14). This will act as an input so type:

    ```python
    GPIO.setup(14, GPIO.IN, GPIO.PUD_UP)
    ```

    And press enter. This tell the Raspberry Pi to treat GPIO number 14 as a 'pulled up' input. (the 'PUD_UP' stands for 'pull up or down' and then the allocation of 'up').

1.  Then, leave a blank line of code by pressing enter.

1. Next you have to allocate the outputs. As there are 3 different balloons, there are 3 different outputs. To set these up simply type:

    ```python
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    ```

    And press enter twice.

1. Make a note to yourself in your code, which GPIO is allocated to what by writing:

    ```python
    #Input 14 is GO BUTTON
    #Output2 is Balloon 1
    #Output3 is Balloon 2
    #Output4 is Balloon 3
    ```

    And press enter twice.

    (Note: by using a hash (`#`) before the words, it means these are just read as notes, and aren't read as actual code)

1. This next part isn't strictly necessary, but I use it so it's easier to make sense of the code. Look back at point 10, and you'll see that you set up your input button as Pull Up. This means that when it's not pushed it's read as being active, and the opposite is also true, so when it is pushed, it's read as being inactive. This seems confusing, but we do this because (why do we do this?). So, in order for you to make sense of the code write:

    ```python
    touched = GPIO.LOW
    ```

    And press enter twice.

1. Now you can write the code that will switch on your transistors, which in turn will make the balloons pop. First of all we only need the balloons to pop once so to ensure this is the case, type the following:

    ```python
    i = 1
    while i == 1:
    ```

    Then press enter one and then tab once.

1. Now type the following which will make the Raspberry Pi react to the input of the button push:

    ```
    if GPIO.input(14) == touched:
        print('Button Pushed')
        sleep(1)
    ```

    And press enter twice.

    (note: the program should automatically indent)

1. And now for the outputs. This code will, in turn, switch each of the outputs on, wait 5 seconds and then turn then them off again. This will result in the balloons exploding five seconds after one another:

    ```python
    GPIO.output(2, True)
    print('Balloon 1')
    sleep(5)
    GPIO.output(2, False)

    GPIO.output(3, True)
    print('Balloon 2')
    sleep(5)
    GPIO.output(3, False)

    GPIO.output(4, True)
    print('Balloon 3')
    sleep(5)
    GPIO.output(4, False)
    i += 1
    ```

    Then press enter twice, and then backspace once, to put the cursor in the correct position for the next part of the code.

    (note: the five seconds is needed for the resistor to get hot enough in order to pop the balloons).

1. So the above is for when the button is pushed, but you also need to give an option for when the button isn't pushed. So type:

    ```python
    else:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(4, False)
    ```

    Again the program should automatically indent. Then press enter twice and backspace twice, to return to the far left of screen.

1. Then simply type the below to finish your code:

    ```python
    GPIO.cleanup()
    ```

    And press enter one final time.

1. Save your program, but pressing `CTRL + S`.

## Run your Balloon Pi-tay Popper

1. You're almost ready to go, ensure that all your wires are in place and the resistors are still firmly taped onto the balloons.

1. Then with your 'Balloon Pi-tay Popper' code still open press `F5`.

1. This will open a new window on your screen.

1. After a line of 3 arrows has appeared in this new window, it is ready to receive your input. So, when you're ready, press your button and watch the balloons pop… pop… POP!

1. To stop the program from running just type `Ctrl + C`.

When you run the program (which we'll go into later) this code means that when the button is pushed, the words 'Button Pushed' will appear on the screen and then the Raspberry Pi will wait (or sleep) for one second.

## What next?

Other Stuff to Try:

- Try changing the order the balloons pop in. To do this just change the order the GPIO pin numbers are used in.

- Convert your balloon popper into a rather addictive Interactive Calculator. The wiring up is exactly the same, but the code is slightly different, see this worksheet for how to make it.
