n = input(f"\nTell me a number! ")

n = int(n)

print(f"\n")

def number_in_letters(num):

	match num:
		case 0: 
			print("zero")
		case 1:
			print("one")
		case 2:
			print("two")
		case _:
			print("other")

number_in_letters(n)


print(f"\n")


