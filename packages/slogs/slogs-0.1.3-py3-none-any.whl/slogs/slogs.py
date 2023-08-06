import colorama
from colorama import Fore, Style
from datetime import datetime


class slogs():
    def __init__(self, autoprint=True, log_saving=False):
        # set variables
        self.autoprint = autoprint
        self.log_saving = log_saving
        
        # init colorama
        colorama.init()
    
    def alert(self, content, parent=None):
        output = ""

        # add parent
        if parent != None:   # if parent is defined
            if type(parent) == dict:   # if parent is in default list
                output = parent["color"] + parent["label"]   # add parent
            else:
                output = Fore.BLUE + parent   # add parent
            output += " : "   # add ":"
        
        # add content
        output += Fore.YELLOW + content + Style.RESET_ALL

        if self.autoprint:   # print if autoprint is enable
            print(output)
        
        self.writeLog(content, parent)   # save log into log file
        
        return output

    def warn(self, content, parent=None):
        output = ""

        # add parent
        if parent != None:   # if parent is defined
            if type(parent) == dict:   # if parent is in default list
                output = parent["color"] + parent["label"]   # add parent
            else:
                output = Fore.BLUE + parent   # add parent
            output += " : "   # add ":"
        
        # add content
        output += Fore.YELLOW + Style.BRIGHT + "WARNING ! " + Style.NORMAL + content + Style.RESET_ALL
        
        if self.autoprint:   # print if autoprint is enable
            print(output)
        
        self.writeLog(content, parent)   # save log into log file
        
        return output
        
    def error(self, content, parent=None):
        output = ""

        # add parent
        if parent != None:   # if parent is defined
            if type(parent) == dict:   # if parent is in default list
                output = parent["color"] + parent["label"]   # add parent
            else:
                output = Fore.BLUE + parent   # add parent
            output += " : "   # add ":"
        
        # add content
        output += Fore.RED + Style.BRIGHT + "ERROR ! " + Style.NORMAL + content + Style.RESET_ALL
        
        if self.autoprint:   # print if autoprint is enable
            print(output)
        
        self.writeLog(content, parent)   # save log into log file
        
        return output
        
    def success(self, content, parent=None):
        output = ""

        # add parent
        if parent != None:   # if parent is defined
            if type(parent) == dict:   # if parent is in default list
                output = parent["color"] + parent["label"]   # add parent
            else:
                output = Fore.BLUE + parent   # add parent
            output += " : "   # add ":"
        
        # add content
        output += Fore.GREEN + content + Style.RESET_ALL
        
        if self.autoprint:   # print if autoprint is enable
            print(output)
        
        self.writeLog(content, parent)   # save log into log file
        
        return output
    
    def note(self, content, parent=None):
        output = ""

        # add parent
        if parent != None:   # if parent is defined
            if type(parent) == dict:   # if parent is in default list
                output = parent["color"] + parent["label"]   # add parent
            else:
                output = Fore.BLUE + parent   # add parent
            output += " : "   # add ":"
        
        # add content
        output += Fore.LIGHTBLACK_EX + content + Style.RESET_ALL
        
        if self.autoprint:   # print if autoprint is enable
            print(output)
        
        self.writeLog(content, parent)   # save log into log file
        
        return output
    
    def writeLog(self, content, parent):
        if not self.log_saving:   # if log saving isn't enabled
            return
        
        # write log
        with open("logs", "a") as f:
            if parent != None:
                f.write("[" + datetime.now().strftime("%Y_%m_%d-%H_%M_%S") + "] " + parent + " : " +content)
            else:
                f.write("[" + datetime.now().strftime("%Y_%m_%d-%H_%M_%S") + "] " + content)
                
            f.write("\n")   # jump line
        
        return True