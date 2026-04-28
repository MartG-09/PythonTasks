def dollar_to_naira(amount):
    amount = float(amount)

    if (type (amount) != float and type (amount) != int):
        return "invalid"
    converted_amount = amount * 1550

    return converted_amount

print(dollar_to_naira("ola"))


#
#def naira_exchange(dollar_amount):
#	if type (dollar_amount) != float and type (dollar_amount) != int:
#		return"invalid input"
#	result = dollar_amount * 1550
#	return result
#	
#print (naira_exchange(1.2))
