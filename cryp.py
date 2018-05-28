class crypto():
    def caesar(self):
        cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
        if cryptMode not in ['E','D']:
            print("Error: mode is not Found!"); raise SystemExit
        startMessage = input("Write the message: ").upper()
        try:rotKey = int(input("Write the key: "))
        except ValueError: print("Only numbers!"); raise SystemExit
        def encryptDecrypt(mode, message, key, final = ""):
            for symbol in message:
                if mode == 'E':
                    final += chr((ord(symbol) + key - 13)%26 + ord('A'))
                else:
                    final += chr((ord(symbol) - key - 13)%26 + ord('A'))
            return final
        print("Final message:",encryptDecrypt(cryptMode, startMessage, rotKey))
    def RSA(self):
        import rsa
        (pub,priv)=rsa.newkeys(1024)
        print("\n"+str(pub))
        print("\n"+str(priv)+"\n")
        with open("crypt.py","w") as crypt:
            crypt.write('''
        import rsa 
        pub_key=int(input("Write the PublicKey: "))
        text=input("\\n[*] Write the text:\\n\\n[text] >> ")
        message=text.encode("utf8")
        crypt=rsa.encrypt(message,rsa.PublicKey(pub_key,65537))
        with open("text_crypt.txt","wb") as w:
            w.write(crypt)
            print("\\n[*] Crypt-text:\\n\\n"+str(crypt)+"\\n\\n[+] File: 'text_crypt.txt' successfully saved!\\n")
        ''')
        print("\n[+] File: 'crypt.py' successfully saved!")
        with open("key.py","w") as key:
            key.write('''
        import rsa
        file=input("Write the filename: ")
        with open(file,"rb") as r:
            read=r.read()
            message=rsa.decrypt(read,rsa.'''+str(priv)+''')
            print("\\n[*] Decrypted text:\\n\\n[text] << "+str(message.decode("utf8"))+"\\n")
        ''')
        print("[+] File: 'key.py' successfully saved!\n")
    def AES(self):
        import pyAesCrypt
        from os import remove
        from os.path import splitext
        cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
        if cryptMode not in ['E','D']:
            print("Error: mode is not Found!"); raise SystemExit
        fileName = input("Write the file: ")
        paswFile = input("Write the password: ")
        bufferSize = 64*1024
        def encryptDecrypt(mode, file, password, final = ""):
            if mode == 'E':
                try:
                        pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
                        remove(file)
                except FileNotFoundError: return "[x] File not found!"
                else: return "[+] File '"+str(file)+"' overwritten!"
            else:
                try:
                    pyAesCrypt.decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
                    remove(file)
                except FileNotFoundError: return "[x] File not found!"
                except ValueError: return "[x] Password is False!"
                else: return "[+] File '"+str(splitext(file)[0])+".crp' overwritten!"
        print(encryptDecrypt(cryptMode, fileName, paswFile))
if __name__=='__main__':
    k = int(input("Vibirite shifr: 1 - caesar, 2 - RSA, 3 - AES: "))
    if k==1:
        m=crypto()
        m.caesar()
    elif k==2:
        m=crypto()
        m.RSA()
    elif k==3:
        m=crypto()
        m.AES()
    else:
        print("Vveden neverniy kod")