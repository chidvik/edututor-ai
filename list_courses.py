from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']

def main():
    # Load existing token (we already authenticated)
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('classroom', 'v1', credentials=creds)

    # List courses
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print("No courses found.")
    else:
        print("Your Courses:")
        for course in courses:
            print(f"- {course['name']} (ID: {course['id']})")

if __name__ == '__main__':
    main()
