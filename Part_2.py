          #Lists are mutable and items can be modified  and Tuples are immutable

#List
my_numbers=[10,20,30,40,50,60]  #list is used square bracket
my_numbers[0]=100
print(my_numbers)
   #out [100, 20, 30, 40, 50, 60]

#Tuple
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
price_max = max(prices)  #it returns maximum value in the list
print(price_max)
 #out 159.54


prices1 = [159.54, 37.13, 71.17]
prices_min=min(prices)   #it returns min value in the list
print(prices_min)
   #out 37.13


shoes_brands=['Addidas','Zara','Nike']
shoes_brands.pop(0)  #This function removes items by index num
print(shoes_brands)

         # List iteration is slower and time consuming
         # Tuple iteration is faster

# iteration with Tuple
famouse_players=('Ronaldo','Messi','Neimar','Anvar')
for i in enumerate(famouse_players):    # enumerate function with tuple
    print(i)
#out (0, 'Ronaldo')
#(1, 'Messi')
#(2, 'Neimar')
#(3, 'Anvar')


famouse_players2=('Ronaldo','Messi','Neimar','Anvar')
years=('2016','2017','2018','2020')
zipped=tuple(zip(famouse_players2,years))   # zip function with tuple
for i in zipped:
    print(zipped)
#out (('Ronaldo', '2016'), ('Messi', '2017'), ('Neimar', '2018'), ('Anvar', '2020'))
#(('Ronaldo', '2016'), ('Messi', '2017'), ('Neimar', '2018'), ('Anvar', '2020'))
#(('Ronaldo', '2016'), ('Messi', '2017'), ('Neimar', '2018'), ('Anvar', '2020'))
#(('Ronaldo', '2016'), ('Messi', '2017'), ('Neimar', '2018'), ('Anvar', '2020'))


#  iteration with list
 languages=['Uzbek','Tadjik','English','Arab']
 for i, lan in enumerate(languages):  #enumerate func counts items
     print(i, "Wiut",lan)
#out
#0Wiut Uzbek
#1 Wiut Tadjik
#2 Wiut English
#3 Wiut Arab

wiut_students_marks=[20,30,10,50]
names=['Anvar','Jasur','Faridun','John']
final_report=list(zip(wiut_students_marks,names)) #zip function with Tuples
print(final_report)
# OUT  [(20, 'Anvar'), (30, 'Jasur'), (10, 'Faridun'), (50, 'John')]


          #Tuple is useful for  accessing elements rather than List
schedule_wiut = [('Mon','3 pm',10),('Tue','12pm',8),('Wed','9 am',8),('Thu','6 am',5)]
#Given list
print("Given deadline: ",schedule_wiut)
# Use index
res = [x[1] for x in schedule_wiut]

print("The 1 st element form each tuple in the list: \n",res)
 #out
#Given deadline:  [('Mon', '3 pm', 10), ('Tue', '12pm', 8), ('Wed', '9 am', 8), ('Thu', '6 am', 5)]
#The 1 st element form each tuple in the list:
#['3 pm', '12pm', '9 am', '6 am']



                         #Difference between Lists and Dictionaries
 #  Dictionary elements  accessed through key-values and list elements by index value

students_mark={"Anvar":70,"John":40,"George":30}
print(students_mark["Anvar"])   #accessed by key values
print(students_mark["John"])
          #out 70  ,40

my_identity={"Name":"Anvar","Age":20,"Birth in city":"Samarkand","ID":11342}
for x in my_identity.items():  #  returns value and keys together
print(x)                             #    value() the method returns values of dict
                                        #     key() returns just inputs of dict




cars_color={"Ferrari":"red","Cobalt":"black","Gentra":"grey"}
cars_color1=cars_color.items()   #items() method returns list of keys and values stored in tuple pair
print(cars_color1)
 #out dict_items([('Ferrari', 'red'), ('Cobalt', 'black'), ('Gentra', 'grey')])



        # dictionary is changeable and we can add new items rather than tuples
       #adding items in Dictionary
US_presidents ={1:"Bill Clinton",2:"Barac Obama",3:"Donald Trump"}
US_presidents[3]="Joe Biden"   # must be embeded by key name for change value
print(US_presidents)
#out {1: 'Bill Clinton', 2: 'Barac Obama', 3: 'Joe Biden'}

         # removing items from dictionary similar to List
my_csf_tutors={"name1":"Olga Yugay","name2":"Vasiliy Kuznetov","name3":"Subair Ali"}
del my_csf_tutors["name2"]   # we can remove items by providing key values of values in dict
 #out {"name1":"Olga Yugay","name3":"Subair Ali"}


#            zip() function with List
high_ranked_uni=['Wiut','Inha','Webster']
rank_scores=[10,7,9]
report=zip(high_ranked_uni,rank_scores)   #items are zipping from left to right
for ranks in   enumerate(report):      #looping for each items and also counting objents in the lists
    print(ranks)
  #out
#(0, ('Wiut',10))
#(1,('Inha',7))
#(2,('Webster',9))



  # Traversing lists in Parallel
rich_countries = ['Uzbekistan', 'USA', 'Japan']
rich_cities = ['Samrkand', 'New York', 'Tokio']
economy_report = list(zip(rich_countries, rich_cities)) #convert into list() method and  zip() should be inside List round Braces
for r, p in economy_report:
        print(f'Rich city:{p}')   #here traversing through two list items
        print(f'Rich Country:{r}')
        #output
#Rich city:Samrkand
#Rich Country:Uzbekistan
#Rich city:New York
#Rich Country:USA
#Rich city:Tokio
#Rich Country:Japan



#  Traversing and zip() function with Dictionary
winner1={"Name":"Anvar","Age":20,"Student":"Wiut"}   #dict list1
winner2={"Name":"Sardor","Age":20,"Student":"Inha"}  #dict list2
for (s1, f1) ,(s2, f2) in zip(winner1.items(),winner2.items()):     #items() function is used to bring both keys and values
          print(s1, '<>',f1)     # items are stored into differnt variables
          print(s2,'<>',f2)
          #output
#Name <> Anvar
#Name <> Sardor
#Age <> 20
#Age <> 20
#Student <> Wiut
#Student <> Inha


 #         zip and enumerate methods with Tuple

 prog_lans =('CSS','Python','JS')
 progs=('Visual Studio','Pycharm','Node JS')
 zipped=tuple(zip(prog_lans,progs))   #converted into tuple here
 for progs in enumerate(zipped):  #counting of iterations
     print(progs)
#output
#(0, ('CSS', 'Visual Studio'))
#(1, ('Python', 'Pycharm'))
#(2, ('JS', 'Node JS'))



