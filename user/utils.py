from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    message = f'''
    Вы успешно зарегистрировались на аншем сайте. Пройдите активацию аккаунта, отправив нам этот код: {activation_code}
    '''

    send_mail(
        'Активация аккаунта',
        message,
        'alina@gmail.com',
        [email]
    )