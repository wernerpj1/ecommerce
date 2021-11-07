from djoser import email

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'usuarios/template/password_reset.html'