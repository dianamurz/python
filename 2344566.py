spisok=[]
while True:
    tovar=input('chto vi hotite dobavit v spisok?/Esli zakonchili-napishie "vihod":')
    if tovar.lower()=="vihod":
        print('vi zakoncili pokypki!')
        break
    else:
        spisok.append(tovar)
        print(f'tekyshie spisok pokypok soderzhit:{spisok}')
