---

# Instructions Détaillées pour le Script de Création de Tâches

Ce script est conçu pour automatiser la création de tâches dans Google Tasks basées sur des e-mails spécifiques envoyés. Voici les critères et fonctionnalités spécifiques :

## Critères d'E-mail

- **Objet du Mail** : L'objet de chaque e-mail traité doit suivre la structure "Type - Référence - Adresse - Vendeur". Le script recherche spécifiquement les e-mails dont l'objet commence par "Avis de valeur" et s'assure qu'il est bien suivi d'une référence, ce qui valide la création d'une tâche dans Google Tasks.

## Création de Tâche

- **Titre de la Tâche** : Chaque tâche créée portera le titre "RAPPEL Type - Référence - Adresse - Vendeur", reprenant l'intégralité de l'objet de l'e-mail correspondant.
- **Date et Heure** : La tâche est programmée à la date et l'heure d'envoi de l'e-mail.
- **Récurrence Personnalisée** : Les tâches seront récurrentes, avec une répétition toutes les 2 semaines, le même jour que la création de la tâche, et ce pour un total de 50 occurrences.

## Configuration et Sécurité

Suivez les étapes de configuration décrites précédemment pour activer les API nécessaires, installer les dépendances, et configurer les paramètres IMAP et Google API. Assurez-vous de sécuriser votre fichier `credentials.json` et de ne jamais partager vos informations d'accès.

## Planification Automatique

Pour une efficacité maximale, planifiez l'exécution de ce script deux fois par jour à des moments précis (par exemple, à 12h00 et 21h00) en utilisant `cron` sur Linux/Mac ou le Planificateur de Tâches sur Windows. Cela garantira que les tâches sont créées régulièrement sans intervention manuelle.

---
