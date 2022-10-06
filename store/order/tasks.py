from django.core.mail import send_mail


def order_status_email(transaction_id, status, email, value):
    email = email
    subject = f'Order detail'
    if value is None:
        message = f'Your oder with number {transaction_id} ' \
                  f'changed to {status}.'
    else:
        message = f'Your oder with number {transaction_id} ' \
                  f'changed from {value} to {status}.'
    from_email = 'david@admin.admin'
    send_mail(subject, message, from_email, [email], fail_silently=False)
