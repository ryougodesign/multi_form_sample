from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
generated_secret_key = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(generated_secret_key)