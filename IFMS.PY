# Module imports

import IEM as iem
import pickle

# Variable Definitons

__version__ = "Alpha"
__author__ = "Rodrigo, 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
clear = iem.cls
pause = iem.pause
# Function Definitions


def prompt_income():
    clear()
    try:
        income = int(input("On average, what is your monthly income? "))
    except ValueError:
        income = int(input("Please enter a valid number... "))
    finally:
        return income


def prompt_costs():
    clear()
    try:
        costs = int(input("Please enter your average 'Must spend' monthly costs... "))
    except ValueError:
        costs = int(input("Please enter a valid number..."))
    finally:
        if costs < income:
            return costs
        else:
            print("Costs cant be higher than income...")
            return False


def data_summary():
    print("Monthly income: {}\nMonthly Costs: {}".format(income, costs))


def savings_plan():
    clear()
    costs_percentage = (costs * 100) / income
    if costs_percentage < 10:
        savings = income * .4
        savings_percentage = "40%"
    elif costs_percentage => 10 and costs_percentage < 25:
        savings = income * .3
        savings_percentage = "30%"
    elif costs_percentage => 25 and costs_percentage < 50:
        savings = income * .2
        savings_percentage = "20%"
    elif costs_percentage => 50 and costs_percentage < 75:
        savings = income * .1
        savings_percentage = "10%"
    else:
        savings = income * .02
        savings_percentage = "2%"
    yearly_savings = savings * 12
    print("Your recomended savings plan is the following:")
    print("Monthly savings: {}\nThat's {} savings".format(savings, savings_percentage))
    print("Yearly savings: {}".format(yearly_savings))
    pause()

def read_file():
    clear()
    try:
        piggy_bank = pickle.load(open("Piggy Bank.data", "rb"))
    except FileNotFoundError:
        piggy_bank = []
        pickle.dump(piggy_bank, open("Piggy Bank.data", "wb"))
    finally:
        total_savings = 0
        deposits = 0
        for entry in piggy_bank:
            total_savings += entry
            deposits += 1
        print("You have saved a total of: {}\nTotal depposits made: {}".format(total_savings, deposits))
        pause()


def new_deposit():
    try:
        deposit = int(input("Please enter the amount to deposit... "))
    except ValueError:
        deposit = int(input("Please enter a valid amount... "))
    while deposit <= 0:
        deposit = int(input("Please enter a valid amount... "))
    deposit_confirmation = iem.confirm()
    if deposit_confirmation:
        piggy_bank.append(deposit)
        pickle.dump(piggy_bank, open("Piggy Bank.data", "wb"))
        print("Deposit Succesfull!")


def withdrawl():
    clear()
    print("THIS PROGRAM DOES NOT ENCOURAGE WITHDRAWLS FROM PIGGY BANK... Please confirm if you wish to proceed")
    if iem.confirm():
        clear()
        try:
            withdrawl = int(input("Please enter ammount to withdraw... "))
        except ValueError:
            print("Withdrawl ammount not valid, please try again.")
            return
        for deposit in piggy_bank:
            if withdrawl < deposit:
                new_deposit = deposit - withdrawl
                piggy_bank.remove(deposit)
                piggy_bank.append(new_deposit)
                


# Main Code
