DJOSER = {
    'SERIALIZERS': {
        'user': 'apps.users.serializers.UserSerializer',
        'current_user': 'apps.users.serializers.UserSerializer',
        'user_create': 'apps.users.serializers.UserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'PERMISSIONS': {
        'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.AllowAny'],
        'user_create': ['rest_framework.permissions.AllowAny'],
    },
    'TOKEN_MODEL': None,
    'LOGIN_FIELD': 'email',
    'SEND_ACTIVATION_EMAIL': True,
    'EMAIL': {
        'activation': 'racoon_project.email.ActivationEmail',
        'password_reset': 'racoon_project.email.PasswordResetEmail',
    },
    'ACTIVATION_URL': 'auth/users/activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'auth/users/reset_confirm/password/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'LOGOUT_ON_PASSWORD_CHANGE': False,
    'USERNAME_RESET_CONFIRM_URL': 'auth/users/reset_confirm/username/{uid}/{token}/',
    'USERNAME_RESET_SHOW_EMAIL_NOT_FOUND': True,
}
