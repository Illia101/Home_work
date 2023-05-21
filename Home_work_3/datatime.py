from datetime import datetime, timedelta

users = [
    {'name': 'Max', 'birthday': datetime(year=2023, month=5, day=19)},
    {'name': 'Omar', 'birthday': datetime(year=1998, month=5, day=18)},
    {'name': 'Olexander', 'birthday': datetime(year=2000, month=5, day=19)},
    {'name': 'Illia', 'birthday': datetime(year=2000, month=6, day=20)},
]


# def get_birthdays_per_week(users):
#     date_now = datetime.now()
    
    
#     name = users['name']
#     birthday = users['birthday'].date()
    
#     for user in users:
#         if birthday.weekday() == 0:
#             print(f'Monday: {name}')
#         if birthday.weekday() == 1:
#             print(f'Tuesday: {name}')
#         if birthday.weekday() == 2:
#             print(f'Wednesday: {name}')
#         if birthday.weekday() == 3:
#             print(f'Thursday: {name}')
#         if birthday.weekday() == 4:
#             print(f'Friday: {name}')
#         if birthday.weekday() == 5:
#             print(f'Saturday: {name}')
#         if birthday.weekday() == 6:
#             print(f'Sunday: {name}')



from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    birthdays_per_week = {}
    
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        
        days_until_birthday = (birthday - start_of_week).days
        weekday = (today.weekday() + days_until_birthday) % 7
        
        # Якщо день народження випадає на вихідний (5 або 6),
        # встановлюємо weekday на понеділок (0)
        if weekday >= 5:
            weekday = 0
        
        if weekday in birthdays_per_week:
            birthdays_per_week[weekday].append(name)
        else:
            birthdays_per_week[weekday] = [name]
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for i in range(7):
        day = days_of_week[i]
        
        if i in birthdays_per_week:
            print(f"{day}: {', '.join(birthdays_per_week[i])}")
        else:
            print(f"{day}:")


 

get_birthdays_per_week(users)



