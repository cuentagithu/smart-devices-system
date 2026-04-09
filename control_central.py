class ControlCentral:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def manage_devices(self):
        for device in self.devices:
            device.manage()
        
    def get_device_status(self):
        return {device.name: device.status for device in self.devices}