from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'colors', views.ColorViewSet)

urlpatterns=[
	url(r'^',  include(router.urls))

	# url(r'^Colores/$',
	# 	views.ColorListView.as_view(),
	# 	name = "color_list"),

	# url(r'^Colores/(?P<pk>\d+)/$',
	# 	views.ColorDetailsView.as_view(),
	# 	name = "color_detail"),

	# url(r'^Colores/crear/',
	# 	views.ColorCreateView.as_view(),
	# 	name = 'color_crear'),

	# url(r'^Colores/modificar/(?P<pk>\d+)/$',
	# 	views.ColorUpdDesView.as_view(),
	# 	name = 'color_modificar'),
]