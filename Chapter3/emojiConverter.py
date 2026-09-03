# mini project - Emoji Converter
msg = input("Enter your messaage: ")

msg = msg.replace(":)","🙂")
msg = msg.replace(":(","😞")
msg = msg.replace(":D", "😁")
msg = msg.replace(";)", "😉")
msg = msg.replace("$|", "😘")

print(msg)