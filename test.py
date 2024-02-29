import subprocess as sp
import os
process = sp.Popen([f"sudo -S /home/chaitanya/Desktop/SIHPYQT/bash/disabletor.sh"], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
output, error = process.communicate("chai@1234".encode())
process.wait()
print(output.decode())
