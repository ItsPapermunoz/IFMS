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
    pause()
    print("Monthly savings: {}\nThat's {} savings".format(savings, savings_percentage))
    print("Yearly savings: {}".format(yearly_savings))
    

# Main Code
