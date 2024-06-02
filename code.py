print("ceasar cipher")
mylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choice=int(input("1. Encryption 2.Decryption"))
if choice==1:
    name=input("Enter the plain text")
    name=name.lower()
    cipher=[]
    for k in range(0,len(name)):
        for j in range(0,len(mylist)):
            if name[k]==" ":
               continue
            if name[k]==mylist[j]:
               ans=(j+3)%26
               cipher.append(mylist[ans])
    for i in range(0,len(cipher)):
        print(cipher[i])
elif choice==2:
    cipher_txt=input("Enter the cipher text")
    plain=[]
    for k in range(0,len(cipher_txt)):
        for j in range(0,len(mylist)):
            if cipher_txt[k]==mylist[j]:
                if j>=3:
                   ans=(j-3)%26
                   plain.append(mylist[ans])
                else:
                   ans=((j-3)+26)%26
                   plain.append(mylist[ans])
    print(plain)
else:
    print("Choose correct option")
    
print("Vignere cipher")
mylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choice=int(input("1.Encryption 2.Decryption"))
key=input("Enter the key")
if choice==1:
    plain=input("Enter the plain text")
    plain=plain.lower()
    encrypt=[]
    n=len(plain)
    j=0
    for i in range(0,n):
        if plain[i]==" ":
            continue
        for k in range(0,len(mylist)):
            if plain[i]==mylist[k]:
                a1=k
        for k in range(0,len(mylist)):
            j=j%len(key)
            if key[j]==mylist[k]:
                a2=k
        ans=a1+a2
        ans1=ans%26
        encrypt.append(mylist[ans1])
        j+=1   
    print(encrypt)
if choice==2:
    cipher=input("Enter the cipher text")
    cipher=cipher.lower()
    decrypt=[]
    j=0
    for i in range(0,len(cipher)):
        for k in range(0,len(mylist)):
            if cipher[i]==mylist[k]:
                a1=k
        for k in range(0,len(mylist)):
            j=j%len(key)
            if key[j]==mylist[k]:
                a2=k
        ans=a1-a2
        if ans<0:
            ans1=ans+26
        else:
            ans1=ans%26
        j+=1
        decrypt.append(mylist[ans1])
    print(decrypt)
else:
    print("Choose correct operation")