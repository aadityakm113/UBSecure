import os
import subprocess as sp
import sys
import pysondb as ps

def makeDB():
    db = ps.getDb('bool.json')
    if(db.getByQuery({'name':'None'})):
        return
    else :
        db.addMany([
            {'name':'None', 'settings':{}, 'templates':['None']},
            {'name':'Network','settings':{}, 'templates':[]}
            ])
'''class access:
    def __init__(self, password):
        process = sp.Popen([f'sudo -S chown root:root /home/chaitanya/Desktop/progBackup/main.py'], stdin=sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(input=password.encode())
        process.wait()
        print(output.decode())
        p2  = sp.Popen([f'sudo chmod 4755 /home/chaitanya/Desktop/progBackup/main.py'], stdin=sp.PIPE, shell=True, stdout=sp.PIPE)
        output, error = p2.communicate(input=password.encode())
        p2.wait()
        print(output.decode())'''
        
class hardener:
    def __init__(self, su):
        '''with open('audit.txt','w') as f:
            p1=sp.run("lynis audit system",stdout=f,text=True, shell=True)'''
        self.password = su
        self.output = []
            
    def harden(self, temp):
        db = ps.getDb('bool.json')
        arr = db.getByQuery(query = {'name':temp})
        for key,value in arr[0]['settings'].items():
            if value['bool'] == 'True':
                if key == 'pwdp':
                    self.pswdpol()
                elif key == 'rmpk':
                    self.removePacks()
                elif key == 'ufwI':
                    self.installUFW()
                elif key == 'ufwE':
                    self.enableUFW()
                elif key == 'ufwD':
                    self.disableUFW()
                elif key == 'f2bE':
                    self.enablefail2ban()
                elif key == 'f2bD':
                    self.disablefail2ban()
                elif key == 'usbE':
                    print()
                elif key == 'ufwS':
                    self.statusUFW()
                elif key == 'ufwBP':
                    if(value['args']!='None'):
                        self.blockPort(value['args'])
                elif key == 'ufwAP':
                    if(value['args']!='None'):
                        self.allowPort(value['args'])
                elif key == 'ufwBI':
                    if(value['args']!='None'):
                        self.blockIP(value['args'])
                elif key == 'ufwAI':
                    if(value['args']!='None'):
                        self.allowIP(value['args'])
                elif key == 'torD':
                    self.distor()
                elif key == 'ufwDel':
                    print("Delete rule")
                elif key == 'sshp':
                    if(value['args']!='None'):
                        self.sshport(value['args'])
                elif key == 'sshPAE':
                	self.passauthE()
                elif key == 'sshPAD':
                	self.passauthD()
                elif key == 'sshRE':
                	self.sshRootE()
                elif key == 'sshRD':
                	self.sshRootD()
                elif key == 'sshXFE':
                	self.xforwardE()
                elif key == 'sshXFD':
                	self.xforwardD()
        return self.output

    def update(self):
        print("Updating the system")
        process = sp.Popen([f'sudo -S apt update'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        process = sp.Popen([f'sudo -S apt upgrade'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        #os.system('sudo apt update')
        #os.system('sudo apt upgrade')

    #needs fixing
    def pswdpol(self):
        print("Changing password policies")
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
        print("Removing orphan packages using Deborphan")
        '''os.system("sudo apt install deborphan")
        os.system("sudo deborphan")
        os.system("sudo apt --autoremove purge $(deborphan)")'''
        process = sp.Popen([f'sudo -S /home/chaitanya/Desktop/SIHPYQT/bash/deborphan.sh'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        
    def installUFW(self):
        print("Installing and enabling UFW")
        process = sp.Popen([f'sudo -S apt install ufw'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process2 = sp.Popen([f'sudo -S ufw enable'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())

    def enableUFW(self):
        print("Enabling UFW")
        process2 = sp.Popen([f'sudo -S ufw enable'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())
        
    def disableUFW(self):
        print("Disabling UFW")
        process2 = sp.Popen([f'sudo -S ufw disable'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())
        
    def statusUFW(self):
        print("UFW status")
        process = sp.Popen([f'sudo -S ufw status numbered'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def blockPort(self,port):
        print("Blocking port number ", port)
        process2 = sp.Popen([f'sudo -S ufw deny {port}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())

    def allowPort(self,port):
        print("Allowing port number ", port)
        process2 = sp.Popen([f'sudo -S ufw allow {port}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())

    def allowIP(self,ip):
        print("Whitelisting IP: ",ip)
        process2 = sp.Popen([f'sudo -S ufw allow from {ip}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())

    def blockIP(self,ip):
        print("Blacklisting IP: ", ip)
        process2 = sp.Popen([f'sudo -S ufw deny from {ip}'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process2.communicate(self.password.encode())
        process2.wait()
        self.output.append(output.decode())
    
    def enablefail2ban(self):
        print("Installing and enabling Fail2ban")
        process = sp.Popen([f'sudo -S apt -y install fail2ban'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process = sp.Popen([f'sudo systemctl enable fail2ban'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process = sp.Popen([f'sudo systemctl start fail2ban'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process = sp.Popen([f'sudo cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process = sp.Popen([f'sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        process = sp.Popen([f'sudo systemctl restart fail2ban'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def disablefail2ban(self):
        print("Disabling Fail2ban")
        process = sp.Popen([f'sudo -S apt-get purge --auto-remove fail2ban'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        
    def distor(self):
        process = sp.Popen([f"sudo -S /home/chaitanya/Desktop/SIHPYQT/bash/disabletor.sh"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
        sp.run(["/home/chaitanya/Desktop/SIHPYQT/bash/disabletor.sh"], shell=True)

    def sshport(self, value):
        print("Changing SSH port number to ",value)
        process = sp.Popen([f"sudo -S sed -i 's/#Port 2200/Port {value}/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def passauthE(self):
        print("Enabling SSH password authentication")
        process = sp.Popen([f"sudo -S sed -i 's/#PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def passauthD(self):
        print("Disabling SSH password authentication")
        process = sp.Popen([f"sudo -S sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def sshRootE(self):
        print("Enabling root login for SSH")
        process = sp.Popen([f"sudo -S sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def sshRootD(self):
        print("Disabling root login for SSH")
        process = sp.Popen([f"sudo -S sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def xforwardE(self):
        print("Enabling X11 forwarding for SSH")
        process = sp.Popen([f"sudo -S sed -i 's/X11Forwarding no/X11Forwarding yes/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())

    def xforwardD(self):
        print("Disabling X11 forwarding for SSH")
        process = sp.Popen([f"sudo -S sed -i 's/X11Forwarding yes/X11Forwarding no/g' /etc/ssh/sshd_config"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
        output, error = process.communicate(self.password.encode())
        process.wait()
        self.output.append(output.decode())
