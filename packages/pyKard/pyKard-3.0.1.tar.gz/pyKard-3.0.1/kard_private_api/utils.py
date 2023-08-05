import uuid

def generateUUID():
    """ Generate a UUID, and return it. """
    return str(uuid.uuid4())

def generateVendorIdentifier(platform: str):
    """ Generate a vendor identifier for the platform, and return it. """
    vI = "%s:%s" % (platform, generateUUID())
    return vI

