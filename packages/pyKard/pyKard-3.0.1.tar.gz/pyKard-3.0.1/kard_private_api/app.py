import os

from . import graphql
from . import utils
from . import settings


class Kard:
    api_host = "api.kard.eu"

    def __init__(self, phoneNumber: str):
        self.phoneNumber = phoneNumber
        self.settings = settings.KardSettings(self.phoneNumber)

        self.platform = "android"
        self.vendorIdentifier = self.settings.getVendorIdentifier()
        if not self.vendorIdentifier:
            vI = utils.generateVendorIdentifier(platform=self.platform)
            self.vendorIdentifier = vI
            self.settings.setVendorIdentifier(self.vendorIdentifier)


        self.graphql = graphql.GraphQL(self.api_host, '/graphql', self.vendorIdentifier)

        self.karder = kard.karder.setup(self)


    def authenticate(self, forceApiAuth: bool=False):
        if not forceApiAuth:
            accessToken = self.settings.getAccessToken()
            if accessToken:
                self.graphql.setAccessToken(accessToken)
                return True

        query = "mutation androidInitSession($createUser: Boolean, $phoneNumber: PhoneNumber!,"\
                    " $platform: DevicePlatform, $vendorIdentifier: String!)"\
                "{ initSession(input: {createUser: $createUser, phoneNumber: $phoneNumber,"\
                    " platform: $platform, vendorIdentifier: $vendorIdentifier})"\
                " { challenge expiresAt errors { path message } }}"

        variables = {
            "platform": self.platform.upper(),
            "vendorIdentifier": self.vendorIdentifier,
            "phoneNumber": self.phoneNumber,
            "createUser": True
        }
        extensions = {}

        response = self.graphql.request(query, variables, extensions)
        if not response.get('initSession'):
            for error in response['errors']:
                if error['message'] == 'Variable $phoneNumber of type PhoneNumber! was provided invalid value':
                    raise kard.exceptions.InvalidPhoneNumberError("Invalid phone number %s" % self.phoneNumber)

        if response['initSession'].get('challenge') == 'OTP':
            return self.authenticateOTP()

        elif response['initSession'].get('challenge') == 'PASSCODE':
            return self.authenticatePasscode()

    def authenticateOTP(self):
        otp = input("Enter OTP: ")

        query = "mutation androidVerifyOTP($authenticationProvider: AuthenticationProviderInput, $code: String!,"\
                    " $phoneNumber: PhoneNumber!, $vendorIdentifier: String!)"\
                " { verifyOtp(input: {authenticationProvider: $authenticationProvider, code: $code, phoneNumber: $phoneNumber,"\
                    " vendorIdentifier: $vendorIdentifier})"\
                " { challenge accessToken refreshToken errors { path message } }}"
        variables = {
            "code": otp,
            "phoneNumber": self.phoneNumber,
            "vendorIdentifier": self.vendorIdentifier
        }
        extensions = {}

        response = self.graphql.request(query, variables, extensions)
        if not response.get('verifyOtp'): raise Exception("Invalid response %s" % response)

        if response['verifyOtp'].get('challenge') == 'PASSCODE':
            return self.authenticatePasscode()

        elif response['verifyOtp'].get('errors'):
            for error in response['verifyOtp']['errors']:
                if error['message'] == 'That code didn’t work':
                    raise kard.exceptions.InvalidOTPError("Invalid OTP %s" % otp)

    def authenticatePasscode(self):
        passcode = self.settings.getPasscode()
        if not passcode:
            passcode = input("Enter passcode: ")
            # Ask if user wants to save passcode?
            self.settings.setPasscode(passcode)


        query = "mutation androidSignIn($authenticationProvider: AuthenticationProviderInput,$passcode: String!,"\
                    " $phoneNumber: PhoneNumber!, $vendorIdentifier: String!)"\
                " { signIn(input: {authenticationProvider: $authenticationProvider,passcode: $passcode, phoneNumber: $phoneNumber,"\
                    " vendorIdentifier: $vendorIdentifier})"\
                " { accessToken refreshToken errors { path message } }}"
        variables = {
            "passcode": passcode,
            "phoneNumber": self.phoneNumber,
            "vendorIdentifier": self.vendorIdentifier
        }
        extensions = {}

        response = self.graphql.request(query, variables, extensions)
        if not response.get('signIn'): raise Exception("Invalid response %s" % response)

        if response['signIn'].get('accessToken'):
            self.settings.setAccessToken(response['signIn']['accessToken'])
            self.settings.setRefreshToken(response['signIn']['refreshToken'])
            
            self.graphql.setAccessToken(response['signIn']['accessToken'])
            return True

        elif response['signIn'].get('errors'):
            for error in response['signIn']['errors']:
                if error['message'] == 'Invalid passcode':
                    self.settings.setPasscode(None)
                    raise kard.exceptions.InvalidPasscodeError("Invalid passcode %s" % passcode)


from . import kard
