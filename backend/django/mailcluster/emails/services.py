from .models import Email, Thread
from django.contrib.auth.models import User

def get_or_create_user(email):
    """Fetch user by email, or create if not exists."""
    user, created = User.objects.get_or_create(
        email=email,
        defaults={"username": email.split("@")[0]}  # username = part before @
    )
    return user

def send_email(sender_email, receiver_email, subject, body):
    sender = get_or_create_user(sender_email)
    receiver = get_or_create_user(receiver_email)

    # new thread
    thread = Thread.objects.create()

    email = Email.objects.create(
        sender=sender,
        receiver=receiver,
        subject=subject,
        body=body,
        thread=thread,
        parent_email=None
    )
    return email

def reply_email(parent_email_id, sender_email, receiver_email, body):
    parent = Email.objects.get(id=parent_email_id)
    sender = get_or_create_user(sender_email)
    receiver = get_or_create_user(receiver_email)

    reply = Email.objects.create(
        sender=sender,
        receiver=receiver,
        subject=f"RE: {parent.subject}",
        body=body,
        thread=parent.thread,
        parent_email=parent
    )
    return reply

def forward_email(parent_email_id, sender_email, receiver_email, body):
    parent = Email.objects.get(id=parent_email_id)
    sender = get_or_create_user(sender_email)
    receiver = get_or_create_user(receiver_email)

    fwd = Email.objects.create(
        sender=sender,
        receiver=receiver,
        subject=f"FWD: {parent.subject}",
        body=body,
        thread=parent.thread,
        parent_email=parent
    )
    return fwd
