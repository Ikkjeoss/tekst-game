print("Welcome to ikk text game")
name = input("Lets get startet. chose a nick name \n")
name = name.strip() 
print("this game dont have any mining just play\n\n")
try:
   q1 = float(input("let start the game. first question is, how much is 1 + 1 ? \n\n\n"))
   if q1 == 2:
      print("no it is 3\n")
   elif q1 == 3:
      print("you right\n")
   elif q1 > 3:
    print("you are an idiote\n")
except ValueError:
 print("?\n")
q2 = input("if your fateher is at work wher is your mother \n a) home \n b) work \n c) in my paket\n").strip()
if q2 == "a":
    print("ok thats good, but it is wrong\n")
elif q2 == "b":
    print("why you let your mother work , thats wrong\n")
elif q2 == "c":
    print("ofcurs she is in my paket , ritgh\n")
def goodstatu():
   answer1 = input("do you wanna continiu ? pres \"y\" to continiu pres \"n\" to go out ")
   if answer1 == "y":
       print("ok\n")
   elif answer1 == "n":
       exit()
goodstatu()
q3 = input(f"ok {name} lets get sirios, do you have gf/bf? \n a) yes \n b) no\n ").strip()
if q3 == "a":
    print("you lucki basterd.\n")
elif q3 == "b":
    
    print(":(\n")


q4 = input(" If two monkeys stole a banana from each other at the same time, what would be the result? ").strip().capitalize()
if q4 == "Ape-ricious chaos":
    print("thats ritgh\n")   
else:
    print(" it is \"Ape-ricious chaos\"")
q5 = input("what kinde musick do you like ? \n")
print("i dont give fuck\n")

q6 = input("is your eating system is god \n a) yes\n b) no\n").strip()

if q6 == "a":
   print("good but dont eat to much, and go to gym\n")
elif q6 == "b":
   print("if you can eat go to dockter, but if you have mentel isuse go ot your pysckiatris \n")


q7 = input("what coler is  your bugati\n a)brawn\n b)brawn\n c)brawn\n").strip()

if q7 == "a" or "b" or "c":
   print("nice")

q8 = input("what dose the life mine \n a) nothing\n b) something\n c) idk man\n").strip()
if q8 == "a":
   print("i feel you man")
elif q8 == "b":
   print("nice man keep going")
elif q8 == "c":
   a = input("are you lost | yes or no ?").strip()
   if a == "yes":
      print("sory man i cant do anything from here but go out and talk to someone")
   elif a == "no":
      print("keep going man")

q9 = input("how big it is?\n a)unnder 10cm \n b)betwin 10cm to 15cm \n c)over 15cm \n d) i am a women\n")
if q9 == "a":
   print("to smal")
elif q9 == "b":
   print("avreg")
elif q9 == "c":
   print("to big no need for it")
elif q9 == "d":
   print("ok??")

q10 = input("did you like the game?\n a)yessssssss\n b)no \n")
if q10 == "a":
   print("thanks for playing")

elif q10 == "b":
   print("go cry about it")

#thanks for playing and i am a byginer in coding i do stupide projeckts.


