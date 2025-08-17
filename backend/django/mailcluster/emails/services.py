from .models import Email, Thread
from django.contrib.auth.models import User

def send_email(sender_id, receiver_id, subject, body):
    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)

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

def reply_email(parent_email_id, sender_id, receiver_id, body):
    parent = Email.objects.get(id=parent_email_id)
    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)

    reply = Email.objects.create(
        sender=sender,
        receiver=receiver,
        subject=f"RE: {parent.subject}",
        body=body,
        thread=parent.thread,
        parent_email=parent
    )
    return reply

def forward_email(parent_email_id, sender_id, receiver_id, body):
    parent = Email.objects.get(id=parent_email_id)
    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)

    fwd = Email.objects.create(
        sender=sender,
        receiver=receiver,
        subject=f"FWD: {parent.subject}",
        body=body,
        thread=parent.thread,
        parent_email=parent
    )
    return fwd
