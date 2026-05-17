name=input("Please give me a name").strip()
while not name.isalpha():
    print("thats not a name")
    name=input("give me a proper name").strip()
print(f"{name} is awesome")
ask=input("and what is your name").strip()
if  ask.isalpha():
    print(f"{ask} is awesome and nice to meet you {ask}")
else:
    print(f"{ask} is not a real name are you joking")
    joking=input("write (yes/no)").strip()
    while joking not in ["yes","no"]:
          print("write only yes or no")
          joking=input("write (yes/no)")
    if joking == "yes":
        print("REALLY DUDE")
    else:
        print("DAMN i feel sorry for you")






