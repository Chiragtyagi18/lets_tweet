import os
import sys

# Load .env file if it exists (for local development)
# On Vercel, env vars are set via the dashboard, not a .env file
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent / '.env')

# Add the project directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'django_projects'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_projects.settings')

# Import and expose the Django WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
