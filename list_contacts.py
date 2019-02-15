# Build a list of calendar items
from exchangelib import Account, CalendarItem, Credentials,  \
Configuration, EWSDateTime, EWSTimeZone, Attendee, Mailbox, DELEGATE

from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


creds = Credentials(
username="ex.gasf.com\\Administrator", 
password="tech121login*")

config = Configuration(server='ex.gasf.com', credentials=creds)

a = Account(primary_smtp_address="Administrator@test.exchange.com",
autodiscover=False, 
config = config,
access_type=DELEGATE)


folder = a.root / 'AllContacts'
for p in folder.people():
    print(p)
""" for p in folder.people().only('display_name').filter(display_name='Dawn KK mathews').order_by('display_name'):
    print(p """)

""" # Folders have some useful counters:
z = "inbox total count : %s" % (a.inbox.total_count)
print(z)
print(a.inbox.child_folder_count)
print(a.inbox.unread_count)


# Dig deeper on indexed properties
sparse_items_phone_numbers = a.contacts.all().only('phone_numbers')
sparse_items_carphone = a.contacts.all().only('phone_numbers__CarPhone')
sparse_items_street = a.contacts.all().only('physical_addresses__Home__street')
all_contacts = a.contacts.all()

print(sparse_items_phone_numbers)
print(sparse_items_carphone)
print(sparse_items_street)
print(all_contacts) """