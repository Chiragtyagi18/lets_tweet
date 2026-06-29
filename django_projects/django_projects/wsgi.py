import os
import sys
from django.core.wsgi import get_wsgi_application

# 1. Tell Vercel to look inside the outer django_projects folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. Set the settings path 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_projects.settings')

# 3. Create the production application callable
application = get_wsgi_application()
app = application
