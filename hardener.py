import os
import subprocess as sp
import sys
import pysondb as ps

def makeDB():
    db = ps.getDb('bool.json')
    db.addMany([{'name':'pwdp', 'bool':'None', 'args':'None'},
                {'name':'rmpk', 'bool':'None', 'args':'None'},
                {'name':'ufwI', 'bool':'None', 'args':'None'},
                {'name':'ufwE', 'bool':'None', 'args':'None'},
                {'name':'ufwD', 'bool':'None', 'args':'None'},
                {'name':'f2bE', 'bool':'None', 'args':'None'},
                {'name':'f2bD', 'bool':'None', 'args':'None'},
                {'name':'usbE', 'bool':'None', 'args':'None'},
                {'name':'ufwS', 'bool':'None', 'args':'None'},
                {'name':'ufwBP', 'bool':'None', 'args':'None'},
                {'name':'ufwAP', 'bool':'None', 'args':'None'},
                {'name':'ufwAI', 'bool':'None', 'args':'None'},
                {'name':'ufwBI', 'bool':'None', 'args':'None'},
                {'name':'ufwDel', 'bool':'None', 'args':'None'},
                {'name':'torD', 'bool':'None', 'args':'None'}])
class access:
    def __init__(self, password):
        pin = password
        process = sp.Popen([f'sudo -S chown root:root /home/chaitanya/Desktop/prog/SIH PYQT/main.py'], stdin=sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(input=pin.encode())
        process.wait()
        print(output.decode())
        p2  = sp.Popen([f'sudo -S chmod 4755 /home/chaitanya/Desktop/prog/SIH PYQT/main.py'], stdin=sp.PIPE, shell=True, stdout=sp.PIPE)
        output, error = p2.communicate(input=pin.encode())
        p2.wait()
        print(output.decode())
        
class hardener:
    def __init__(self):
        with open('audit.txt','w') as f:
            p1=sp.run("lynis audit system",stdout=f,text=True, shell=True)
            
    def harden(self):
        self.update()
        arr = db.getAll()
        for i in arr:
            if i['bool'] == 'True':
                if i['name'] == 'pwdp':
                    self.pswdpol()
                elif i['name'] == 'rmpk':
                    self.removePacks()
                elif i['name'] == 'ufwI':
                    self.installUFW()
                elif i['name'] == 'ufwE':
                    self.enableUFW()
                elif i['name'] == 'ufwD':
                    self.disableUFW()
                elif i['name'] == 'f2bE':
                    self.enablefail2ban()
                elif i['name'] == 'f2bD':
                    self.diablefail2ban()
                elif i['name'] == 'usbE':
                    print()
                elif i['name'] == 'ufwS':
                    self.statusUFW()
                elif i['name'] == 'ufwBP':
                    self.blockPort(i['args'])
                elif i['name'] == 'ufwAP':
                    self.allowPort(i['args'])
                elif i['name'] == 'ufwBI':
                    self.blockIP(i['args'])
                elif i['name'] == 'ufwAI':
                    self.allowIP(i['args'])
                elif i['name'] == 'torD':
                    self.distor()
                elif i['name'] == 'ufwDel':
                    print("Delete rule")

    def update(self):
        os.system('sudo apt update')
        os.system('sudo apt upgrade')

    def pswdpol():
        os.system('sudo apt -y install libpam-pwquality cracklib-runtime')
        # Define the path to the file
        file_path = "/etc/pam.d/common-password"
        # Open the file in read mode to read its contents
        with open(file_path, "r") as file:
            file_contents = file.readlines()
        # Modify the contents as needed (for example, replace "old_text" with "new_text")
        modified_contents = [line.replace("password   requisite   pam_pwquality.so retry=3", "password requisite pam_pwquality.so retry=3 minlen=8 maxrepeat=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 difok=3 gecoscheck=1 reject_username enforce_for_root") for line in file_contents]
        # Open the file in write mode to overwrite its contents
        with open(file_path, "w") as file:
            file.writelines(modified_contents)
        
    def removePacks(self):
        os.system("sudo apt install deborphan")
        os.system("sudo deborphan")
        os.system("sudo apt --autoremove purge $(deborphan)")
        
    def installUFW():
        process = sp.Popen([f'sudo -S apt install ufw'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(password.encode())
        process.wait()
        print(output.decode())
        process2 = sp.Popen([f'sudo -S ufw enable'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())
        
    def disableUFW():
        process2 = sp.Popen([f'sudo -S ufw disable'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())
        
    def statusUFW():
        process = sp.Popen([f'sudo -S ufw status numbered'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(password.encode())
        process.wait()
        print(output.decode())

    def blockPort(port):
        process2 = sp.Popen([f'sudo -S ufw deny {port}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())

    def allowPort(port):
        process2 = sp.Popen([f'sudo -S ufw allow {port}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())

    def allowIP(ip):
        process2 = sp.Popen([f'sudo -S ufw allow from {ip}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())

    def blockIP(ip):
        process2 = sp.Popen([f'sudo -S ufw deny from {ip}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(password.encode())
        process2.wait()
        print(output.decode())
    
    def enablefail2ban():
        os.system('sudo apt install fail2ban')
        os.system('sudo systemctl enable fail2ban')
        os.system('sudo systemctl start fail2ban')
        os.system('sudo cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local')
        os.system('sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local')
        os.system('sudo systemctl restart fail2ban')
    
    def disablefail2ban():
        os.system('sudo apt-get purge --auto-remove fail2ban')
        
    def distor():
        p1=sp.run("sudo systemctl disable tor.service",stdout=sp.PIPE,text=True,shell=True)
        print(p1.returncode)
        if p1.returncode==0:
            print("success")
        elif p1.returncode==1:
            p1=sp.run("sudo systemctl disable tor.service",stdout=sp.PIPE,text=True,shell=True)
