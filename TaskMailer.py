import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_tz, mktime_tz
import datetime
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Paramètres de connexion IMAP
IMAP_SERVER = 'votre.serveur.imap'
IMAP_PORT = 993
USERNAME = 'votre@adresse.email'
PASSWORD = 'votreMotDePasse'

# Paramètres Google API
SCOPES = ['https://www.googleapis.com/auth/tasks']
CREDENTIALS_FILE = 'chemin/vers/votre/credentials.json'

def get_credentials():
    """Obtient les credentials Google de l'utilisateur."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def connect_to_imap():
    """Se connecte au serveur IMAP et retourne une instance de connexion."""
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(USERNAME, PASSWORD)
    return mail

def search_emails(mail):
    """Recherche les e-mails envoyés avec un sujet spécifique et retourne leurs IDs."""
    mail.select('"Envoyés"')  # Ajustement pour o2switch
    result, data = mail.search(None, '(SUBJECT "Avis de valeur")')
    if result == 'OK':
        return data[0].split()
    return []

def create_task(service, title, due_date):
    """Crée une tâche dans Google Tasks avec le titre donné et la date d'échéance."""
    tasklist = '@default'  # Utilise la liste par défaut. Ajustez si nécessaire.
    task = {
        'title': title,
        'due': due_date.isoformat() + 'Z',  # Format de date RFC3339
        'recurrence': 'RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT=50'
    }
    result = service.tasks().insert(tasklist=tasklist, body=task).execute()
    print(f"Task created: {result['id']}")

def main():
    service = build('tasks', 'v1', credentials=get_credentials())
    mail = connect_to_imap()

    for email_id in search_emails(mail):
        typ, msg_data = mail.fetch(email_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = decode_header(msg['subject'])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                
                # Vérification de la structure de l'objet de l'e-mail
                if subject.startswith("Avis de valeur") and '-' in subject:
                    # Extraire la date d'envoi
                    date_tuple = parsedate_tz(msg['Date'])
                    if date_tuple:
                        send_date = datetime.datetime.utcfromtimestamp(mktime_tz(date_tuple))
                        due_date = send_date + datetime.timedelta(days=1)  # Ajustement de la date d'échéance
                        create_task(service, f"RAPPEL {subject}", due_date)

if __name__ == "__main__":
    main()
