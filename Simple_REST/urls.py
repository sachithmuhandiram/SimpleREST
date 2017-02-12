from django.conf.urls import url
from django.contrib import admin

#Returns a URL pattern list which includes format suffix patterns appended to each of the URL patterns provided.
from rest_framework.urlpatterns import format_suffix_patterns	#format_suffix_patterns(urlpatterns, suffix_required=False, allowed=None)

from simple_rest import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^title/$',views.SimpleAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
