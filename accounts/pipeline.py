from django.contrib.auth import get_user_model

User = get_user_model()

def get_or_create_user(strategy, details, backend, uid, user=None, *args, **kwargs):
    if user:
        return {'user': user}

    email = details.get('email')

    if email:
        email = email.lower().strip()  # Normalize email

        try:
            user = User.objects.get(email=email)
            return {'user': user}
        except User.DoesNotExist:
            user = strategy.create_user(email=email)
            return {'user': user}
    
    return {}