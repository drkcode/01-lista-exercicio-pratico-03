from datetime import datetime
import json


def send_happy_birthday(friend_list_json_path):
    friend_list = get_data_from_json(friend_list_json_path)
    for friend in friend_list:
        birthday = get_birthday_date(friend)
        is_birthday = check_birthday(birthday)

        if not is_birthday:
            continue

        brithday_message = create_happy_birthday_message(friend)
        send_email(friend["email"], brithday_message)


def get_birthday_date(friend):
    birthday = friend["birthday"]

    if len(birthday) < 10:
        raise Exception("date has a invalid format. should be mm-dd-yyyy")

    date = datetime.strptime(birthday, "%m-%d-%Y").date()

    return date


def check_birthday(birthday):
    curr_date = datetime.now()

    if curr_date.day != birthday.day or curr_date.month != birthday.month:
        return False

    return True


def create_happy_birthday_message(friend):
    return f"Happy Birthday, {friend['name']} {friend['surname']}"


def send_email(friend_email, message):
    if len(friend_email) < 1 or len(message) < 1:
        raise Exception("an email and a message must be provided")

    print(f"\nSending email to {friend_email}: OK")
    return True


def get_data_from_json(file_path):
    file = open(file_path, "r")
    data = file.read()
    file.close()
    result = json.loads(data)
    return result
