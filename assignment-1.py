#question1 

l1=(1,2,3,4,5,6);

l2=(6,5,4,3,2,1);

for i in (0,1,2,3,4,5):
   if  l1[i]> l2[i]:
       print(" l1 greater than l2")
   else :
       print("l2 greater than l1")
       
# question2
       
       l3=(10,20,30,40,50);
       
       # tuples are immutable so cannot loop and assign the values 
       
       l4=(l3[0]+5,l3[1]+5,l3[2]+5,l3[3]+5,l3[4]+5);
       
       print (l4);
       
       
#question 3
       
       def add_10(num):
           num=num+10
           print ( " the new values of num is", num);
                       
         #function calling 
            add_10(20)
           
            
#quetsion 4
              def check_even_odd(num1):
                if num1%2==0:
                    print(" even number")
                else:
                        print("odd number")
                        
                        
                        
                        
                      