print("Press1：Fahrenheit→centigrade")
print("Press2：centigrade→Fahrenheit")

temp=input("Please enter the function you want to select：")
guess=int(temp)

if guess==1 :
    temp=input("Please enter the Fahrenheit to be converted:")
    F=int(temp)
    C=(F-32)/1.8
    print("Fahrenheit："+str(F)+"F = centigrade："+str(C)+"℃")
elif guess==2 :
    temp=input("Please enter the centigrade to be converted:")
    C=int(temp)
    F=C*1.8+32
    print("centigrade："+str(C)+"℃ = Fahrenheit："+str(F)+"F")
else :
     print("Please check your input！")