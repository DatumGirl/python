#question1


l1=(10,20,30);
l2=(40,50,60);
t_combine=l1+l2;
t_combine=t_combine*3;
print(t_combine[3]);
print(t_combine[3:]);
print(t_combine[:3]);
print(t_combine)

print(t_combine[-3:]);

#question2

t1=(1,2,3);
t2=("a","b","c");
t3=(True,False);
list=[t1,t2,t3];
t4=(1,"a",True);
list.append(t4);
list1=["sparta",123]
list.extend(list1)


#question3

fruit={"fruits":("apple","banana","mango","guava"),"cost":(85,54,120,70)}

print(fruit.keys());
print(fruit.values());

#question4

a={"1","1","a","a",True,True}
print (a)