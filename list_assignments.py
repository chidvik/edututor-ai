from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# SCOPES required to read coursework
SCOPES = [
    "https://www.googleapis.com/auth/classroom.coursework.students.readonly",
    "https://www.googleapis.com/auth/classroom.coursework.students",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly"
]



def main():
    creds = None

    # Load credentials or run OAuth flow
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8090)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build the Classroom API service
    service = build('classroom', 'v1', credentials=creds)

    # 🔁 Replace with your actual course ID
    course_id = '782699348480'

    # Get courseWork (assignments)
    results = service.courses().courseWork().list(courseId=course_id).execute()
    courseworks = results.get('courseWork', [])

    if not courseworks:
        print("No assignments found.")
    else:
        print("📚 Assignments:")
        for work in courseworks:
            print(f"- {work['title']} (Due: {work.get('dueDate', 'N/A')})")

if __name__ == '__main__':
    main()
