Ticket=int(input("Сколько билетов хотите приобрести?"))
sum_price=0
for i in range(1,Ticket+1):
    Age=int(input("Сколько лет посетителю?"))
    if Age<18:
        sum_price +=0
    elif 18<=Age<=25:
        sum_price +=990
    else:
        sum_price +=1390
if Ticket>3:
    print(sum_price*0.9)
else:
    print(sum_price)