def show_messages(msgs):
    for msg in msgs:
        print(msg)

def send_messages(msgs):
    sent_messages = []
    while msgs:
        send_msg = msgs.pop()
        print(f"current msg: {send_msg}")
        sent_messages.append(send_msg)
    for sent_msg in sent_messages:
        print(sent_msg)



txt_msgs = ["how's your day.","what's up man","How was the event?","lets go somewhere"]

send_messages(txt_msgs[:])
print("-----------")
show_messages(txt_msgs)