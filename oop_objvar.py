class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots.
    # Usage: Robot.population OR self.__class__.population
    population = 0

    def __init__(self, name):
        """Initialize the robot data."""
        # Note: self.name is a object variable.
        self.name = name
        print('Initializing {0} ...'.format(self.name))

        # When a robot is created,
        # robot population +1
        # Note: it's Robot.population, not self.population, BECAUSE Robot.population is a class variable!
        Robot.population += 1

    def say_hi(self):
        """Greeting from a robot.
        Yeah, they can do that."""
        print('Greetings, master, you can call me', self.name)

    def die(self):
        """A robot is dying ..."""
        print('Robot {0} is dying ...'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} is the last robot.'.format(self.name))
        elif Robot.population == 1:
            print('There is still only one robot left working.')
        else:
            print('There are still {} robots working'.format(Robot.population))

    @classmethod
    # Usage: Robot.count() or self.__class__.count()
    def count(cls):
        """Count the population of robots"""
        if Robot.population == 0:
            print('Master, now we have no robot.')
        elif Robot.population == 1:
            print('Master, we have only one robot working now.')
        else:
            print('Master, we already have {} robots working now.'.format(Robot.population))


android_1 = Robot('Android No. 1')
android_1.say_hi()
Robot.count()

print('\n')

android_2 = Robot('Android No. 2')
android_2.say_hi()
Robot.count()

print('\n')

android_3 = Robot('Android No. 3')
android_3.say_hi()
# android_3.count()  # Note: it works, but is not recommended.
Robot.count()
android_1.die()

print('\n')

android_4 = Robot('Android No. 4')
android_4.say_hi()
android_2.die()
Robot.count()

print('\n')

android_5 = Robot('Android No. 5')
android_5.say_hi()
Robot.count()

print('\n')

print(android_5.__class__.population)
android_5.__class__.count()
