from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Email
from .graph import Graph
from .cluster import Cluster
# create a single Graph instance
graph = Graph()

@api_view(['POST'])
def send_email_view(request):
    data = request.data
    email = graph.sendEmail(
        from_addr=data['sender'],
        to_addr=data['receiver'],
        subject=data['subject'],
        body=data['body']
    )
    graph.showgraph()
    return Response({
        "message": "Email sent",
        "email_id": email.email_id,
    })

@api_view(['POST'])
def reply_email_view(request):
    data = request.data
    reply = graph.replyEmail(
        email_id=data['parent_email'],
        from_addr=data['sender'],
        to_addr=data['receiver'],
        body=data['body']
    )
    if not reply:
        return Response({"error": "Original email not found"}, status=404)
    if reply == "ERROR":
        return Response({"error": "Invalid sender/receiver for reply"}, status=400)
    
    graph.showgraph()
    return Response({
        "message": "Reply sent",
        "reply_id": reply.email_id,
    })

@api_view(['POST'])
def forward_email_view(request):
    data = request.data
    fwd = graph.forwardEmail(
        email_id=data['parent_email'],
        from_addr=data['sender'],
        to_addr=data['receiver'],
        body=data['body']
    )
    if fwd == "ERROR":
        return Response({"error": "Invalid sender/receiver for forward"}, status=400)
    if not fwd:
        return Response({"error": "Original email not found"}, status=404)
    graph.showgraph()
    return Response({
        "message": "Forward sent",
        "forward_id": fwd.email_id,
    })

@api_view(['GET'])
def view_thread_view(request, root_email_id):
    result = graph.viewThread(root_email_id)
    return Response({
        "root_email_id": root_email_id,
        "emails": result
    })

@api_view(['GET'])
def cluster_emails_view(request):
    cluster = Cluster()
    email_clusters = cluster.cluster_emails(graph)

    # Convert IDs into full email details
    clusters_with_data = {}
    for root, members in email_clusters.items():
        clusters_with_data[str(root)] = list(
            Email.objects.filter(email_id__in=members).values(
                'email_id', 'sender', 'receiver', 'subject', 'body', 'parent_email_id', 'thread_id'
            )
        )

    return Response({
        "clusters": clusters_with_data
    })



@api_view(['GET'])
def view_all_emails(request):
    emails = Email.objects.all().values(
        'email_id', 'sender', 'receiver', 'subject', 'body', 'parent_email_id', 'thread_id'
    )
    return Response({
        "emails": list(emails)
    })
# --- NEW FUNCTION: List all threads with root email ---
@api_view(['GET'])
def view_all_threads(request):
    """
    Returns a list of all threads with root email info.
    Each thread includes:
        - thread_id
        - root_email (sender, receiver, subject, body)
    """
    # Get all root emails (emails with no parent)
    root_emails = Email.objects.filter(parent_email__isnull=True).values(
        'email_id', 'sender', 'receiver', 'subject', 'body', 'thread_id'
    )
    
    threads = []
    for root in root_emails:
        threads.append({
            "thread_id": root['thread_id'],
            "root_email": root
        })
    
    return Response({"threads": threads})


