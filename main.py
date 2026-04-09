import tkinter as tk
from tkinter import messagebox

class SmartHomeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Smart Home Control System")

        self.label = tk.Label(master, text="Welcome to the Smart Home Control System!")
        self.label.pack()

        self.lights_button = tk.Button(master, text="Control Lights", command=self.control_lights)
        self.lights_button.pack()

        self.thermostat_button = tk.Button(master, text="Control Thermostat", command=self.control_thermostat)
        self.thermostat_button.pack()

        self.security_button = tk.Button(master, text="Control Security System", command=self.control_security)
        self.security_button.pack()

    def control_lights(self):
        messagebox.showinfo("Control Lights", "Lights control panel")

    def control_thermostat(self):
        messagebox.showinfo("Control Thermostat", "Thermostat control panel")

    def control_security(self):
        messagebox.showinfo("Control Security", "Security system control panel")

if __name__ == '__main__':
    root = tk.Tk()
    gui = SmartHomeGUI(root)
    root.mainloop()