'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
op=input("Press S for encrypting the message and anykey for decrypting the code:\t")
if op=='S':
#ENCRIPTION METHOD
    message= input("Enter The Message of ENCRIPTION:\t")
    print("YOUR ENCRIPTED MESSAGE:")
    for elm in message:
        asc=ord(elm)
        if asc<72:
            main=asc+40           #logic building
        else:
            main=asc-40
        temp=chr(main)
        
    
        print(temp,end='')
else:

#DECRIPTION METHOD
    cd=input("Enter the code for DECRIPTION:\t")
    for elm1 in cd:
        asc1=ord(elm1)            #logic building
        main1=asc1+40
        temp1=chr(main1)
        if temp1=="p":
            temp1=" "
        print(temp1,end='')
    