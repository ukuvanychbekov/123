from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import *
from .seriaizers import CategorySerializer, BookSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class CategoryGenericViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookGenericViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
