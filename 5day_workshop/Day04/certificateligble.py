print("certificate eligble project")
user_attendance = input("Did u attend 5 day workshop? please input Y?N:").lower()
print(user_attendance)
if user_attendance=="n":
    print("Sorry! are u no elgible for cerificate")

elif user_attendance =="y":
    assignment = input("Did u complete all assignemt? please input Y/N:").lower()
    if assignment == "y":
        live_class = input("did u opened ur camera during class ? please input Y?N:").lower()
        if live_class == "y":
            camera_On = input("Did u do live class:Y?N:").lower()
            if camera_On == "y":
                print("YOUR are elible for certifcate")
            else:
                print("Your not eligblee")
        else:
            print("Your not eligible")
    else:
        print("You are not elible")
else:
    print("Enter the right keyword")
