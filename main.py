from hub import port, button, sound
import runloop, motor, time, color_sensor,time

async def main():
    #await GLUE.AwaitNextFunction(Model_2)
    # Example code using the GLUE library.
    print("Hello, World!")
    await GLUE.AssignMotorPorts(port.D,port.C)
    await GLUE.MotorPairMoveForward(1500, 400) # move using the GLUE library!
    time.sleep_ms(2001)
    motor.run_to_absolute_position(port.E,367, 300)
    time.sleep_ms(550)
    await GLUE.MotorPairMoveBackward(500, 300)
    time.sleep_ms(501)
    await GLUE.MotorPairMoveForward(180, 200)
    motor.run_to_relative_position(port.E,2, 120)
    time.sleep_ms(500)
    await GLUE.MotorPairMoveForward(100,150)
    time.sleep_ms(100)
    motor.run_to_absolute_position(port.E, 266, 10000)
    time.sleep_ms(500)
    await GLUE.MotorPairMoveBackward(1500, 400)
    time.sleep(7)
    sound.beep(4000,500)
    time.sleep(3)
    # model 1.5
    await GLUE.MotorPairMoveForward(5000,1000000)
    #runloop.run(Model_2())
    
    return 0



async def Model_2():
    print("doing second model")
    """
    await GLUE.MotorPairMoveForward(835,600)
    time.sleep_ms(3000)
    await GLUE.TurnLeft()
    time.sleep_ms(1000)
    await GLUE.MotorPairMoveForward(1000, 450)
    time.sleep_ms(1200)
    await GLUE.TurnRight()
    time.sleep_ms(1100)
    await GLUE.MotorPairMoveForward(1000, 450)
    time.sleep_ms(1000)
    await GLUE.TurnRight()
    time.sleep_ms(1000)
    await GLUE.MotorPairMoveForward(600, 700)
    time.sleep_ms(1200)
    """
    await GLUE.MotorPairMoveForward(1000,200)
    time.sleep_ms(1200)
    await GLUE.TurnLeft()
    time.sleep_ms(1200)
    await GLUE.MotorPairMoveForward(1000,550)
    time.sleep_ms(1200)
    await GLUE.TurnRight()
    time.sleep_ms(1200)
    await GLUE.MotorPairMoveForward(1200, 900)
    time.sleep_ms(2900)
    await GLUE.TurnRight()
    time.sleep_ms(1200)
    motor.run_to_absolute_position(port.E, 319, 10000)
    await GLUE.MotorPairMoveForward(700,450)
    time.sleep_ms(1500)
    time.sleep_ms(600)
    await GLUE.MotorPairMoveForward(550, 450)
    time.sleep_ms(2000)
    for x in range(5):
        time.sleep_ms(1000)
        await motor.run_for_time(port.E, 2000,400)
        time.sleep_ms(600)
        motor.run_to_absolute_position(port.E, 260, 600)
        time.sleep_ms(300)
        await GLUE.MotorPairMoveBackward(750, 100)
    time.sleep_ms(3500)
    await GLUE.MotorPairMoveBackward(1000,500)
    time.sleep_ms(1300)
    await GLUE.TurnRight()
    time.sleep_ms(1200)
    await GLUE.MotorPairMoveForward(1600, 1000)
    #await GLUE.MotorPairMoveForward(1200, 600)

    """
    await GLUE.MotorPairMoveForward(2500, 10000) # deprecated code will not run until updated
    time.sleep_ms(2501)
    await GLUE.MotorPairMoveBackward(1900, 10000)
    """


    #motor.run_to_absolute_position(port.E, 36, 1000)
    time.sleep_ms(100)




# --------------------------
# GLUE LIBRARY:


# GPL 3.0
# LEGO
# UNIVERSAL
# EXTENSION


# this is a addon to lego robotics to make life easier for anybody just trying to go about their day.

# under the GPL 3.0 license respect that!

# original repo and author: https://github.com/SnowDev9099/Python-GLUE-Library/tree/main

# --------------------------

class GLUE:

    @staticmethod
    async def AwaitNextFunction(Function):
        DONE = False
        while not DONE:
            if button.pressed(button.LEFT or button.RIGHT):
                Function()


    @staticmethod
    async def AssignMotorPorts(Port_ONE, Port_TWO):
        global Port_SECOND
        global Port_FIRST
        Port_SECOND = Port_TWO
        Port_FIRST = Port_ONE



    # motor pair is already a function but when you have your drivebase hooked up to it, it tends to "get a bit funky" this aims to solve that
    @staticmethod
    async def MotorPairMoveForward(DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        global Port_SECOND
        global Port_FIRST

        motor.run_for_time(Port_SECOND, DurationInMS, -Velocity)
        motor.run_for_time(Port_FIRST, DurationInMS, Velocity)


    @staticmethod
    async def MotorPairMoveBackward(DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        global Port_SECOND
        global Port_FIRST

        motor.run_for_time(Port_SECOND, DurationInMS, Velocity)
        motor.run_for_time(Port_FIRST, DurationInMS, -Velocity)


    @staticmethod
    async def TurnLeft(time=1000,velocity=-500):
        global Port_FIRST
        Port_FIRST
        motor.run_for_time(Port_FIRST, 800, 500)


    @staticmethod
    async def TurnRight(time=1000,velocity=-500):
        global Port_SECOND
        Port_SECOND
        motor.run_for_time(Port_SECOND, 800, -500)

    @staticmethod
    def GetCurrentColor(port_first=port.A):
        return color_sensor.color(port_first)

    @staticmethod
    async def Calculate(First, Second, Add, Subtract, Multiply, Divide): # good for things you'll need to calcute either being async or easier with a method. you could calculate distance posibly with speed and distance sensor?
        if Add:
            return First + Second
        elif Subtract:
            return First - Second
        elif Multiply:
            return First * Second
        elif Divide:
            if Second == 0:
                print("Divide by zero error!")
            else:
                return First / Second

    @staticmethod
    def MotorPairStop():
        global MotorStop
        MotorStop = True


    @staticmethod
    def MotorPairRun(port_first=port.C, port_second=port.E, Velocity=200):
        global MotorStop
        MotorStop = False
        while not MotorStop:
            motor.run(port_first, Velocity)
            motor.run(port_second, -Velocity)
            time.sleep_ms(50) # prevents code from stopping and overloading the CPU on the Lego Spike Hub
        motor.stop(port_first)
        motor.stop(port_second)









runloop.run(main())
