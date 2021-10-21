from django.http import HttpResponse

from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import urllib.request
import xmltodict
from .models import Product, Category, Marca
from .serializers import ProductSerializer, CategorySerializer, MarcaSerializer

@api_view(['POST'])
def buscarCep(request):
    cep = request.GET.get("cep")
    tipo = request.GET.get("tipo")
    peso = request.GET.get("peso")
    if cep:
        url = ('http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?sCepOrigem=80410220&sCepDestino='+str(cep)+'&nVlPeso='+str(peso)+'&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&nVlDiametro=0&nCdServico='+str(tipo)+'&nCdEmpresa=&sDsSenha=&sCdMaoPropria=s&nVlValorDeclarado=0&sCdAvisoRecebimento=s&StrRetorno=xml&nIndicaCalculo=3')
        file = urllib.request.urlopen(url)
        data = file.read()
        file.close()
        data = xmltodict.parse(data)        
        dadosEntrega = data['Servicos']['cServico']
        return Response(dadosEntrega)
    else:
        return Response('Something is wrong')


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:9]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(categorias_id__slug=category_slug).get(url_externo=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class MarcaDetail(APIView):
    def get_object(self, marca_slug):
        try:
            return Marca.objects.get(slug=marca_slug)
        except Marca.DoesNotExist:
            raise Http404
    
    def get(self, request, marca_slug, format=None):
        marca = self.get_object(marca_slug)
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)



@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
