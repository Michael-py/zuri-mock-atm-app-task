from datetime import datetime as dt
from random import randrange
from tqdm import tqdm
import time
import re

DATABASE = {1000000000:['John', 'Doe', 'john@doe.gmail.com', 1111, 50000 ]}




def register():

	print("\n" + " Kindly Fill The Form ".center(50, "*") + "\n")

	
	check = True

	while check:

		FIRST_NAME = input("Enter Your First Name: \n\n------------> ")
		LAST_NAME = input("Enter Your Last Name: \n\n------------> ")
		EMAIL = input("Enter Your Email Address: \n\n------------> ")

		try:
			PASSWORD = int(input("Enter a pin (4 Digits): \n\n------------> "))
			check = False

		except ValueError:
			print("You have made an invalid input\n")
			check = True

		try:
			if auth_reg(FIRST_NAME, LAST_NAME, EMAIL,PASSWORD) == True:
				check = True

			else:
				check = False

		except ValueError:
			print("\nYou have entered a wrong email. Please check and try again\n\n")
			check = True

	ACCOUNT_NUMBER = generate_account()

	BALANCE = 500

	print(f"\n------------> Your Account Number Is {ACCOUNT_NUMBER}\n")

	DATABASE[ACCOUNT_NUMBER] = [FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, BALANCE]

	time.sleep(.2)

	print("------------> Thank You For Opening an Account With Us.")
	print("------------> We Look To Giving You The Best Service\n")


	login()


def auth_reg(first, last, email, pass_word):

	STATUS = False

	if first.isnumeric() or last.isnumeric(): 
		print("Names can only be strings\n")
		STATUS = True

	if not re.match(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email):
		raise ValueError

	
	if len(str(pass_word)) > 4 or len(str(pass_word) < 4):

		print("\nPassword Longer than Required. Try Again\n")
		STATUS = True
		

	return STATUS



def login():

	print("\n" + " Kindly Enter Your Login Details ".center(50, "*") + "\n")

	trials = 3

	while trials > 0:

		try:
			ACCOUNT_NUMBER = int(input("Account Number: -----> "))
			PASSWORD = int(input("Pin: -----> "))

			USER_NAME = " ".join([DATABASE[ACCOUNT_NUMBER][0], DATABASE[ACCOUNT_NUMBER][1]])

			if ACCOUNT_NUMBER in DATABASE.keys() and PASSWORD == DATABASE[ACCOUNT_NUMBER][3]:
				actions(USER_NAME, ACCOUNT_NUMBER)
				break

			else:
				print("You Have Entered a Wrong Account Number or Password. Try Again\n")
				trials -= 1
				print(f"You Have {trials} Trials Left\n")


		except (ValueError, KeyError):
			print("Something has gone wrong".center(50))
			print("\n1.\tEnsure You Have Entered A Valid Account Number\n")
			print("2.\tEnsure You Have Entered the Right Pin\n")
			login()


		if trials == 0:
			handle_login_issues(ACCOUNT_NUMBER)


def handle_login_issues(acct_no):

	print("What Do You Want To Do?")
	print("\n\t1. Try Again\n\t2. Reset Pin\n\t4. Reach Out To Customer Care")

	while True:	
		try:
			
			action = int(input("------------> "))

			if action not in [1, 2, 3]:
				print("Wrong Choice")
				continue

			if action == 1:
				login()
				break

			elif action == 2:
				pin_reset(acct_no)
				break

			else:
				complaint()
				break

		except ValueError:
			print("Wrong Input")
			continue



def generate_account():

	EXCLUSION_LIST = []

	while True:
		ACCOUNT_GENERATED = randrange(1000000001, 9999999999)

		if ACCOUNT_GENERATED in EXCLUSION_LIST:
			continue

		else:
			print("Generating Account, Please Be Patient".center(50, "*").title() + "\n")
			for i in tqdm(range(int(10099999)), ascii=True, desc="Generating Account"):
				pass

			EXCLUSION_LIST.append(ACCOUNT_GENERATED)
			print("\nAccount Successfully Generated".center(50, "*").title())
			break

	return ACCOUNT_GENERATED




def current_time():

	currentTimeDate = dt.now()
	date = currentTimeDate.strftime("%A %d %B, %Y")
	time = currentTimeDate.strftime("%X")

	print("\n")

	return "\t\t".join([date,time])




def actions(user_name, acct_no):

	print("*"*50)
	print(current_time())

	print("\n")
	print(f"Welcome {user_name}".center(50, "*").upper())
	print("\nThese are the options available \n")
	print("\t1. Cash Withdrawal")
	print("\t2. Cash Deposit")
	print("\t3. Cash Transfer")
	print("\t4. Check Balance")
	print("\t5. Pin Reset")
	print("\t6. Complaint \n")
	print("\t7. Cancel Transaction \n")
	


	try:
		selectedOption = int(input("Please select an option: "))

		if selectedOption == 1:
			withdraw(acct_no)

		elif selectedOption == 2:
			deposit(acct_no)

		elif selectedOption == 3:
			transfer(acct_no)

		elif selectedOption == 4:
			balance(acct_no)

		elif selectedOption == 5:
			pin_reset(acct_no)

		elif selectedOption == 6:
			complaint(user_name, acct_no)

		elif selectedOption == 7:
			time.sleep(0.5)
			print("\n Thank You For Banking With Us. Do Have a Nice Day.\n")
			time.sleep(0.5)


		else:
			print("Invalid Selection")
			actions(user_name, acct_no)

	except ValueError:
		print("Invalid Selection")
		actions(user_name, acct_no)


def withdraw(acct_no):
	
	try:
		withdraw_amount = int(input("How Much Do You Want To Withdraw?\nNote: Must Be In Multiples of #500 \n\n------------> "))

		if withdraw_amount % 500 != 0:
			print("\nAmount Must be in Multiples of #500\n")
			time.sleep(0.5)
			withdraw(acct_no)

		elif withdraw_amount > DATABASE[acct_no][-1]:
			print("\nYou Have Insufficient Balance\n")
			balance(acct_no)

		else:

			print(f"\nWithdrawing {withdraw_amount:#,.2f} \n")
			for i in tqdm(range(int(10000000)), ascii=True, desc="Processing Withdraw Request..."):
				pass

			print("\nTransaction successful\nPlease take your cash\n")

			DATABASE[acct_no][-1] -= withdraw_amount
			balance(acct_no)

	except ValueError:
		print("Wrong Input")
		withdraw(acct_no)




def deposit(acct_no):
	try:
		deposit_amount = int(input("How Much Do You Want To Deposit?\nNote: Must not be greater than #50,0000\n\n------------> "))

		if deposit_amount not in range(500, 50001, 500):
			print("\nYou cannot not make this deposit. Enter a Value between #500 and #50,000\n")

		else:

			print(f"\nDepositing {deposit_amount:#,.2f} \n")
			for i in tqdm(range(int(10000000)), ascii=True, desc="Processing Deposit Request..."):
				pass

			time.sleep(1)

			print("\nTransaction successful\n")

			DATABASE[acct_no][-1] += deposit_amount
			balance(acct_no)

	except ValueError:
		print("Wrong Input")
		deposit()




def transfer(acct_no):
	try:
		beneficiary = int(input("Enter Beneficiary Account Number\n\n------------> "))
		transfer_amount = int(input("How Much Do You Want To Transfer?\nNote: Must not be greater #5,000,0000\n\n------------> "))

		if len(str(beneficiary)) > 10 or len(str(beneficiary)) < 10:
			time.sleep(2)
			print("\nWrong Account Number, Check and Try again\n")
			transfer(acct_no)

		elif transfer_amount > DATABASE[acct_no][-1]:
			print("\nYou Have Insufficient Balance to make this transfer\n")
			transfer(acct_no)


		else:
			print(f"\nTransfering {transfer_amount:#,.2f} \n")
			for i in tqdm(range(int(10000000)), ascii=True, desc="Processing Deposit Request..."):
				pass

			print("Transaction successful\n")

			DATABASE[acct_no][-1] -= transfer_amount
			balance(acct_no)

	except ValueError:
		print("Wrong Input")
		transfer(acct_no)




def balance(acct_no):

	balance_amount = DATABASE[acct_no][-1]

	print(f"\n\nYour Current Balance is #{balance_amount:#,.2f}\n\n")
	print("*"*50 + "\n")

	USER_NAME = " ".join([DATABASE[acct_no][0], DATABASE[acct_no][1]])

	time.sleep(1)

	actions(USER_NAME, acct_no)




def pin_reset(acct_no):

	try:
		new_pin = int(input("Enter a new pin: -----> "))
		confirm_new_pin = int(input("Confirm pin: -----> "))

		if new_pin != confirm_new_pin:
			print("Pins do not match, retry")
			pin_reset(acct_no)

		else:

			DATABASE[acct_no][3] = confirm_new_pin

			time.sleep(2)

			print("Pin Reset Successfully")

			login()

	except ValueError:
		print("Wrong Input")
		pin_reset(acct_no)


def complaint(user_name, acct_no):

	print(f"{user_name}".center(50, "*"))
	print("\nThank You For contacting Us.\n\n")

	issue = input("\nDrop Your Complaint > ")

	print(f"\nComplaint Receive, We wlll reply you via your email: {DATABASE[acct_no][2]}".title())



def main():

	print("\n")
	print(" welcome to Cool Butter Bank ".center(50, "#").upper() + "\n")
	print(" do you have an account with us? ".center(50, "*").title() + "\n")

	while True:
		answer = input("(y/N: -----> ")

		if answer.lower() not in ['y', 'n']:
			print("You have made an invalid input")
			continue
		break

	if answer.lower() == 'y':
		login()

	else:
		register()


if __name__ == '__main__':
	main()


