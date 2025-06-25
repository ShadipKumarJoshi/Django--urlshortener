![alt text](image.png)
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/Scripts/activate

# Install Django and requests
pip install django requests

# Install all requirements
pip install -r requirements.txt

# Run
cd weather_dashboard
py manage.py runserver

- Tailwind should be properly configured in `settings.py` using [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/).



