import time as t


user_pin = 1221
user_balance = 105000.90
user_name = "Mr. Neeraj"
print("Welcome To Indusind Bank", user_name, end = "\n\n")

choice = 6


while(True):
    print("\t\t1. Logout & Exit")
    print("\t\t2. View Account Balance")
    print("\t\t3. Withdraw Cash")
    print("\t\t4. Deposite Cash")
    print("\t\t5. Change Pin")
    print("\t\t6. Return Card")
    choice = int(input("Enter Number To Proceed > "))
    print("\n\n")

    if choice == 1:
        print("Exiting...")
        t.sleep(2)
        print("You Have Been Successfully Logged Out. Thank You!\n\n")
        break
    elif choice in (2,3,4,5,6):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please Enter Your 4-Digit PIN > "))

            if input_pin == user_pin:
                print("Account Authorized!\n\n")

                if choice == 2:
                    print("Loading Account Blanace...")
                    t.sleep(1)
                    print("Your Current Balance Is Rs.",user_balance, end = "\n\n\n")
                    break
                elif choice == 3:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1)

                    while(True):
                        withdraw_amt = float(input("Enter The Amount You Wish To Withdraw > "))

                        if withdraw_amt>user_balance:
                            print("Can't Withdraw Rs.", withdraw_amt)
                            print("Please Enter A Lower Amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            t.sleep(1)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance-=withdraw_amt
                                print("Amount Withdrawn - Rs.", withdraw_amt)
                                print("Remaining Balance - Rs.", user_balance, end ="\n\n\n")
                                break

                            else:
                                print("Cancelling Transaction...")
                                t.sleep(0.5)
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif choice == 4:
                        print("Loading Cash Deposite...")
                        t.sleep(1)

                        deposit_amt = float(input("Enter The Amount You Wish To Deposit > "))
                        print("Depositing Rs.", deposit_amt)
                        t.sleep(1)
                        confirm = input("Confirm? Y/N > ")
                        if confirm in ('Y', 'y'):
                            user_balance+=deposit_amt
                            print("Amount Deposited - Rs.", deposit_amt)
                            print("Updated Balance - Rs.", user_balance, end = "\n\n\n")
                        else:
                            print("Cancelling Transaction...")
                            t.sleep(0.5)
                            print("Transaction Cancelled!\n\n")

                        break

                elif choice == 5:
                    print("Loading PIN Change...")
                    t.sleep(1)

                    pin_new = int(input("Enter Your New PIN > "))

                    print("Changing PIN to", pin_new)
                    t.sleep(1)
                    confirm = input(("Confirm? Y/N > "))
                    if confirm in ('Y', 'y'):
                        user_pin = new_pin
                        print("PIN Changed Successfully! \n\n")
                    else:
                        print("Cancelling PIN Change...")
                        t.sleep(0.5)
                        print("Process Cancelled!\n\n")

                    break

                else:
                    print("Loading Card Return...")
                    t.sleep(1)

                    print("Returning Your ATM Card")
                    t.sleep(1)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        print("Card Returned Successfully! \n\n")
                    else:
                        print("Cancelling Process...")
                        t.sleep(0.5)
                        print("Process Cancelled!\n\n")

                break

            else:
                num_of_tries-=1
                print("PIN Incorrect! Number Of Tries Left >", num_of_tries, end = "\n\n")

        else:
            print("Exiting...")
            t.sleep(1.5)
            print("You Have Been Logged Out. Thank You!\n\n")
            break

    else:
        print("Invalid Input!")
        print("\t\t1. Enter 1 To Logout & Exit!")
        continue