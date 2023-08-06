from ..Beacon import Beacon
from ..CTRL import Server

import random
import string

class Project:
  def __init__(self, config):
    print("Project Init")
    self.id = self.generateID()
    print("[Project] ID: "+self.id)
    self.config = config
    self.server = Server(self, config)
    self.beacon = Beacon(self, config)
    self.port = self.beacon.helper.get_available_port()
    self.server.start(self.port)
    self.beacon.start()
  
  def generateID(self):
    return self.config.projectSpecs["type"]+(''.join(random.choices(string.ascii_uppercase + string.digits, k=7)))

  # Mandatory endpoint
  def specs(self):
    return {
      "id": self.id,
      "name": self.config.projectSpecs["name"],
      "queues": self.config.projectSpecs["queues"],
      "description": self.config.projectSpecs["description"],
      "address": self.beacon.helper.get_local_ip_address(),
      "port": self.port
    }, 200
