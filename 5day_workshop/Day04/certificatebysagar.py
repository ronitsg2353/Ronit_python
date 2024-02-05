print("Certificate Eligibility Checker")

status = input("Enter Y/N, Y(When you attended all class, N(If any Gap)) = ").lower()

#lower function transform the text to lowercase

# if N == "n":
if status == "n":
    print("Not eligible for certificate")

elif status == "y":
    assignment = input("Did you completed all assignment? (Y/N) = ").lower()
    if assignment == "y":
        live = input("Did you completed all live classes? (Y/N) = ").lower()
        if live == "y":
            camera_on = input("Did you turn on camera? (Y/N) = ").lower()
            if camera_on == "y":
                print("Eligible for certificate")
            else:
                print("Not eligible")
        else:
            print("Not eligible")
    else:
        print("Not eligible")

else:
    print("Enter right keyword")