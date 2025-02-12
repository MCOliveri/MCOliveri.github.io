finger = []
i = 0
list_amount = int(input("amount of nums: "))

while i in range(list_amount):
    num = int(input("Give me a number: "))
    finger.insert(0, num)
    i += 1

print(finger)