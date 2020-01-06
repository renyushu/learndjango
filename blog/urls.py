from django.urls import path
from . import views

app_name = 'blog' # 通过app_name定义了一个命名空间，方便以应用为中心组织URL并且通过名称对应到URL上。
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # 然后使用path()设置了两条具体的URL pattern。第一条没有任何的参数，对应post_list视图。
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]