#Task_4

n = int(input("Введите целое положительное число \n"))
max = 0

while n != 0:
   if n % 10 > max:
       max = n % 10
   n = n//10

print(f'Максимальная цифра в данном числе - {max}')
