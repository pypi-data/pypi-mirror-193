'''Test the haptic master

Classes
-------
TestHapticMaster

Functions
---------
test_connection()
test_inertia()
test_state()
test_coulombfriction()
test_calibrate_force_sensor()

'''

import unittest
from haptic_master.haptic_master import HapticMaster


IP = '192.168.0.25'
PORT = 7654


class TestHapticMaster(unittest.TestCase):
    '''Unit test class for testing the haptic master
    
    Methods
    -------
    test_connection()
        Test the connection to the robot
    test_inertia()
        Test the inertia of the robot
    test_state()
        Test the states of the robot
    test_coulombfriction()
        Test the Coulomb friction of the robot
    test_calibrate_force_sensor()
        Test the force sensor calibration of the robot
    
    '''

    def test_connection(self):
        '''Testing the robot communication'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        robot.disconnect()

    def test_inertia(self):
        '''
        Testing the inertia of the robot, set the inertia to the specified
        value and read the inertia from the robot
        '''

        # Open connection]
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # End-effector inertia value for the robot
        end_effector_inertia = 2.3

        # Set the inertia
        robot.set_inertia(end_effector_inertia)

        # Get inertia value
        self.assertEqual(robot.get_inertia(), end_effector_inertia)

        robot.disconnect()

    def test_state(self):
        '''
        Testing the robot states, set the robot states to position and force
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        # Set state to position
        self.assertEqual(robot.set_state('position'), 'state set to \'position\'')

        # Read the state value from the robot
        self.assertEqual(robot.get_state(), 'position')

        # Set state to force
        self.assertEqual(robot.set_state('force'), 'state set to \'force\'')

        # Read the state value from the robot
        self.assertEqual(robot.get_state(), 'force')

        robot.disconnect()

    def test_coulombfriction(self):
        '''
        Testing the coulomb friction
        Set the friction coefficient to a predefined value and read it from
        the robot
        '''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        coulomb_friction_coef = 0.205

        # Set the Coulomb friction coefficient
        self.assertTrue(robot.set_coulombfriction(coulomb_friction_coef))

        # Read the Coulomb friction coefficient from the robot
        self.assertEqual(robot.get_coulombfriction(), coulomb_friction_coef)

        robot.disconnect()

    def test_calibrate_force_sensor(self):
        '''Testing the force sensor calibration'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        self.assertTrue(robot.calibrateforcesensor())

        robot.disconnect()

if __name__ == '__main__':
    unittest.main()
