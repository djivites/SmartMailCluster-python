from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import send_email, reply_email, forward_email
from .models import Email

@api_view(['POST'])
def send_email_view(request):
    data = request.data
    email = send_email(
        sender_id=data['sender'],
        receiver_id=data['receiver'],
        subject=data['subject'],
        body=data['body']
    )
    return Response({"message": "Email sent", "email_id": email.id, "thread_id": email.thread.id})

@api_view(['POST'])
def reply_email_view(request):
    data = request.data
    reply = reply_email(
        parent_email_id=data['parent_email'],
        sender_id=data['sender'],
        receiver_id=data['receiver'],
        body=data['body']
    )
    return Response({"message": "Reply sent", "reply_id": reply.id, "thread_id": reply.thread.id})

@api_view(['GET'])
def view_thread_view(request, thread_id):
    emails = Email.objects.filter(thread_id=thread_id).order_by('created_at')
    result = [{"id": e.id, "subject": e.subject, "body": e.body, "from": e.sender.username, "to": e.receiver.username} for e in emails]
    return Response({"thread_id": thread_id, "emails": result})
