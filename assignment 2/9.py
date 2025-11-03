import random

def GenerateOTP():
    return random.randint(0, 9999)

def Otp(secret):
    guess = int(input("Enter the OTP: "))
    attempts = 3
    for i in range (attempts):
        while attempts != 0:
            if guess != secret:
                attempts -= 1
                print(f"Incorrect OTP. You have {attempts} attempts left.")
                if attempts == 0:
                    print("No attempts left. OTP verification failed.")
                    return 
                guess = int(input("Re-enter the OTP: "))
            else:
                print("OTP verified successfully!")
                return True

secret = GenerateOTP()
print(f"Generated OTP (for testing purposes): {secret}")
guessotp = Otp(secret)
if guessotp:
    print("Access Granted")
else:
    print("Access Denied")
    
