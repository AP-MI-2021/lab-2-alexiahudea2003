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
	assert get_largesr_prime_below(8) == 7
	assert get_largest_prime_below(12) == 11
	assert get_largest_prime_below(30) == 29
def main():
	x=int(input("Care este numarul tau?)
	print(get_largest_prime_below(x))
if __name__ == '__main__':
  main()


#Problema 2

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
	assert is_palindrome(121) == True 
def main():
	x=int(input("Care este numarul tau?)
	print(get_largest_prime_below(x))
if __name__ == '__main__':
  main()
	
		    
#Problema 3
		    
def get_base_2(n):
	if n==0
		return "0"
	else:
		n=int(n)
		baza=2
		p=1
		y=0
		while n>=1:
		    	m=n%2
			y=y+m*p
		   	n=n//2
		    	p=p*10
		return y
def test_get_base_2():
	assert get_base_2(4) == 100
	assert get_base_2(5) == 101
	assert get_base_2(0) == 0 
def main():
	x=int(input("Care este numarul tau?)
	print(get_base_2(x))
if __name__ == '__main__':
  main()
	

