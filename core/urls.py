from django.urls import path
from core import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new_post/', views.new_post, )
    path('detail/<int:post_id>', views.post_detail, name='post_detail'),

]
