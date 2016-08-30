"""nmid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from camp_fin.views import IndexView, CandidateList, CandidateDetail, OfficeDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^candidates/$', CandidateList.as_view(), name='candidate-list'),
    url(r'^offices/(?P<slug>[\w-]+)/$', OfficeDetail.as_view(), name='office-detail'),
    url(r'^candidates/(?P<pk>[0-9]+)/$', CandidateDetail.as_view(), name='candidate-detail')
]
