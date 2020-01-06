"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
]
"""
path参数：
    - route: 是一个匹配url的准则（类似正则表达式）。当Django响应一个请求时，它会从urlpatterns的第一项开始，
                按顺序一次匹配列表中的项，直到找到匹配的项

    - view: 当django找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个HttpRequest对象作为第一个参数，被"捕获"的参数以
            关键字的形式传入传入。
    


"""