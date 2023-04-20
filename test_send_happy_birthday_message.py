import unittest
from datetime import datetime
from send_happy_birthday_message import (
    check_birthday,
    create_happy_birthday_message,
    send_email,
    get_birthday_date,
    get_data_from_json,
)


class TestCheckBirthDay(unittest.TestCase):
    def test_is_bithday(self):
        curr_date_string = datetime.now().strftime("%m-%d-%Y")
        curr_date = datetime.strptime(curr_date_string, "%m-%d-%Y").date()
        sut = check_birthday(curr_date)
        self.assertTrue(
            sut,
            "should return true if the birthday date match current date",
        )

    def test_not_birthday(self):
        test_date = datetime.strptime("01-13-1991", "%m-%d-%Y").date()
        sut = check_birthday(test_date)
        self.assertFalse(
            sut,
            "should return false if the input date do not match the current date",
        )


class TestCreateHappyBirthdayMessage(unittest.TestCase):
    def test_happy_birthday_message(self):
        friend = {
            "name": "John",
            "surname": "Doe",
            "email": "johndoe@email.com",
            "birthday": "13-01-1991",
        }
        sut = create_happy_birthday_message(friend)
        self.assertEqual(
            sut,
            f"Happy Birthday, John Doe",
            "should return a message equal to: Happy Birthday, John Doe",
        )


class TestSendBirthdayMessage(unittest.TestCase):
    def test_empty_email(self):
        assert_msg = "should raise a exception if email is empty"
        with self.assertRaises(Exception, msg=assert_msg):
            send_email(friend_email=None, message="Happy Birthday, John Doe")

        with self.assertRaises(Exception, msg=assert_msg):
            send_email(friend_email="", message="Happy Birthday, John Doe")

    def test_empty_message(self):
        assert_msg = "should raise a exception if message is empty"
        with self.assertRaises(Exception, msg=assert_msg):
            send_email(friend_email="johndoe@email.com", message=None)

    def test_success_send_email(self):
        sut = send_email("johndoe@email.com", "Happy Birthday, John Doe")
        self.assertTrue(sut, "should return true if email was sent")


class TestGetBirthdayDate(unittest.TestCase):
    def test_empty_string_birthday(self):
        assert_msg = "should raise a exception if friend birthday property is empty"
        with self.assertRaises(Exception, msg=assert_msg):
            friend = {
                "name": "John",
                "surname": "Doe",
                "email": "johndoe@email.com",
                "birthday": "",
            }
            get_birthday_date(friend)

    def test_date_birthday(self):
        friend = {
            "name": "John",
            "surname": "Doe",
            "email": "johndoe@email.com",
            "birthday": "01-13-1991",
        }
        sut = get_birthday_date(friend)
        self.assertEqual(
            sut.day, 13, "should return 13 if birth day input is equal 01-13-1991"
        )
        self.assertEqual(
            sut.month, 1, "should return 1 if birth month input is equal 01-13-1991"
        )
        self.assertEqual(
            sut.year,
            1991,
            "should return 1991 if year of month input is equal 01-13-1991",
        )


class TestGetDataFromJSONFile(unittest.TestCase):
    def test_file_not_exits(self):
        with self.assertRaises(Exception):
            get_data_from_json("")

    def test_read_file(self):
        data = [
            {
                "name": "John",
                "surname": "Doe",
                "email": "johndoe@email.com",
                "birthday": "01-13-1991",
            }
        ]
        sut = get_data_from_json("test_friend_list.json")
        self.assertEqual(sut, data, "should be a list of objects")
        self.assertEqual(
            sut[0]["name"],
            "John",
            "should first object name property be equal to 'John'",
        )
        self.assertEqual(
            sut[0]["surname"],
            "Doe",
            "should first object surname property be equal to 'Doe'",
        )
