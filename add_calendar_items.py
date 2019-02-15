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

tz = EWSTimeZone.timezone('Europe/Copenhagen')
year, month, day = 2019, 2, 20
calendar_items = []
for hour in range(7, 17):
    calendar_items.append(CalendarItem(
        start=tz.localize(EWSDateTime(year, month, day, hour, 30)),
        end=tz.localize(EWSDateTime(year, month, day, hour + 1, 15)),
        subject='Test item',
        body='Hello from Python',
        location='devnull',
        categories=['foo', 'bar'],
        required_attendees = [Attendee(
            mailbox=Mailbox(email_address='Administrator@test.exchange.com'),
            response_type='Accept'
        )]
    ))

# Create all items at once
return_ids = a.bulk_create(folder=a.calendar, items=calendar_items)
print(return_ids)