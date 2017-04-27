from django.conf.urls import url
from Analyzer import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sentiment_scores/$', views.sentiment_scores, name='sentiment_scores'),
    url(r'^show_database/$', views.show_database, name='show_database'),
    url(r'^trending/$', views.trending, name='trending'),
    url(r'^show_trending/$', views.show_trending, name='show_trending'),
    url(r'^show_firebase$', views.show, name='show'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^add_feedback/$', views.add_feedback, name='add_feedback'),
]