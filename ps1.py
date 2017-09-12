###### this is the first .py file ###########

####### write your code here ##########

binary_data = input("Enter the binary data\n")
flag ='0101'
even= '1'
even_parity= int(str(binary_data)+ str(even))
even_parity_flag= int(str(binary_data)+ str(even)+ str(flag))
odd= '0'
odd_parity= int(str(binary_data)+ str(odd))
odd_parity_flag= int(str(binary_data)+ str(odd)+ str(flag))

def digitsum(binary_data):
	total=0
	for letter in str(binary_data):
		total+=int(letter)
		print(total)
	
	return total;

	

total=digitsum(binary_data)

if total%2 == 0:
	print("even number of 1's")
	print("Binary data with parity bit")
	print(even_parity)
	print('The modified string received at the other end')
	print(even_parity_flag)
else:
	print("odd number of 1's")
	print("Binary data with parity bit")
	print(odd_parity)
	print('The modified string received at the other end')
	print(odd_parity_flag)







