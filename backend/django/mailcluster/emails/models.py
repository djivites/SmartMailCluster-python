from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    """Each conversation thread (like your nextThreadId in C++)."""
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thread {self.id}"

class Email(models.Model):
    """Represents one email in the system."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_emails")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_emails")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Graph / Thread relationships
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="emails")
    parent_email = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="replies")

    def __str__(self):
        return f"Email {self.id} | {self.subject}"
