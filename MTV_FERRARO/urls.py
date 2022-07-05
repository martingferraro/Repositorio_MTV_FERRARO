"""MTV_FERRARO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Appfamiliares.views import Familiar
from Appfamiliares.views import padre
from Appfamiliares.views import madre
from Appfamiliares.views import hermano
from Appfamiliares.views import padre_template
from Appfamiliares.views import madre_template
from Appfamiliares.views import hermano_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar/', Familiar),
    path('padre/', padre),
    path('madre/', madre),
    path('hermano/', hermano),
    path('padretemplate/', padre_template),
    path('madretemplate/', madre_template),
    path('hermanotemplate/', hermano_template),

]
