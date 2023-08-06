__version__ = '0.0.2'

print("Datahub Version :: ", __version__)

from .Project.Project import Project
from .Beacon.Beacon import Beacon
from .Beacon.Network import NetworkHelpers as Network
from .CTRL.Server import Server

def hello_world():
    print("This is my first pip package!")
