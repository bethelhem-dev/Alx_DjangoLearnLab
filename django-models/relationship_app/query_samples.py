# query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  # replace with actual project name
django.setup()

from relationship_app.models import Author

# Create an author and print it
author = Author.objects.create(name="Jane Austen")
print("Created author:", author.name)
