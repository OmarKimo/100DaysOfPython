PROFIT = 0  # $

resources = {
    "Water": 300,   # ml
    "Milk": 200,    # ml
    "Coffee": 100,  # g
}

UNITS = {
    "Water": 'ml',  
    "Milk": 'ml',   
    "Coffee": 'g',  
}

MENU = {
    "espresso": {
        "Water": 50,   # ml
        "Milk": 0,    # ml
        "Coffee": 18,  # g
        "Money": 1.5      # $
    },
    "latte": {
        "Water": 200,   # ml
        "Milk": 150,    # ml
        "Coffee": 24,  # g
        "Money": 2.5      # $
    },
    "cappuccino": {
        "Water": 250,   # ml
        "Milk": 100,    # ml
        "Coffee": 24,  # g
        "Money": 3      # $
    }
}

# see if resources have enough for order
def can(dic):
    for key in resources.keys():
        if resources[key] < dic[key]:
            return key
    return None

# remove order requirements from resources
def getOrder(dic, money):
    global PROFIT
    for key in resources.keys():
        resources[key] -= dic[key]
    PROFIT += dic['Money']
    money -= dic['Money']
    return money

def report():
    for key, item in resources.items():
        print(f"{key}: {item}{UNITS[key]}") 
    print(f"Money: ${PROFIT}")
