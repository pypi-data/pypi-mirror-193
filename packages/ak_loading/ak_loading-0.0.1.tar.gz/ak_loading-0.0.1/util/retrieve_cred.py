import sys
if sys.platform=="win32":
    import keyring, getpass
else:
    import getpass

def getpwd(item, username):
    if sys.platform=="win32":
        pwd = keyring.get_password(item, username)
        if not pwd:
            print("Password is not saved in keyring.")
            pwd = getpass.getpass(f"Enter the password for {item} corresponding to Username:{username}: ")
            choice = input("Would you like to save this pwd to keyring?(Y|n): ")
            if choice.strip().lower() in ['', 'y','n']:
                if choice.strip().lower() != 'n':
                    keyring.set_password(item, username, pwd)
    else:
        pwd = getpass.getpass(f"Enter the password for {item} corresponding to Username:{username}: ")
    
    return pwd