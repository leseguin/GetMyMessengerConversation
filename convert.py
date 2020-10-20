import json
import datetime
import sys



def getMessages():
    with open('message_1.json') as json_file:
        dataa = json.load(json_file)
        messages = ""
        for m in dataa['messages']:
            if 'content' in m:
                name = m['sender_name'] + ' :'
                date = datetime.datetime.fromtimestamp(m['timestamp_ms']/1000).strftime('%d/%m/%Y %H:%M')
                contenu = m['content'].encode('latin1').decode('utf8')
                contenuu = contenu.encode('utf8')
                datee = date.encode('utf8')
                namee = name.encode('utf8')
                messageRecent = datee + " " + namee + " \n\n" + contenuu + "\n \n \n"
                messages =  messageRecent + messages
    return messages
     
    
    
     
fichier = open(sys.argv[1] + ".txt", "a")
fichier.write("Angelique \n\n\n")
fichier.write(getMessages())
fichier.close()

