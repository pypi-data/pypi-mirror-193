'''Test the haptic effects

Classes
-------
TestEffects

Functions
---------
test_spring()
test_damper()
test_bias_force()
test_shaker()

'''

import unittest
from haptic_master.haptic_master import HapticMaster
from haptic_master.effect import BiasForce, Damper, Shaker, Spring


IP = '192.168.0.25'
PORT = 7654


class TestEffects(unittest.TestCase):
    '''Unit test class for testing the haptic effects
    
    Methods
    -------
    test_spring()
        Test the spring effect
    test_damper()
        Test the damper effect
    test_bias_force()
        Test the bias force effect
    test_shaker()
        Test the shaker effect
    
    '''

    def test_spring(self):
        '''Testing the spring effect'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Spring parameters
        position = [0.0, 0.2, 0.5]
        velocity = [0.0001, 0.0002, 0.0003]
        attitude = [0.0, 0.0, 0.0499792, 0.9987503]
        stiffness = 10.0
        dampfactor = 0.01
        deadband = 0.023
        direction = [1.0, 0.0, 0.0]
        maxforce = 24.2
        dampglobal = False

        # Create a spring instance
        my_spring = Spring(name='mySpring', robot=robot)

        # Create the spring on the HapticMaster controller
        self.assertTrue(my_spring.create())

        # Set position of the spring and read it from the robot
        self.assertTrue(my_spring.set_pos(position))
        self.assertEqual(my_spring.get_pos(), position)

        # Set velocity of the spring and read it from the robot
        self.assertTrue(my_spring.set_vel(velocity))
        self.assertEqual(my_spring.get_vel(), velocity)

        # Set attitude of the spring and read it from the robot
        self.assertTrue(my_spring.set_att(attitude))
        # self.assertAlmostEqual(my_spring.get_att(), attitude, places=5)

        # Enable the spring
        self.assertTrue(my_spring.set_enable())
        self.assertEqual(my_spring.get_enabled(), True)

        # Disable the spring
        self.assertTrue(my_spring.set_disable())
        self.assertEqual(my_spring.get_enabled(), False)

        # Set stiffness and read it from the robot
        self.assertTrue(my_spring.set_stiffness(stiffness))
        self.assertEqual(my_spring.get_stiffness(), stiffness)

        # # Set damping factor and read it from the robot
        self.assertTrue(my_spring.set_dampfactor(dampfactor))
        self.assertEqual(my_spring.get_dampfactor(), dampfactor)

        # # Set deadband length and read it from the robot
        self.assertTrue(my_spring.set_deadband(deadband))
        self.assertEqual(my_spring.get_deadband(), deadband)

        # # Set spring direction and read it from the robot
        self.assertTrue(my_spring.set_direction(direction))
        self.assertEqual(my_spring.get_direction(), direction)

        # # Set spring's maximum force and read it from the robot
        self.assertTrue(my_spring.set_maxforce(maxforce))
        self.assertEqual(my_spring.get_maxforce(), maxforce)

        # Set spring's global damping and read it from the robot
        self.assertTrue(my_spring.set_dampglobal(dampglobal))
        self.assertFalse(my_spring.get_dampglobal())

        # Remove effect
        self.assertTrue(my_spring.remove())

        robot.disconnect()

    def test_damper(self):
        '''Testing the damper effect'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        my_damper = Damper(name='myDamper', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(my_damper.create())

        dampcoef = [0.2, 0.43, 0.59]

        # Set the damper's damping coefficient and read it from the robot
        self.assertTrue(my_damper.set_dampcoef(dampcoef))
        self.assertEqual(my_damper.get_dampcoef(), dampcoef)

        robot.disconnect()

    def test_bias_force(self):
        '''Testing the bias force effect'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Create a damper instance
        my_bias_force = BiasForce(name='myBiasForce', robot=robot)

        # Create the damper on the HapticMaster controller
        self.assertTrue(my_bias_force.create())

        force = [0.192, 0.233, 0.995]

        # Set the bias force's value and read it from the robot
        self.assertTrue(my_bias_force.set_force(force))
        self.assertEqual(my_bias_force.get_force(), force)

        robot.disconnect()

    def test_shaker(self):
        '''Testing the shaker effect'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        frequency1 = 0.21
        frequency2 = 0.12
        direction = [0.0, 1.0, 0.0]
        posmax = 0.23
        velmax = 2.3
        accmax = 23.0
        stiffness = 120.0
        dampfactor = 0.02
        deadband = 1.3
        maxforce = 12.5

        my_shaker = Shaker('myShaker', robot)

        self.assertTrue(my_shaker.create())

        self.assertTrue(my_shaker.set_frequency1(frequency1))
        self.assertEqual(my_shaker.get_frequency1(), frequency1)

        self.assertTrue(my_shaker.set_frequency2(frequency2))
        self.assertEqual(my_shaker.get_frequency2(), frequency2)

        self.assertTrue(my_shaker.set_direction(direction))
        self.assertEqual(my_shaker.get_direction(), direction)

        self.assertTrue(my_shaker.set_posmax(posmax))
        self.assertEqual(my_shaker.get_posmax(), posmax)

        self.assertTrue(my_shaker.set_velmax(velmax))
        self.assertEqual(my_shaker.get_velmax(), velmax)

        self.assertTrue(my_shaker.set_accmax(accmax))
        self.assertEqual(my_shaker.get_accmax(), accmax)

        self.assertTrue(my_shaker.set_stiffness(stiffness))
        self.assertEqual(my_shaker.get_stiffness(), stiffness)

        self.assertTrue(my_shaker.set_dampfactor(dampfactor))
        self.assertEqual(my_shaker.get_dampfactor(), dampfactor)

        self.assertTrue(my_shaker.set_deadband(deadband))
        self.assertEqual(my_shaker.get_deadband(), deadband)

        self.assertTrue(my_shaker.set_maxforce(maxforce))
        self.assertEqual(my_shaker.get_maxforce(), maxforce)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()
