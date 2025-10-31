from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_email_view),
    path('reply/', views.reply_email_view),
    path('forward/', views.forward_email_view),
    path('thread/<int:root_email_id>/', views.view_thread_view),   # View one thread (emails inside)
    path('emailcluster/', views.cluster_emails_view),
    path('emails/', views.view_all_emails),                        # View all emails
    path('threads/', views.view_all_threads),                      # View all threads (root emails)
]

