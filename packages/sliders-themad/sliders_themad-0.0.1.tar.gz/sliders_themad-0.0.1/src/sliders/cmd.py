import os, sys
import pickle
class CmdParser:
    def __init__(self, settings):
        self.conf = settings
    def parse(self, cmd, args):
        if args[0] == "help":
            self.help()
        elif args[0] == "info":
            self.info()
        elif args[0] == "exit":
            pass
        elif args[0] == "cd":
            os.chdir(args[1])
        elif args[0] == "settings":
            self.conf.settings[args[1]] = ' '.join(args[2:])
            with open('sliders.conf', 'wb') as handle:
                pickle.dump(self.conf.settings, handle)
        elif args[0] == "run":
            try:
                os.system(self.conf.settings["run."+args[1]])
            except IndexError:
                os.system(self.conf.settings["run"])
        elif args[0] == "edit":
            if len(args) < 2:
                print("Not enough arguments.")
            else:
                os.system(self.conf.settings["editor"]+" "+args[1])
        else:
            os.system(cmd)
        
        # Returns
        
        return self.conf
    
    def help(self):
        print("""
Help, eventually
""")
    def info(self):
        print("""
Info, eventually
""")
    
