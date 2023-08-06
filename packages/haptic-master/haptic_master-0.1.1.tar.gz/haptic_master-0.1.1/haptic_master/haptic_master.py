'''Class for handling HapticMaster communications and operations

Classes
-------
HapticMaster

Functions
---------
connect()
disconnect()
get_inertia()
set_inertia(value)
get_state()
set_state(value)
get_coulombfriction()
set_coulombfriction(value)
get_measpos()
get_measforce()
get_modelpos()
get_modelvel()
get_modelacc()
get_measposjoint()
get_measforcejoint()
get_modelposjoint()
get_modelveljoint()
get_modelaccjoint()
get_force_calibrated()
get_position_calibrated()
get_workspace_r()
get_workspace_phi()
get_workspace_z()

Variables
---------
ip_address
port
sock

'''

import socket
import re
import logging
from string import printable
from dataclasses import dataclass, field


@dataclass(frozen=True)
class HapticMaster:
    '''A class for HapticMaster

    Attributes
    ----------
    ip_address (str): IP address of the robot
    port (int): Port number of the robot
    sock (socket): Socket for TCP/IP communication

    Methods
    -------
    connect()
        Connect to the HapticMaster robot
    disconnect()
        Close the connection to the HapticMaster robot
    get_inertia()
        Get the end-effector inertia of the robot
    set_inertia(value)
        Set the end-effector inertia of the robot
    get_state()
        Get the current state of the robot
    set_state(value)
        Set the state of the robot
    get_coulombfriction()
        Get the Coloumb friction of the robot
    set_coulombfriction(value)
        Set the Coloumb friction of the robot
    get_measpos()
        Get the measured position of the robot
    get_measforce()
        Get the measured force of the robot
    get_modelpos()
        Get the model position
    get_modelvel()
        Get the model velocity
    get_modelacc()
        Get the model acceleration
    get_measposjoint()
        Get the measured position in joint space
    get_measforcejoint()
        Get the measured force (torque) in joint space
    get_modelposjoint()
        Get the model position in joint space
    get_modelveljoint()
        Get the model velocity in joint space
    get_modelaccjoint()
        Get the model acceleration in joint space
    get_force_calibrated()
        Check if the robot is force calibrated
    get_position_calibrated()
        Check if the robot is position calibrated
    get_workspace_r()
        Get the workspace limits for r-direction
    get_workspace_phi()
        Get the workspace limits for phi-direction
    get_workspace_z()
        Get the workspace limits for z-direction

    '''

    ip_address: str
    port: int
    sock: socket = field(default_factory=lambda: socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    def connect(self):
        '''Connect to the HapticMaster robot'''

        try:
            # Connect to the robot
            self.sock.connect((self.ip_address, self.port))

        except socket.error:
            logging.error('Connection error')

    def disconnect(self):
        '''Clear all haptic effects and objects and close connection'''

        # Clear all haptic effects
        msg = 'remove all'
        logging.info(self.send_message(msg))

        # Close connection
        self.sock.close()

    def get_inertia(self) -> float:
        '''Get the end-effector inertia of the robot

        Returns
        -------
        float: End-effector inertia [kg]

        '''

        msg = 'get inertia'

        return float(self.send_message(msg))

    def set_inertia(self, value: float) -> bool:
        '''Set the end-effector inertia of the robot

        Parameters
        ----------
        value (float): End-effector inertia [kg]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = 'set inertia ' + str(value)

        response = self.send_message(msg)

        logging.info(response)

        return True

    def get_state(self) -> str:
        '''Get the current state of the robot

        Returns
        -------
        str: State of the robot: init, off, force, position, home

        '''

        msg = 'get state'

        return self.send_message(msg)

    def set_state(self, device_state):
        '''Set the state of the robot

        Parameters
        ----------
        device_state (str): State for the robot

        Returns
        -------
        str: Response from the robot

        '''

        if device_state in ['init', 'off', 'force', 'position', 'home']:
            msg = 'set state ' + device_state
            return self.send_message(msg)
        raise ValueError('Wrong state name is given')

    def get_coulombfriction(self) -> float:
        '''Get the minimum force before moving the robot (Coulomb friction)

        Returns
        -------
        float: Coulomb friction [N]

        '''

        msg = 'get coulombfriction'

        return float(self.send_message(msg))

    def set_coulombfriction(self, value: float) -> bool:
        '''Set the Coulomb friction of the robot

        Parameters
        ----------
        value (float): Coulomb friction [N]

        Returns
        -------
        bool: True if successful, False otherwise

        '''

        msg = 'set coulombfriction ' + str(value)

        return 'Coulomb friction set' in self.send_message(msg)

    def get_measpos(self) -> list:
        '''Get the measured position of the robot end-effector

        Returns
        -------
        list: Position vector [m]

        '''

        msg = 'get measpos'

        return self.string_to_list(self.send_message(msg))

    def get_measforce(self) -> list:
        '''Get the measured force of the robot end-effector

        Returns
        -------
        list: Force vector [N]

        '''

        msg = 'get measforce'

        return self.string_to_list(self.send_message(msg))

    def get_modelpos(self) -> list:
        '''Get the model position of the robot end-effector

        Returns
        -------
        list: Position vector [m]

        '''

        msg = 'get modelpos'

        return self.string_to_list(self.send_message(msg))

    def get_modelvel(self) -> list:
        '''Get the model velocity of the robot end-effector

        Returns
        -------
        list: Velocity vector [m/s]

        '''

        msg = 'get modelvel'

        return self.string_to_list(self.send_message(msg))

    def get_modelacc(self) -> list:

        '''Get the model acceleration of the robot end-effector

        Returns
        -------
        list: Acceleration vector [m/s^2]

        '''

        msg = 'get modelacc'

        return self.string_to_list(self.send_message(msg))

    def get_measposjoint(self) -> list:
        '''Get the measured position of the robot joints

        Returns
        -------
        list: Position vector [m]

        '''

        msg = 'get measposjoint'

        return self.string_to_list(self.send_message(msg))

    def get_measforcejoint(self) -> list:
        '''Get the measured force of the robot joints

        Returns
        -------
        list: Force vector [N]

        '''

        msg = 'get measforcejoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelposjoint(self) -> list:
        '''Get the model position of the robot joints

        Returns
        -------
        list: Position vector [m]

        '''

        msg = 'get modelposjoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelveljoint(self) -> list:
        '''Get the model velocity of the robot joints

        Returns
        -------
        list: Velocity vector [m/s]

        '''

        msg = 'get modelveljoint'

        return self.string_to_list(self.send_message(msg))

    def get_modelaccjoint(self) -> list:
        '''Get the model acceleration of the robot joints

        Returns
        -------
        list: Acceleration vector [m/s^2]

        '''

        msg = 'get modelaccjoint'

        return self.string_to_list(self.send_message(msg))

    def get_force_calibrated(self) -> bool:
        '''Check if the robot force sensor is calibrated

        Returns
        -------
        bool: Calibration status [non-dimensional]

        '''

        msg = 'get force_calibrated'

        return self.string_to_bool(self.send_message(msg))

    def get_position_calibrated(self) -> bool:
        '''Check if the robot position sensors are calibrated

        Returns
        -------
        bool: Calibration status [non-dimensional]

        '''

        msg = 'get position_calibrated'

        return self.string_to_bool(self.send_message(msg))

    def get_workspace_r(self) -> list:
        '''Get the workspace dimensions of the robot in radial direction
        R low stop, Distance to center to real axis, R high stop

        Returns
        -------
        list: Workspace limits [m]

        '''

        msg = 'get workspace_r'

        return self.string_to_list(self.send_message(msg))

    def get_workspace_phi(self) -> list:
        '''Get the workspace dimensions of the robot in angular direction
        Phi low stop, Phi high stop

        Returns
        -------
        list: Workspace limits [rad]

        '''

        msg = 'get workspace_phi'

        return self.string_to_list(self.send_message(msg))

    def get_workspace_z(self) -> list:
        '''Get the workspace dimensions of the robot in z-direction
        Z low stop, Z high stop

        Returns
        -------
        list: Workspace limits [m]

        '''

        msg = 'get workspace_z'

        return self.string_to_list(self.send_message(msg))

    def calibrateforcesensor(self) -> bool:
        '''Calibrate the force sensor of the robot

        Returns
        -------
        bool: Calibration status [non-dimensional]

        '''

        return 'Force sensor calibrated' in self.send_message('calibrateforcesensor')

    def _haptic_master_message(self, msg):
        '''Create the serialised message accepted by the HapticMaster

        Parameters
        ----------
        msg (str): Message to be serialised

        Returns
        -------
        list: Decimal representation of the message in the correct format

        '''

        hm_msg = [0, 0, 0, 0, 0, 0, 0, 0]

        # Convert msg to ascii dec
        decimal_msg = [ord(c) for c in msg]

        hm_msg[3] = len(decimal_msg)

        return hm_msg + decimal_msg

    def _haptic_master_response(self, msg):
        '''Decode the reponse from the haptic master

        Parameters
        ----------
        msg (list): Decimal byte array of the response message

        Returns
        -------
        str: Decoded message as a string

        '''

        msg_str = ''.join(c for c in msg.decode('ascii') if c in printable)

        if re.search('[a-zA-Z]', msg_str):
            return msg_str.replace('"', '').replace('\n', '')

        return msg_str

    def send_message(self, msg: str) -> str:
        '''Send message to HapticMaster using TCP/IP over socket

        Parameters
        ----------
        msg (str): Message to be sent to the robot

        Returns
        -------
        str : Response from the HapticMaster

        '''

        self.sock.sendall(bytearray(self._haptic_master_message(msg)))

        try:
            return self._haptic_master_response(self.sock.recv(1024))
        except Exception as socket_exception:
            raise socket_exception

    def string_to_list(self, list_s: str):
        '''Convert a list in a string to a float string

        Parameters
        ----------
        list_s (str): String containing the list

        Returns
        -------
        list: Float list from the string

        '''

        return [float(si) for si in list_s[list_s.find('[')+1:list_s.find(']')].split(',')]

    def string_to_bool(self, bool_s: str):
        '''Convert a boolean in a string to a boolean

        Parameters
        ----------
        bool_s (str): String containing the boolean

        Returns
        -------
        bool: Boolean from the string

        '''

        return 'true' in bool_s
