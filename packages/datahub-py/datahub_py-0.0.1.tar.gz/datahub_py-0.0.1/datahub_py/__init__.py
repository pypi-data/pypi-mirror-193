__version__ = '1.3'

from .Project.Project import Project
from .Beacon.Beacon import Beacon
from .Beacon.Network import NetworkHelpers as Network
from .CTRL.Server import Server

def hello_world():
    print("This is my first pip package!")
