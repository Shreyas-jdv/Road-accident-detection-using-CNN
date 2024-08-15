from twilio.rest import Client

account_sid = 'AC5eb73b8b89d51b0c5bde9d0feb941768'
auth_token = 'e3dc247165172cb7d6b10ae04323c115'
twilio_phone_number = '+14066377357'
recipient_phone_number = '+919325425933'


def message():
    client = Client(account_sid, auth_token)
    message1 = client.messages.create(
    body='Accident at route 65',
    from_=twilio_phone_number,
    to=recipient_phone_number
    )
    # return (message1.sid)
