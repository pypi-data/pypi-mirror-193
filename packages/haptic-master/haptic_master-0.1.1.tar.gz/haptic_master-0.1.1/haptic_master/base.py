'''Create a base for effects and objects

Classes
-------
Base

Functions
---------
get_pos()
set_pos(value)
get_vel()
set_vel(value)
get_att()
set_att(value)

Variables
---------
name
robot

'''

from dataclasses import dataclass
from .haptic_master import HapticMaster

@dataclass(frozen=True, slots=True)
class Base:
    '''Base class shared by effects and objects of the HapticMaster API

    Attributes
    ----------
    name (str): Name of the effect/object
    robot (HapticMaster): The robot where the effect/object is going to be implemented

    Methods
    -------
    get_pos()
        Get the position of the effect/object from the robot
    set_pos(value)
        Set the position of the effect/object on the robot
    get_vel()
        Get the velocity of the effect/object from the robot
    set_vel(value)
        Set the velocity of the effect/object on the robot
    get_att()
        Get the orientation of the effect/object from the robot
    set_att(value)
        Set the orientation of the effect/object on the robot

    '''

    name: str
    robot: HapticMaster

    def get_pos(self) -> list:
        '''Get the position of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'get ' + self.name + ' pos'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_pos(self, value: list) -> bool:
        '''Set the position of the effect/object on the robot

        Parameters
        ----------
        value (list): The position of the effect/object to be set

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'set ' + self.name + ' pos ' + str(value).replace(' ', '')

        return 'Effect\'s position set' in self.robot.send_message(msg)

    def get_vel(self) -> list:
        '''Get the velocity of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'get ' + self.name + ' vel'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_vel(self, value: list) -> bool:
        '''Set the velocity of the effect/object on the robot

        Parameters
        ----------
        value (list): The velocity of the effect/object to be set

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'set ' + self.name + ' vel ' + str(value).replace(' ', '')

        return 'Effect\'s velocity set' in self.robot.send_message(msg)

    def get_att(self) -> list:
        '''Get the attitude (orientation) of the effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'get ' + self.name + ' att'

        return self.robot.string_to_list(self.robot.send_message(msg))

    def set_att(self, value: list) -> bool:
        '''Set the attitude (orientation) of the effect/object on the robot

        Parameters
        ----------
        value (list): The orientation of the effect/object to be set as
                      a unit quaternion

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'set ' + self.name + ' att ' + str(value).replace(' ', '')

        return 'Effect\'s attitude set' in self.robot.send_message(msg)

    def set_enable(self) -> bool:
        '''Enable the effect/object

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'set ' + self.name + ' enable'

        return 'enabled' in self.robot.send_message(msg)

    def set_disable(self) -> bool:
        '''Disable the effect/object

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'set ' + self.name + ' disable'

        return 'disabled' in self.robot.send_message(msg)

    def get_enabled(self) -> bool:
        '''Get the enable/disable status of an effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        msg = 'get ' + self.name + ' enabled'

        return self.robot.string_to_bool(self.robot.send_message(msg))

    def remove(self) -> bool:
        '''Remove an effect/object from the robot

        Returns
        -------
        bool: True if successful, False otherwise

        '''
        return 'Removed' in self.robot.send_message(f'remove {self.name}')
