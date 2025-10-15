from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesores

# Listar profesores
def index(request):
	profesores = Profesores.objects.all()
	return render(request, 'listar_profesores.html', {'profesores': profesores})

# Ver profesor
def listar_profesores(request, id):
	profesor = get_object_or_404(Profesores, id=id)  # Cambiar "estudiante" por "profesor"
	return render(request, 'listar_profesores.html', {'profesor': profesor})

# Agregar profesor
def agregar_profesores(request):  # Cambiar el nombre de la función para consistencia
	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellido_paterno = request.POST['apellido_paterno']
		apellido_materno = request.POST['apellido_materno']
		genero = request.POST['genero']
		correo = request.POST['correo']
		# Crear un nuevo profesor y guardarlo en la base de datos
		nuevo_profesor = Profesores(
			nombre=nombre,
			apellido_paterno=apellido_paterno,
			apellido_materno=apellido_materno,
			genero=genero,
			correo=correo
		)
		nuevo_profesor.save()
		return redirect('inicio')
	return render(request, 'agregar_profesores.html')

# Editar profesor
def editar_profesores(request, id):  # Cambiar el nombre de la función para consistencia
	profesor = get_object_or_404(Profesores, id=id)  # Cambiar "estudiante" por "profesor"
	if request.method == 'POST':
		profesor.nombre = request.POST['nombre']
		profesor.apellido_paterno = request.POST['apellido_paterno']
		profesor.apellido_materno = request.POST['apellido_materno']
		profesor.genero = request.POST['genero']
		profesor.correo = request.POST['correo']
		profesor.save()  # Guardar los cambios en la base de datos
		return redirect('inicio')
	return render(request, 'editar_profesores.html', {'profesor': profesor})

def borrar_profesores(request, id):
    profesor = get_object_or_404(Profesores, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('inicio')
    return render(request, 'borrar_profesores.html', {'profesor': profesor})