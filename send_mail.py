
from exchangelib import Account, Message, CalendarItem, Credentials,  \
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

# You can also send emails. If you don't want a local copy:
m = Message(
    account=a,
    subject='Daily motivation',
    body='All bodies are beautiful',
    to_recipients=[
        Mailbox(email_address='Administrator@test.exchange.com'),
        Mailbox(email_address='admin@mail.gasf.com'),
    ],
    cc_recipients=['muneebkt@gmail.com', 'denice@example.com'],  # Simple strings work, too
    bcc_recipients=[
        Mailbox(email_address='icecreamcastlee8@gmail.com'),
        'felicity@example.com',
    ],  # Or a mix of both
)
if m.send():
   print ('mail send successfully')