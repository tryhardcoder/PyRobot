from abc import ABC, abstractmethod
import wpilib
import ntcore
import robotpy


class V2:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y







class MechDriveController:

    def __init__(self) -> None:
        pass

    # linear in m/s, angular in degs/s
    def tick(self, linear: V2, angular: V2) -> list[float]:
        pass







class MechDrive:

    def __init__(self, ports: list[int]) -> None:
        assert(len(ports) == 4)

        self.motors = [ wpilib.Spark(ports[0]), 
                        wpilib.Spark(ports[1]),
                        wpilib.Spark(ports[2]),
                        wpilib.Spark(ports[3]) ]


    def setPower(self, powerVals: list[float]) -> None:
        assert(len(powerVals) == 4)

        i = 0
        for motor in self.motors:
            motor.set(powerVals[i])

            i+=1









# Prof -> drive interface
# (linear, angular, x)


# drive ctrl -> mech hardware interface
# (powers)


# drive ctrl -> swerve interface
# (angular speeds, linear speeds)



