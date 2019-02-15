""" from exchangelib import Credentials, Account, DELEGATE
import sys

username = 'Administrator@test.exchange.com'
password = 'tech121login*'
credentials = Credentials(username, password)
account = Account('Administrator@test.exchange.com', credentials=credentials, autodiscover=True, 
access_type=DELEGATE)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)

sys.exit("I am getting the heck out of here!") """


from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
HTMLBody, Build, Version

from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

import sys

creds = Credentials(
username="ex.gasf.com\\Administrator", 
password="tech121login*")

config = Configuration(server='ex.gasf.com', credentials=creds)

account = Account(
primary_smtp_address="Administrator@test.exchange.com",
autodiscover=False, 
config = config,
access_type=DELEGATE)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)

sys.exit("I am getting the heck out of here!")
