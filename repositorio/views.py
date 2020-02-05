from django.shortcuts import render
from django.utils import timezone
from .models import *
from rest_framework import generics
from repositorio.serializers import *

class RolList(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})