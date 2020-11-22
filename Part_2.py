#Lists are mutable and items can be modified  and Tuples are immutable
my_numbers=[10,20,30,40,50,60]  #list is used square bracket
my_numbers[0]=100
print(my_numbers)
   #out [100, 20, 30, 40, 50, 60]

my_numbers2=(20,30,40,50,60,20,10)   #used parenthesis to creat Tuples
my_numbers2[3]='100'
print(my_numbers2)
   #out TypeError: 'tuple' object does not support item assignment


# Lists has several built-in methods but Tuple does not have built-in methods

my_cities=['Samrkand','Tashkent','Bukhara']
my_cities.append('London')   #added a new item end of the List  by this method
print(my_cities)
 #out ['Samarkand','Tashkent','Bukhara',London']

a=[10,20,100,34,5,7]
a.sort()   # this method can modify the order from ascending to descending
print(a)
   #out  [5, 7, 10, 20, 34, 100]


my_cities2=['Samarkand','Tashkent','Bukhara']
my_cities2.extend([10,20,30])   #it can add multiple items in the list
print(my_cities2)
   #out ['Samarkand', 'Tashkent', 'Bukhara', 10, 20, 30]

prices = [159.54, 37.13, 71.17]
price_max = max(prices)  #it can maximum price in the list
print(price_max)
 #out 159.54

prices1 = [159.54, 37.13, 71.17]
prices_min=min(prices)   #it returns min value in the list
print(prices_min)
   #out 37.13
