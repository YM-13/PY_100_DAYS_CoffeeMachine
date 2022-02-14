MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"coffee": 18,
		},
		"cost": 1.5,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}


# TODO: 1. Print report of all coffee machine resources.
def report(current_resources, profit):
	for key in current_resources:
		print(f"{key.capitalize()}: {current_resources[key]}")
	print(f"Money: {profit['money']}")
# return f"{resources['water']}\n{resources['milk']}\n{resources['coffee']}"


# TODO: 2. Check resources sufficient to make drink order.
def check_resources(current_resources, need_resources):
	"""This function assumes that there are enough resources to prepare this drink. Данная функция предполагает наличие достаточного количества ресурсов для приготовления данного напитка"""
	for key in need_resources:
		if need_resources[key] > current_resources[key]:
			return f"Sorry there is not enough {key}."
	return True


# TODO: 3. Process coins.
def process_coins():
	print("Please insert coins.")
	money_quarters = int(input("How many quarters?: ")) * 0.25
	money_dimes = int(input("How many dimes?: ")) * 0.10
	money_nickles = int(input("How many nickles?: ")) * 0.05
	money_pennies = int(input("How many pennies?: ")) * 0.01
	return money_quarters + money_dimes + money_nickles + money_pennies


# TODO: 4. Check transaction successful?
def check_transaction(paid_money, drink_price):
	if paid_money < drink_price:
		return ("Sorry that's not enough money. Money refunded.")
	elif paid_money == drink_price:
		return paid_money
	else:
		print(f"Here is ${round((paid_money - drink_price), 2)} dollars in change.")
		return drink_price


# TODO: 5. Make the coffee (change resources).
def make_coffee(need_resources, current_resources):
	update_resources = {}
	for key in need_resources:
		update_resources[key] = current_resources[key] - need_resources[key]
	return update_resources


def coffee_machine_on():
	current_resources = {}
	if current_resources == {}:
		current_resources = resources

	profit = {
		"money": 0
	}
	machine_is_off = False
	while machine_is_off != True:
		wish = input("What would you like? (espresso/latte/cappuccino): ")

		need_resources = {}
		drink_price = 0
		paid_money = 0

		if wish == "report":
			print(f"{report(current_resources, profit)}")
		elif wish == "off":
			machine_is_off = True
		else:
			need_resources = MENU[wish]["ingredients"]
			drink_price = MENU[wish]["cost"]
			if check_resources(current_resources, need_resources) != True:
				print(check_resources(current_resources, need_resources))
			else:
				pass
			paid_money = process_coins()
			profit["money"] += check_transaction(paid_money, drink_price)
			current_resources = make_coffee(need_resources, current_resources)
			print(f"Here is your {wish}. Enjoy!")





coffee_machine_on()
