import pickle
class Config:
    def __init__(self):
        self.settings = {}
        try:
            with open('sliders.conf', 'rb') as handle:
                self.settings = pickle.load(handle)
        except FileNotFoundError:
            self.settings["cmdline"] = "SLD> "
            self.settings["run"] = "echo No run command yet! Define one with settings run echo Your command!"
            self.settings["editor"] = "nano"
