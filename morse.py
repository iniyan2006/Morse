import time
import winsound
trans_dict = {
    "A":". -","B":'-...',"C":'-.-.',
    "D":"-..","E":'.',"F":'..-.',
    "G":'--.',"H":'....',"I":'..',
    "J":'.---',"K":'-.-',"L":'.-...',
    "M":'--',"N":'-.',"O":'---',
    "P":'.--.',"Q":'--.-',"R":'.-.',
    "S":'...',"T":'-',"U":'..-',
    "V":'...-',"W":'.--',"X":'-..-',
    "Y":'-.--',"Z":'--...'," ":' '
}
message = input("enter your message:\n")
trans = " ".join(trans_dict[c] for c in message.upper())
print(trans)
for c in trans:
    if c == '.':
        time.sleep(0.25)
        winsound.Beep(1500, 500)
    elif c == '-':
        time.sleep(0.25)
        winsound.Beep(1500, 900)
    elif c  == ' ':
        time.sleep(0.50)
