# devs_money = 100
# dev_can_play_smash = False

# if devs_money > 10 and dev_can_play_smash:
#     print("Dev enters a smash tournament!")
# elif devs_money < 10 and dev_can_play_smash:
#     print("Dev is too poor to enter")
# else:
#     print("Dev just can't play smash")    

varMark = int(input("Enter your mark: "))
print (varMark)
if varMark > 85:
    print ("Distinction")
elif varMark >= 65 and varMark <= 85:
    print ("Pass")
else:
    print ("Fail")

# if varMark > 85:
#     print("Distinction")
# if 65 <= varMark <= 85:
#     print("Pass")    
# else:
#     print("Fail")