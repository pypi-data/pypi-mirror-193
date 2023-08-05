import os
import json

class KardSettings:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.file = ".kard-login_%s-settings.json" % self.phone_number


        if os.name == 'nt':
            self.file_path = os.path.join('C:\\', 'Users', os.getlogin(), self.file)
        else:
            self.file_path = os.path.join(os.path.expanduser('~'), self.file)


    def getSettings(self):
        if not os.path.exists(self.file_path):
            self.saveSettings({
                "phoneNumber": self.phone_number
            })

        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def saveSettings(self, settings: dict):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)


    def getVendorIdentifier(self):
        return self.getSettings().get("vendorIdentifier")

    def setVendorIdentifier(self, vendorIdentifier: str|None):
        settings = self.getSettings()
        settings["vendorIdentifier"] = vendorIdentifier
        
        if vendorIdentifier is None:
            del settings['vendorIdentifier']
        
        self.saveSettings(settings)

    def getPlatform(self):
        return self.getVendorIdentifier().split(":")[0]

    def getPasscode(self):
        return self.getSettings().get("passcode")
    
    def setPasscode(self, passcode: str|None):
        settings = self.getSettings()
        settings["passcode"] = passcode
        
        if passcode is None:
            del settings['passcode']
        
        self.saveSettings(settings)

    def getAccessToken(self):
        return self.getSettings().get("accessToken")
    
    def setAccessToken(self, accessToken: str|None):
        settings = self.getSettings()
        settings["accessToken"] = accessToken
        
        if accessToken is None:
            del settings['accessToken']
        
        self.saveSettings(settings)
    
    def getRefreshToken(self):
        return self.getSettings().get("refreshToken")
    
    def setRefreshToken(self, refreshToken: str|None):
        settings = self.getSettings()
        settings["refreshToken"] = refreshToken
        
        if refreshToken is None:
            del settings['refreshToken']
        
        self.saveSettings(settings)

