import re
import sys

def remove_ansi_escape_codes():
    with open("audit.txt", 'r') as file:
        content = file.read()
        # Remove ANSI escape codes using regular expressions
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        cleaned_content = ansi_escape.sub('', content)
        with open("audit.txt", 'w') as file:
            file.write(cleaned_content)

def sysinf():
    details=[]
    p1 = r'Program version'
    p2 = r'Operating system'
    p3=r'ernel version'
    p4=r'Hardware platform'
    p5=r'Hostname'
    with open('audit.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if re.search(p1,line) or re.search(p2,line) or re.search(p3,line) or re.search(p4,line) :
            index=re.search(":",line)
            details.append((line[index.start()+1:]).strip())
        elif re.search(p5,line):
            details.append((line[index.start()+1:]).strip())
            break
    return details
    
def scaninf():
    details=[]
    p1 = r'Hardening index'
    p2 = r'Tests performed'
    p3 = r'Plugins enabled'
    
    with open('audit.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if re.search(p2,line) or re.search(p3,line) :
            index=re.search(":",line)
            details.append((line[index.start()+1:]).strip())
            if re.search(p3,line):
                break
        elif re.search(p1,line):
            brac = re.search(r'\[',line)
            index=re.search(":",line)
            details.append((line[index.start()+1:brac.start()]).strip())
            
    return details

def suggestions():
    with open('audit.txt','r') as f:
        f = f.read()
        # Search for 'Suggestions (42):' using a regular expression
        pattern = r'Suggestions'
        end_pattern=r'Follow-up:'
        match1 = re.search(pattern, f)
        match2 =re.search(end_pattern, f)
        return (f[match1.start():match2.start()])

def warnings():
    with open('audit.txt','r') as f:
        f=f.read()
        pattern = r'Warnings'
        end_pattern = r'Suggestions'
        if re.search(pattern, f):
            match1 = re.search(pattern, f)
            match2 =re.search(end_pattern, f)
            return f[match1.start():match2.start()]
        else:
            return "Great! No warnings."
