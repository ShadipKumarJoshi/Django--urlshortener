![alt text](image-1.png)
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


## Environment Variables

This project uses an [OpenWeatherMap](https://openweathermap.org/) API key. To run the project, create a `.env` file in the root directory and add the following:

OPENWEATHERMAP_API_KEY=your_actual_api_key_here
