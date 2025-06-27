from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Scope for managing Google Classroom courses
SCOPES = ['https://www.googleapis.com/auth/classroom.courses']

def main():
    creds = None

    # Load existing token or run auth flow
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8090)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build Google Classroom API service
    service = build('classroom', 'v1', credentials=creds)

    # Course details
    course = {
        'name': 'EduTutor AI Demo Course',
        'section': 'Period 1',
        'descriptionHeading': 'Welcome to EduTutor AI',
        'description': 'This course is auto-created for integration testing.',
        'room': 'Room A',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }

    # Create the course
    course = service.courses().create(body=course).execute()
    print(f"✅ Course created: {course.get('name')} (ID: {course.get('id')})")

if __name__ == '__main__':
    main()
