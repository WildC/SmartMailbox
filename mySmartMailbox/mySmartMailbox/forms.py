import datetime

class Address(object):
    street=""
    street_no=""
    postcode=""
    city=""
    country=""

    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.street = ""
        self.street_no = ""
        self.postcode = ""
        self.city = ""
        self.country = ""

def initAddress(street,street_no,postcode,city,country):
    object=Address()
    object.street = street
    object.street_no = street_no
    object.postcode = postcode
    object.city = city
    object.country = country
    return object

class Recipient(object):
    last_name=""
    first_name=""
    address = Address()

    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.last_name = ""
        self.first_name = ""
        self.address = Address()

def initRecipient(first_name,last_name,street,street_no,postcode,city,country):
    object=Recipient()
    object.first_name = first_name
    object.last_name = last_name
    object.address = initAddress(street,street_no,postcode,city,country)
    return object


class Mailbox(object):
    id = 0
    status = False
    owner = ""
    shipment_no = ""
    recipient = ""
    assign_ts = datetime.datetime(1970, 1, 1, 1, 1, 1)

    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.id = 0
        self.status = False
        self.owner = ""
        self.shipment_no = ""
        self.recipient = Recipient()
        self.assign_ts = datetime.datetime(1970, 1, 1, 1, 1, 1)

def initMailbox(id, status, owner, shipment_no, first_name,last_name,street,street_no,postcode,city,country,assign_ts):
    object=Mailbox()
    object.id = id
    object.status = status
    object.owner = owner
    object.shipment_no = shipment_no
    object.recipient = initRecipient(first_name,last_name,street,street_no,postcode,city,country)
    object.assign_ts = assign_ts
    return object
