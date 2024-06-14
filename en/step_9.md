## Code more balloons

Now we'll return to the code and make a few small adjustments to make it pop more balloons!

---- task ---

Where we previously used `balloon = OutputDevice(2)` to store the GPIO pin for the first balloon, you'll now need to set up more balloons. You can do this using a list:

```python
balloons = [OutputDevice(2), OutputDevice(3)]
```

--- /task ---

---- task ---

Then, instead of just popping one balloon, we'll make it pop them all in turn:

```python
for balloon in balloons:
    print("Armed...")
    balloon.on()
    sleep(10)
    balloon.off()
```

--- /task ---



