from distutils.log import error
import time
from datetime import datetime
import os
import os.path
def index(str,find):
    index = str.find(find)
    return index
def copy_passwd(str,index):
    passwd=str[index+1:]
    return passwd

def check_passwd(pas):
    lenn=False
    num,maj,min,=0,0,0
    if len(pas)>=8:
        lenn=True
    for i in pas:
        if i.isnumeric():
            num = num+1
        if i.isupper():
            maj=maj+1
        if i.islower():
            min=min+1
    return True if (maj!=0 and min!=0 and num!=0 and lenn) else False
def return_result():
    now = datetime.now()
    current_time = now.strftime("%H-%M")
    extension='.txt'
    filename = current_time+extension
    return filename
def return_data(file):
    f=open(os.path.join("results",file),'r+', encoding="utf8")
    return f
def main():
    global name
    todo=[]
    try:
     os.mkdir("results")
    except Exception:
     pass

    f=open(os.path.join("results","base.txt"),"r+",encoding='utf-8')
    main.name = return_result()
    fr=open( os.path.join("results",main.name),'w+', encoding="utf8")
    for line in f:
        line = line.rstrip()
        todo = line.split(':')
        try:
          if todo=="":
              pass
          mail = todo[0]
          passwd = todo[1]
        except:
            error
        if check_passwd(passwd):
            fr.write(f"{mail}:{passwd}\n")
    fr.close()
    f.close()

if __name__ == "__main__":
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(f"Done in {toc-tic:0.1f}")
