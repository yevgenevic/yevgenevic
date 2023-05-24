# from twilio.rest import Client
#
# # Twilio account SID and authentication token
# account_sid = 'AC1a503ca2ef4aa566b03ed883dc554c41'
# auth_token = '88f89a464dbd6bf72814b90fd7a16044'
#
# # Create a Twilio client
# client = Client(account_sid, auth_token)
# # Send an SMS
# message = client.messages.create(
#     body='Hello, this is a test message!',
#     from_='+12543554371',  # Your Twilio phone number
#     to='+998916484505'  # The recipient's phone number
# )
#
# print(f'Sent message SID: {message.sid}')
#
# import requests
#
# api_url = 'https://api.twilio.com/2010-04-01'
# api_key = '88f89a464dbd6bf72814b90fd7a16044'
# recipient_phone_number = '+998916484505'
# message = 'Hello, this is a test message!'
# response = requests.post(api_url, json={
#     'recipient': recipient_phone_number,
#     'body': message,
#     'type': 'text',
#     'sender': 'YourSenderID',
#     'api_key': api_key
# })
#
# if response.status_code == 201:
#     print('SMS sent successfully.')
# else:
#     print('Failed to send SMS. Error:', response.text)


# digits = [1,2,3]
# print(list(map(int,str(int("".join([str(i) for  i in digits]))+1))))


n = 11111111111111111111111111111101
res = 0
for i in range(32):
    res = res<<1
    bit = n%2
    res = res +bit
    n = n>>1
print(res)



