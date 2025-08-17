from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_email_view),
    path('reply/', views.reply_email_view),
    path('thread/<int:thread_id>/', views.view_thread_view),
]
