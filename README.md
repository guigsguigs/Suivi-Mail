# Projet de Suivi d'Emails pour Avis de Valeurs Immobilières

## Objectif
Automatiser le suivi des emails d'avis de valeurs envoyés aux clients via notre logiciel immobilier. Le projet permet de détecter les envois d'emails, suivre les réponses des clients, envoyer des rappels automatiques en cas de non-réponse, et intégrer les rappels dans Google Agenda pour une meilleure gestion du temps.

## Fonctionnalités
- **Détecter les envois d'avis de valeurs** : Identifie les emails envoyés depuis la boîte "envoyé" d'o2switch.
- **Suivi des réponses** : Vérifie si les clients ont répondu aux emails envoyés.
- **Rappels automatiques** : Envoie des rappels si aucune réponse n'est reçue après 7 et 15 jours.
- **Intégration avec Google Agenda** : Crée automatiquement des événements de rappel dans Google Agenda pour les suivis.
- **Analyse de sentiment** (optionnel) : Évalue le ton des réponses reçues.

## Technologie Utilisée
- **Python** : Langage de programmation.
- **imaplib et smtplib** : Pour interagir avec les serveurs de messagerie IMAP et SMTP d'o2switch.
- **SQLite** : Pour la gestion de la base de données.
- **schedule** : Pour la planification des tâches.
- **Google Calendar API** : Pour intégrer les rappels dans Google Agenda.

## Mise en Place
1. **Installation des dépendances** :
   ```
   pip install imaplib smtplib schedule sqlite3 google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```
2. **Configuration** :
   - Configurez l'accès à votre serveur IMAP et SMTP chez o2switch.
   - Suivez la documentation de Google pour configurer l'accès à l'API Google Calendar.

3. **Lancement du script** : Exécutez le script pour démarrer le suivi. Planifiez une exécution régulière avec un outil comme cron.

## Utilisation
- Le script vérifie les réponses et envoie des rappels automatiquement.
- Les rappels sont également ajoutés à Google Agenda pour un suivi facile.

## Sécurité et Confidentialité
- Conformez-vous aux réglementations sur la confidentialité des données (ex. RGPD).
- Sécurisez les informations d'identification et les données personnelles.
