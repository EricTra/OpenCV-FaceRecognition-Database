import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionrealtimed-e816a-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "0000": {
        "name": "Tran Thi Thuy Ba",
        "major": "English Lecture",
        "starting_year": 2019,
        "total_attendance": 20,
        "standing": "Best",
        "year": 4,
        "last_attendance_time": "2023-8-16 00:54:34"

    },
    "1111": {
        "name": "Do Trong Vinh",
        "major": "IoT",
        "starting_year": 2020,
        "total_attendance": 15,
        "standing": "Good",
        "year": 4,
        "last_attendance_time": "2023-8-16 00:54:34"

    },
    "2222": {
        "name": "Nguyen Anh Tuan",
        "major": "Auditing",
        "starting_year": 2020,
        "total_attendance": 14,
        "standing": "Best",
        "year": 4,
        "last_attendance_time": "2023-8-16 00:54:34"

    },
    "3333":{
        "name": "Tra Quang Duy",
        "major": "AI engineer",
        "starting_year": 2021,
        "total_attendance": 10,
        "standing": "Good",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "4444": {
        "name": "Nguyen Quang Ngoc",
        "major": "Moblie Dev",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Best",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "5555": {
        "name": "Truong Tan Phuc",
        "major": "Server",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Best",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "6666": {
        "name": "Nguyen Hai Viet",
        "major": "Game dev",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Best",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "7777": {
        "name": "Nguyen Van Thang",
        "major": "Back End",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Poor",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "8888": {
        "name": "Tran Huy Hoang",
        "major": "Back End",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Best",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    },
    "9999": {
        "name": "Duong Van Hieu",
        "major": "Full Stack",
        "starting_year": 2021,
        "total_attendance": 14,
        "standing": "Good",
        "year": 3,
        "last_attendance_time": "2023-8-16 00:54:34"
    }
}
for key, value in data.items():
    ref.child(key).set(value)