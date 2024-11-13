global path
path = "/etc/apt/apt.conf"

def write(username, password, proxy, port):
    filepointer = open(path, "a")
    filepointer.write(f"Acquire::http::proxy \"http://{username}:{password}@{proxy}:{port}/\";\n")
    filepointer.write(f"Acquire::https::proxy \"http://{username}:{password}@{proxy}:{port}/\";\n")
    filepointer.write(f"Acquire::ftp::proxy \"ftp://{username}:{password}@{proxy}:{port}/\";\n")
    filepointer.write(f"Acquire::socks::proxy \"socks://{username}:{password}@{proxy}:{port}/\";\n")
    filepointer.close()

def clean():
    with open(path,"r+") as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"http://" not in line and r"http://" not in line and r"ftp://" not in line and r"socks://" not in line:
                opened_file.write(line)
        opened_file.truncate()

if __name__=="__main__":
    write("username","password","proxy","port")
    #clean()
