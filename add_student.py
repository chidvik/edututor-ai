from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = [
    'https://www.googleapis.com/auth/classroom.rosters',
    'https://www.googleapis.com/auth/classroom.courses'
]

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8090)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)

    # ✅ Replace with your actual course ID
    course_id = '782699348480'

    # ✅ Replace with the Gmail you added as a Test User
    student_email = 'chidviksai42@gmail.com'

    student = {
        'userId': student_email
    }

    try:
        result = service.courses().students().create(courseId=course_id, body=student).execute()
        print(f"✅ Student {result['profile']['name']['fullName']} added to course.")
    except Exception as e:
        print("❌ Error adding student:", e)

if __name__ == '__main__':
    main()
