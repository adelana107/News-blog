from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name='home'),
    path('article/<int:pk>', views.articlePage, name='article'), 
    path('all-news/', views.all_news, name='all-news'),
    path('main-news/', views.main_news, name='main-news'),
    path('featured-news/', views.featured_news, name='featured-news'),
    path('breaking-news/', views.breaking_news, name='breaking-news'),
    path('latest-news/', views.latest_news, name='latest-news'),
    path('trending-news/', views.trending_news, name='trending-news'),
    path('popular-news/', views.popular_news, name='popular-news'),
    path('submit-comment/<str:pk>/', views.articlePage, name='submit_comment'),
    path('search/', views.post_search, name='post_search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile-page/<int:pk>', views.profile_page, name='profile-page'),
    path('update-profile/<int:pk>', views.update_profile, name = 'update-profile'),
    path('create-post/<int:pk>', views.create_Post, name= 'create-post')
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

