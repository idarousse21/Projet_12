<h1 align ="center">Explication et lancement du code</h1>

------------------------------
<h2 align = "center"> Application et Bibliothèque</h2>

<p>
    Pour employer le code, tout d'abord, installez l'application python et le système de gestion de base de données PostgreSQL.
<ul>
    <li>
        <a href = "https://www.python.org/downloads/">Python </a>
    </li>
    <li>
        <a href = "https://www.postgresql.org/">PostgreSQL </a>
    </li>
</ul>
</p>
<p>
    Nous utiliserons aussi les bibliothèques python:.
<ul>
    <li>
        <a href = "https://www.djangoproject.com/">Django </a>
    </li>
    <li>
        <a href = "https://www.django-rest-framework.org/">Django REST framework</a>
    </li>
    <li>
        <a href = "https://django-rest-framework-simplejwt.readthedocs.io/en/latest/">Simple JWT</a>
    </li>
    <li>
        <a href = "https://django-filter.readthedocs.io/en/stable/">Django-filter</a>
    </li>
</ul>
</p>

<h2 align = "center"> Documentation de l'application </h2>
<p>
   Avant de lancer l'application je vous suggère de lire la documentation de l'API:
<ul>
    <li>
        <a href = "https://documenter.getpostman.com/view/23090595/2s93JqRPw6">Documentation Epicevnts API </a>
    </li>
</ul>

</p>

<h2 align = "center"> Lancement du code </h2>
<p>Pour commencer, vous devez lancer l'invite de commande et employer les commandes suivantes:
    <ol>
        <li>Clonez le projet:</li>
                <ul><li>git clone https://github.com/idarousse21/Projet_12 </li></ul>
            <li>Dirigez-vous sur le dossier cloné:</li>
                <ul><li>cd Projet_12 </li></ul>
            <li>Créez un environnement virtuel:</li>
                <ul><li>python -m venv env</li></ul>
            <li>Puis activation de l'environnement virtuel:</li>
                <ul><li>Sur Windows:</li></ul>
                env\Scripts\activate
                <ul><li>Sous Mac/Linus:</li></ul>
                source/env/Scripts/activate
            <li>Télécharger les bibliothèque nécessaire :</li>
                <ul><li>pip install -r requirements.txt</li></ul>
            <li>Démarrer le serveur django:</li>
                <ul><li>python manage.py runserver</li></ul>
    </ol>

<h2 align = "center"> Synchronisation de la database avec PostgreSQL</h2>
    <p>
        Pour synchronisé la database avecl'application il faut:
    </p>
    <ul>
        <li> Créer une database sur PostgreSQL avec comme nom "epicevents",
             un utilisateur avec comme user "idarousse" et comme mot de passe "idarousse123" (sinon vous pouvez modifié le fichier settings de l'application afin qu'il              corréspond avec votre base de donnée)</li>
    </ul>       
   
