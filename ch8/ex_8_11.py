# exercise 8-11
def send_messages(messages, sent_messages):
    """Print each message and move it to a list
    of sent messages"""
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)




sent_messages = []
messages_list = ['Hello!', 'What is happening?', 'Are you OK?']


send_messages(messages_list[:], sent_messages)

print("\nOriginal messages:")
print(messages_list)

print("\nSent messages:")
print(sent_messages)