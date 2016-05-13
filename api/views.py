from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import ClorsForm
from .models import Colors
import json
# Create your views here.

def index(request):
	return HttpResponse("Esta es mi pagina principal JOJO")

class HomeView(View):
	def get(self, request):
		return HttpResponse("<h1>Hola " + nombre + "<h1>")

class IndexView(View):
	def get(self, request):
		get_params = request.GET
		nombre = get_params.get("nombre", "Fulano")
		return HttpResponse("Esto es un parametro: " + nombre)

	@method_decorator(csrf_exempt)
	def post(self,request):
		get_params = request.POST
		nombre = get_params.get("nombre","Fulano")
		return HttpResponse("Esto es un Post")

	def delete(self,request):
		return HttpResponse("Esto es un delete")

	def put(self,request):
		return HttpResponse("Esto es un put")


class GreetView(View):
	def get(self,request, nombre):
		return HttpResponse("<h1>Hola " + nombre + "<h1>")

class JsonView(View):
	def get(self, request):
		return HttpResponse("""{"grupo": "Cinta negra", "integrantes": ["Salvador", "Ivan", "Wili"]""", content_type='application/json')

	def post(self, request):
		my_json = {'colors': ['azul', 'blanco']}
		color = request.POST.get('color')
		if color:
			my_json['colors'].append(color)

		return HttpResponse(json.dumps(my_json), content_type='application/json')

class ColorView(View):
	colores = {
		'rojo': "#FF0000",
		'azul': "#0000FF"
	}
	def get (self, request, color):
		hex = self.colores.get(color)
		if hex:
			resp={'status':'ok', 'hex': hex}
		else:
			resp={'status': 'erro', 'message': 'Color no available'}

		return HttpResponse(json.dumps(resp), content_type='application/json')

class ColorsView(View):
	def get(self, arg):
		list_color = []
		colors = Colors.objects.all()
		for c in colors:
			dict_color = {
				'name' : c.name,
				'hexadecimal' : c.hexadecimal,
				'red' : c.red,
				'green' : c.green,
				'blue' : c.blue,
			}
			list_color.append(dict_color)
		my_colorjason = {'colors': len(list_color)}
		return HttpResponse(json.dumps(my_colorjason), content_type='application/json')

class AddColor(View):
	def get(self,request):
		template_name="api/colores.html"
		form = ClorsForm()
		context = {'form': form}
		return render(request, template_name, context)
	def post(self,request):
		colorform = ClorsForm(request.POST)
		if colorform.is_valid():
			colorform = colorform.save()
			return HttpResponse("ok")
		else:
			return HttpResponse("Horro!!!")

class DisplayColors(view):
	def get(self, request):
		template_name = "api/display_colors.html"
		return render(request,)