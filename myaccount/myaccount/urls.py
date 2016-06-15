from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r"^account/", include("account.urls")),
    url(r"^blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    url(r"^likes/", include("pinax.likes.urls", namespace="pinax_likes")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
