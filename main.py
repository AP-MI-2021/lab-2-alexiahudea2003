#Problema 1

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
def test_get_largest_prime_below():
	assert get_largest_prime_below(8) == 7
	assert get_largest_prime_below(12) == 11
	assert get_largest_prime_below(30) == 29
x=int(input("Care este numarul tau?"))
print(get_largest_prime_below(x))
	
#Problema 2

def is_palindrome(n):
	y=n
	oglindit=0
	while n>0:
		c=n%10
		oglindit=oglindit*10+c
		n=n//10
	if y==oglindit:
		return True
	else:
		return False
def test_is_palindrome():
	assert is_palindrome(76) == False
	assert is_palindrome(77) == True
	assert is_palindrome(121) == True
x=int(input("Care este numarul tau?"))
print(is_palindrome(x))

		    
#Problema 3
		    
def factor(n):
	factor=1
	for i in range(1,n+1):
		factor=factor*i
	return factor
def get_n_choose_k(n,k):
	return (factor(n)/(factor(k)*factor(n-k)))
def test_get_n_choose_k():
	assert get_n_choose_k(3,2) == 3
	assert get_n_choose_k(2,1) == 2
	assert get_n_choose_k(6,4) == 15
x=int(input("Care este primul numar?"))
y=int(input("Care este al doilea numar?"))
print(get_n_choose_k(x,y))

def main():
	print("introduceti datele:")
	
if __name__ == '__main__':
	main()


