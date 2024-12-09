import requests
import filecmp
import os
import os.path
import time

with open("config/uidstart.txt", "r") as f:
    uidstart = int(f.read())

with open("config/uidend.txt", "r") as f:
    uidend = int(f.read())


print("Welcome to Miniclip YoMe! Grabber.")
time.sleep(1)
print()
print("Created by tuesday, telegram: @toasty2622 ")
print()
time.sleep(2)
CopyCounter = 0 
NeedToDelete = False
loop = True

while uidstart <= uidend:
    if os.path.exists('account_id_' + str(uidstart) + '_yome.png') == False:
        url = 'https://avatars-live.pool.miniclippt.com/avatars/pool/' + str(uidstart) + '-200.png'
        html = requests.get(url)

        with open('account_id_' + str(uidstart) + '_yome.png', 'wb') as r:
            r.write(html.content)

        if filecmp.cmp("premade/default.png",'account_id_' + str(uidstart) + '_yome.png', shallow = False):
            CopyCounter = CopyCounter + 1

        for i in range(1,21):
            if filecmp.cmp("premade/" + str(i) + ".png",'account_id_' +  str(uidstart) + '_yome.png', shallow = True):
                CopyCounter = CopyCounter + 1


        if CopyCounter >= 1:
            NeedToDelete = True
        else:
            NeedToDelete = False

        if NeedToDelete:
            os.remove('account_id_' + str(uidstart) + '_yome.png')

        print("Account ID: " + str(uidstart) + " Processed.")
    
    with open("config/uidstart.txt", "w") as g:
        g.write(str(uidstart))

    uidstart = int(uidstart)

    
    uidstart = uidstart + 1
    CopyCounter = 0
    

    

