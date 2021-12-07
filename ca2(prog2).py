# Hew Yi Wei Group MA8

password = input ("Enter your Password: ")

#print (len(password))

if password.isnumeric() or password.islower() or password.isupper() or 6 > len(password) < 20:

    print ("Invalid Password")

else:

    for a in password:
        if a == ' ':
            print ("Invalid Password")
            exit()

    print ("Valid Password")

    

    

        
