
### 1. Virtual venv
```
python3.10 -m venv venv
source venv/bin/activate
```

### 2. Installing requirements

```
pip install -r requirements/base.txt # install for both
pip install -r requirements/develop.txt # on develop mode
pip install -r requirements/production.txt # on production mode
```

### 3. Create .env file
```
DJANGO_SETTINGS_MODULE= # settings module
CUSTOM_VAR= # custom var
SECRET_KEY= # your strong secret key

```
### 4. Migration
```
python manage.py migrate
```

### 5. Run server
```
python manage.py runserver
```