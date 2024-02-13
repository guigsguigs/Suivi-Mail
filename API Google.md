L'activation des API Google Tasks et Gmail est une étape cruciale pour permettre à votre script d'interagir avec ces services Google. Voici un guide détaillé sur la manière de procéder :

### 1. Accéder à Google Cloud Console

- **Ouvrez votre navigateur** et allez sur [Google Cloud Console](https://console.cloud.google.com/).
- Si vous n'êtes pas déjà connecté, connectez-vous avec votre compte Google.

### 2. Créer un Nouveau Projet

- Dans l'interface de la Google Cloud Console, recherchez et cliquez sur le menu déroulant en haut à côté de "Google Cloud Platform" et sélectionnez "Nouveau Projet".
- Donnez un **nom à votre projet** et, si nécessaire, sélectionnez une organisation. Cliquez ensuite sur "Créer".

### 3. Activer les API Google Tasks et Gmail

- Une fois le projet créé, vous serez redirigé vers le tableau de bord de ce projet. Cliquez sur "Navigation Menu" (les trois lignes horizontales en haut à gauche), puis sur "API et services" > "Bibliothèque".
- Dans la barre de recherche, tapez **"Google Tasks API"** et sélectionnez-la dans les résultats. Cliquez sur "Activer" pour activer l'API pour votre projet.
- Répétez cette étape pour **"Gmail API"** : retournez à la "Bibliothèque" d'API, recherchez "Gmail API" et activez-la également.

### 4. Créer des Identifiants

- Après avoir activé les deux API, retournez au "Tableau de bord" des API & services via le menu de navigation.
- Cliquez sur "Identifiants" dans le menu de navigation latéral, puis sur le bouton "Configurer l'écran de consentement OAuth".
  - Sélectionnez "Externe" comme type d'utilisateur et cliquez sur "Créer".
  - Remplissez les informations nécessaires sur l'écran de consentement, telles que le nom de l'application, l'email de support, etc., puis enregistrez et continuez jusqu'à ce que vous ayez complété toutes les sections.
- Ensuite, cliquez sur "Créer des identifiants" > "ID client OAuth".
  - Choisissez "Application de bureau" comme type d'application, donnez-lui un nom, puis cliquez sur "Créer".
- Une fois les identifiants créés, vous verrez un écran affichant votre ID client et votre secret client. Vous pouvez fermer cette fenêtre.

### 5. Télécharger le fichier `credentials.json`

- Après avoir créé votre ID client OAuth, vous verrez un bouton à côté de l'ID client dans la section "Identifiants" vous permettant de télécharger le fichier JSON. Cliquez sur le bouton de téléchargement pour obtenir votre fichier `credentials.json`.

### 6. Intégrer `credentials.json` dans Votre Projet

- Placez le fichier `credentials.json` téléchargé dans le même dossier que votre script Python. Ce fichier contient les informations nécessaires pour authentifier votre script auprès des services Google.

En suivant ces étapes, vous aurez activé les API nécessaires et obtenu le fichier `credentials.json` requis pour authentifier votre script auprès de Google Tasks et Gmail. Assurez-vous de conserver votre fichier `credentials.json` en sécurité et de ne pas le partager publiquement.
