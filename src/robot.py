import wpilib
import ntcore
import robotpy





class Robot(wpilib.TimedRobot):
    

    def robotInit(self) -> None:

        self.FLDrive = wpilib.Spark(0)
        self.FLDrive.set(0.3)

        self.FRDrive = wpilib.Spark(1)
        self.BLDrive = wpilib.Spark(2)
        self.BRDrive = wpilib.Spark(3)

        self.joystick = wpilib.Joystick(0)

    def robotPeriodic(self) -> None:
        wpilib.SmartDashboard.putNumber("Joysitck y", self.joystick.getY())




    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass
    

    

    def autonomousInit(self) -> None:
        pass
    
    def autonomousPeriodic(self) -> None:
        pass




    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass



if __name__ == "__main__":
    wpilib.run(Robot)