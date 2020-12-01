#Task_3_2 with **kwargs

def check_email(email):
    """Функция проверки корректности ввода email"""

    if '@' not in email:
        print('некорректный адрес')
        return 'invalid_email'
    elif (email.index('@') == 0) | (email.index('@') == len(email)-1):
        print('нет логина или домена')
        return 'invalid_email'
    elif (email.index('.') != len(email)-3) & (email.index('.') != len(email)-4):
        print('нет домена')
        return 'invalid_email'
    else:
        return email

def check_phone(phone):
    """Функция проверки корректности ввода номера телефона"""

    valid_chr = ['0','1','2','3','4','5','6','7','8','9']
    for num in phone:
        if num not in valid_chr:
            print('некорректный номер')
            return 'invalid_number'
    return phone

def check_date(date):
    """Функция проверки корректности ввода года рождения"""

    valid_chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in date:
        if (num not in valid_chr) | (len(date) > 4):
            print('некорректный год рождения')
            return 'invalid_date'
    return date

def notebook(**kwargs):
    book = list()
    book.append(kwargs)
    return " ".join(book[0].values())
    
forms = ['name','family','date','city','email','phone']
par = {}
for key in forms:
    par[key] = input(f'Input {key} - ')
    if key == 'email': par[key] = check_email(par[key])
    if key == 'date': par[key] = check_date(par[key])
    if key == 'phone': par[key] = check_phone(par[key])

print(notebook(**par))

