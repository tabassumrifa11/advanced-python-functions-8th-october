print("\033c")

number = int(input("Enter the number: "))
oddList = [i for i in range (1, number+1) if i % 2 != 0]


print("List of odd numbers:", oddList)



fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']

cap_fruits = [fruit.capitalize() for fruit in fruits]

print(cap_fruits)