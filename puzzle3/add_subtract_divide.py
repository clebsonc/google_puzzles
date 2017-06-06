def solve(number):
	ans = 0
	while number != 1:
		if number == 3:
			ans += 2
			break
		elif number %2 == 0:
			ans += 1 
			number /= 2
		elif number & 3 == 3:
			ans += 1
			number +=1
		elif number&1==1:
			ans += 1
			number -= 1


def answer(number):
	number = int(number)
	return solve(number)

if __name__ == "__main__":
	number = input()
	print answer(number)


