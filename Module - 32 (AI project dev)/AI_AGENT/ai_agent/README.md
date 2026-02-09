# Install Requests:
- Using pip:
```bash
pip install requests
```
- this is for 3rd party api calls, not for the API itself.

# Install Python-decouple:
- Using pip:
```bash
pip install python-decouple
```
- this is for managing environment variables, such as API keys.

# For using mysql database:
- In settings.py, change the database settings to use MySQL instead of SQLite. 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ai_agent_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Then will need to install the MySQL client library for Python as well:
```bash
pip install mysqlclient
```
