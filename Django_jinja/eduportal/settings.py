# settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'courses/static']
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'courses/templates']
