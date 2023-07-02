from datetime import datetime , timedelta

users = [
    {'name': 'Max', 'birthday': datetime(year=2000, month=8, day=19)},
    {'name': 'Omar', 'birthday': datetime(year=1998, month=8, day=18)},
    {'name': 'Olexander', 'birthday': datetime(year=2000, month=9, day=19)},
    {'name': 'Illia', 'birthday': datetime(year=2000, month=11, day=20)},
]


def get_birthdays_per_week(users):
    today = datetime.now()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(7):
        day = (today + timedelta(days=i)).strftime('%A')
        if day == 'Monday':
            monday_users = [user['name'] for user in users if user['birthday'].weekday() >= 5 and user['birthday'].weekday() <= 6]
            if monday_users:
                print(f"{day}: {', '.join(monday_users)}")

        users_to_greet = [user['name'] for user in users if user['birthday'].weekday() == i]
        if users_to_greet:
            print(f"{day}: {', '.join(users_to_greet)}")



get_birthdays_per_week(users)
