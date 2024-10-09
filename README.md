📚 Attendance System Using Face Recognition


🎯 Overview

This project implements a face recognition attendance system using Python, OpenCV, and the Twilio API. It captures real-time video feed, recognizes registered individuals, marks their attendance, and sends a confirmation message via SMS.

🛠️ Key Features

Real-time Face Recognition: Detects faces in a live video stream using face_recognition and OpenCV.

Attendance Tracking: Records attendance by writing recognized names, timestamps, and dates into a CSV file.

SMS Notifications: Sends an SMS to registered attendees notifying them of their marked attendance using Twilio.

📦 Requirements

To run this project, you'll need the following Python packages:


`face_recognition`

`opencv-python`

`numpy`

`csv`

`pyttsx3`

`streamlit`

`twilio`

You can install the required packages using pip:


`pip install face_recognition opencv-python numpy pyttsx3 streamlit twilio`

⚙️ Setup Instructions

Clone the Repository:

`git clone https://github.com/yourusername/attendance-system.git`

Navigate to the Project Directory:

`cd attendance-system`

Update Twilio Credentials:

Replace the placeholder `account_sid` and `auth_token` with your Twilio account credentials.

Update the `attendee_phone_numbers` dictionary with the names and phone numbers of your attendees.

Add Sample Images:

Include sample images of the attendees in the project directory, naming them as follows:
`Sample_image1.jpeg`
`Sample_image2.jpg`
`Sample_image3.jpg`
`Sample_image4.jpg`

Run the Application:

`python attendance_system.py`

📸 How to Use

When prompted, allow the application to access your camera.

The program will start capturing video frames and recognizing faces.

When a registered attendee is recognized, their attendance will be marked, and they will receive an SMS notification.

To stop the video stream, click the "Stop Streamlit" button.

📄 Output

Attendance records will be saved in a CSV file named with the current date (e.g., 09-Oct-2024.csv).

🤝 Contributions

Feel free to fork the repository, make changes, and submit pull requests!

📄 License

This project is open-source and available under the MIT License.

