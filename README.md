# ResQ — Module M4

Implémentation Sprint 1 du module **Aide humanitaire, bénévoles, ressources et refuges**.

## Démarrage backend
```powershell
cd resq_backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations humanitarian
python manage.py migrate
python manage.py runserver
```

## Démarrage frontend
```powershell
cd frontend
npm install
npx ng serve
```

CRUD REST : `/api/volunteers/`, `/api/resources/`, `/api/shelters/`, `/api/missing-persons/`.
