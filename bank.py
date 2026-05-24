
def bank(s, i=0.02, t=10):
    savings = int(input('skolko vi hotite polozhit deneg v bank: '))
    interest = int(input('pod kakoi procent vi kladete dengi: '))/100
    time = int(input('na skolko let vi hotite polozhit dengi v bank : '))
    
    if i > 0.05:
        print('maksimalniy procent v nashem banke 5% godovih')
        return False
    savings = calc_savings(s,i,t)

savings = int(input('skolko vi hotite polozhit deneg v bank: '))
interest = int(input('pod kakoiprocent vi kladete dengi: '))/100
time = int(input('na skolko let vi hotite polozhit dengi v bank: '))
def calc_savings(savings, interest, time):
    for i in range(time):
        savings+=savings*interest
    return savings
total_savings = bank(savings, interest, time)
print(f'Vash itogovi shet v banke: {total_savings}')

         
