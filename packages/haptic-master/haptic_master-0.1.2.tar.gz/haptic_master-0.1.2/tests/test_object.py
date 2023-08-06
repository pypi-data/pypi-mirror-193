'''Test the haptic objects

Classes
-------
TestObjects

Functions
---------
test_block()
test_sphere()
test_flat_plane()
test_cylinder()
test_torus()

'''

import unittest
from haptic_master.haptic_master import HapticMaster
from haptic_master.object import Block, Cylinder, FlatPlane, Sphere, Torus


IP = '192.168.0.25'
PORT = 7654


class TestObjects(unittest.TestCase):
    '''Unit test class for testing the haptic objects
    
    Methods
    -------
    test_block()
        Test the block object
    test_sphere()
        Test the sphere object
    test_flat_plane()
        Test the flat plane object
    test_cylinder()
        Test the cylinder object
    test_torus()
        Test the torus object
    
    '''

    def test_block(self):
        '''Testing block object'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        my_block = Block('myBlock', robot)

        self.assertTrue(my_block.create())

        stiffness = 10.23
        dampfactor = 0.593
        no_pull = False
        tang_damping = 0.0432
        damping_forcemax = 1.203
        friction = 2.302
        ejection_velmax = 0.232
        ejection_damping = 0.392
        outward_forcemax = 20.23
        powermax = 102.0
        block_size = [0.23, 0.31, 0.15]

        # Set the stiffness of the object and read it from the robot
        self.assertTrue(my_block.set_stiffness(stiffness))
        self.assertEqual(my_block.get_stiffness(), stiffness)

        # Set damping factor of the object and read it from the robot
        self.assertTrue(my_block.set_dampfactor(dampfactor))
        self.assertEqual(my_block.get_dampfactor(), dampfactor)

        # Set no pull of the object and read it from the robot
        self.assertTrue(my_block.set_no_pull(no_pull))
        self.assertEqual(my_block.get_no_pull(), no_pull)

        # Set tangential damping of the object and read it from the robot
        self.assertTrue(my_block.set_tang_damping(tang_damping))
        self.assertEqual(my_block.get_tang_damping(), tang_damping)

        # Set max damping force of the object and read it from the robot
        self.assertTrue(my_block.set_damping_forcemax(damping_forcemax))
        self.assertEqual(my_block.get_damping_forcemax(), damping_forcemax)

        # Set friction of the object and read it from the robot
        self.assertTrue(my_block.set_friction(friction))
        self.assertEqual(my_block.get_friction(), friction)

        # Set max ejection velocity of the object and read it from the robot
        self.assertTrue(my_block.set_ejection_velmax(ejection_velmax))
        self.assertEqual(my_block.get_ejection_velmax(), ejection_velmax)

        # Set ejection damping of the object and read it from the robot
        self.assertTrue(my_block.set_ejection_damping(ejection_damping))
        self.assertEqual(my_block.get_ejection_damping(), ejection_damping)

        # Set max outward force of the object and read it from the robot
        self.assertTrue(my_block.set_outward_forcemax(outward_forcemax))
        self.assertEqual(my_block.get_outward_forcemax(), outward_forcemax)

        # Set max power of the object and read it from the robot
        self.assertTrue(my_block.set_powermax(powermax))
        self.assertEqual(my_block.get_powermax(), powermax)

        # Set block size and read it from the robot
        self.assertTrue(my_block.set_size(block_size))
        self.assertEqual(my_block.get_size(), block_size)

        # Remove object
        self.assertTrue(my_block.remove())

        robot.disconnect()

    def test_sphere(self):
        '''Testing sphere object'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        my_sphere = Sphere('mySphere', robot)

        self.assertTrue(my_sphere.create())

        sphere_radius = 0.258

        self.assertTrue(my_sphere.set_radius(sphere_radius))
        self.assertEqual(my_sphere.get_radius(), sphere_radius)

        robot.disconnect()

    def test_flat_plane(self):
        '''Testing flat plane object'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        my_flat_plane = FlatPlane('myFlatPlane', robot)

        self.assertTrue(my_flat_plane.create())

        plane_normal = [1.0, 0.0, 0.0]

        self.assertTrue(my_flat_plane.set_normal(plane_normal))
        self.assertEqual(my_flat_plane.get_normal(), plane_normal)

        robot.disconnect()

    def test_cylinder(self):
        '''Testing cylinder object'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        my_cylinder = Cylinder('myCylinder', robot)

        self.assertTrue(my_cylinder.create())

        cylinder_radius = 0.201
        cylinder_length = 0.492

        self.assertTrue(my_cylinder.set_radius(cylinder_radius))
        self.assertEqual(my_cylinder.get_radius(), cylinder_radius)
        self.assertTrue(my_cylinder.set_length(cylinder_length))
        self.assertEqual(my_cylinder.get_length(), cylinder_length)

        robot.disconnect()

    def test_torus(self):
        '''Testing torus object'''

        # Open connection
        robot = HapticMaster(IP, PORT)
        robot.connect()

        my_torus = Torus('myTorus', robot)

        self.assertTrue(my_torus.create())

        torus_ring_radius = 0.203
        torus_outer_radius = 0.943

        self.assertTrue(my_torus.set_ringradius(torus_ring_radius))
        self.assertEqual(my_torus.get_ringradius(), torus_ring_radius)

        self.assertTrue(my_torus.set_tuberadius(torus_outer_radius))
        self.assertEqual(my_torus.get_tuberadius(), torus_outer_radius)

        robot.disconnect()


if __name__ == '__main__':
    unittest.main()
