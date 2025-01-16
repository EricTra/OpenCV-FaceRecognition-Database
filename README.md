## 🌟 Project Overview
The **OpenCV-FaceRecognition-Database** project is an automated attendance system designed for workplaces and schools. The system utilizes **Orange Pi 5 Plus**, a **Logitech HD C720 Camera**, and is powered by **OpenCV** and **Firebase**. By implementing real-time face detection and recognition, the project replaces traditional attendance methods with a seamless, secure, and contactless experience.

---

## 🛠️ Technologies Used
- **Programming Language**: Python
- **Libraries**: OpenCV, Firebase Admin SDK, face_recognition, NumPy
- **Hardware**:
  - Orange Pi 5 Plus
  - Logitech HD C720 Camera
  - ![image](https://github.com/user-attachments/assets/b37546a1-e9d2-4932-99b5-c46477a81e76)

- **Database**: Firebase Realtime Database, Firebase Storage
- **Development Environment**: PyCharm IDE

---

## ✨ Key Features
- Real-time face detection and recognition.
- Automated attendance tracking and logging in Firebase.
- Secure image storage and data management via Firebase.
- User-friendly interface displaying employee/student information.

---

## 📥 Installation and Usage

### 1. Environment Setup
Clone the repository:
```bash
git clone https://github.com/EricTra/OpenCV-FaceRecognition-Database.git
cd OpenCV-FaceRecognition-Database
`````
Install required dependencies:
```bash
pip install opencv-python firebase-admin face-recognition numpy
`````
### 2. Firebase Configuration
- Create a Firebase project on Firebase Console.
- Download the serviceAccountKey.json file and place it in the root directory of the project.
- Update the database URL and storage bucket in the source code (Main.py, AddDataToDatabase.py, etc.) to match your Firebase configuration.
 ### 3. Running the Application
1. Encode facial data and save it to a file:
```bash
python EncodeGenerator.py
`````

2. Add user data to Firebase:
 ```bash
python AddDataToDatabase.py
`````

3. Start the facial recognition system:
```bash
python Main.py
`````

---
## 📸 Demo and Screenshots

### 1. User interface during facial recognition:
![image](https://github.com/user-attachments/assets/5311f34b-7fc1-4355-9483-e1b234fa902a)
![image](https://github.com/user-attachments/assets/0a648c8a-0a7d-43d0-b791-5dd0d81089b5)
![image](https://github.com/user-attachments/assets/a7eeb3b8-388c-43b3-b471-3866743d9ba6)
![image](https://github.com/user-attachments/assets/cacced62-87fb-4d8e-8cb3-43bfd19fcddb)
![image](https://github.com/user-attachments/assets/036fc9fe-a7c9-471c-a073-5c4eeaea248c)
![image](https://github.com/user-attachments/assets/5587cb47-9626-4db3-87c2-1981014b8055)

### 2. Real-time data stored in Firebase:
![image](https://github.com/user-attachments/assets/0045cc50-30b2-42de-8401-45fed5842ec6)
![image](https://github.com/user-attachments/assets/f10171d9-8910-4f8a-bbd7-e9c8cf2bcb62)

---
## 📧 Contact Information
- Author: Trà Quang Duy
- Email: traquangduy246@gmail.com
- LinkedIn: https://www.linkedin.com/in/traquangduy/

