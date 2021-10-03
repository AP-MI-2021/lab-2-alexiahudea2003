Problema 1

def get_largest_prime_below(n):
	for i in range (n-1,1,-1):
		ok=True
		for j in range (2,i//2,1):
			if i%j==0:
				ok=False
				break
		if ok==True:
			return i
			break
def test_get_largest_prime_below(n):
	assert get_largesr_prime_below(8) == 7
	assert get_largest_prime_below(12) == 11
 test_get_largest_prime_below()



Problema 2

def is_palindrome(n):
	y=n
	oglindit=0
	while n>0:
		c=n%10
		oglindit=oglindit*10+c
		n=n//10
	if y==oglindit:
		return print(True)
	else:
		return print(False)
def test_is_palindrome():
	assert is_palindrome(76) == False
	assert is_palindrome(77) == True
test_is_palindrome()
