from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .forms import FormPub

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

def detalle_pub(request, pk):
    p = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', {'p': p})

def nueva_pub(request):
    if request.method == "POST":
        formulario = FormPub(request.POST)
        if formulario.is_valid():
            pub = formulario.save(commit=False)
            pub.autor = request.user
            pub.fecha_publicacion = timezone.now()
            pub.save()
            return redirect('detalle_pub', pk=pub.pk)
    else:
        formulario = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': formulario})

