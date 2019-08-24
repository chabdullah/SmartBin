from django.urls import path

from . import views

app_name = 'history'

urlpatterns = [
    # ex: /history/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /history/5/
    path('<int:material_id>/', views.detail, name='detail'),
    path('<int:material_id>/<int:mesured_weight>/update', views.update, name='update'),
    path('api/chart/data', views.ChartData.as_view())

]