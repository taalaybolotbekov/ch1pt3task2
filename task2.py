def gradus():
    tem = input('Введите температуру: ')
    sign = tem[-1] # извлекается последний знак строки
    # строка за исключением последнего знака переводится в целое число
    tem= int(tem[0:-1]) 
    if sign == 'C' or sign == 'c': # Если знак обозначает Цельсии,
        tem = round(tem * (9/5) + 32) # перевод в Фаренгейты, округление до целого
        return(str(tem) + 'F')
    elif sign == 'F' or sign == 'f': # Если знак обозначает Фаренгейты
        tem = round((tem - 32) * (5/9)) # перевод в Цельсии и округление до целого
        return(str(tem) + 'C')
print(gradus())