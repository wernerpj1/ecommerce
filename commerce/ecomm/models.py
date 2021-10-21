from django.db import models
from autoslug import AutoSlugField
from io import BytesIO
from PIL import Image

from django.core.files import File

class Category(models.Model):
    name = models.CharField(primary_key= True,  max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Marca(models.Model):
    name = models.CharField(max_length=30, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    
    tipo = models.CharField(max_length=20, null=True)
    ref = models.CharField(max_length=20, null=True)
    nome = models.CharField(max_length=200, null=True)
    publicado = models.BooleanField(default=False, null=True)
    em_destaque = models.BooleanField(default=False, null=True)
    visibilidade_no_catálogo = models.CharField(max_length=20, null=True)
    descricao_breve = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=500, null=True)
    data_de_inicio_do_preco_promocional = models.DateField(null=True)
    data_de_termino_do_preco_promocional = models.DateField(null=True)
    situacao_fiscal = models.CharField(max_length=15, null=True)
    classe_de_imposto = models.CharField(max_length=20, null=True)
    em_stock = models.BooleanField(default=True, null=True)
    stock = models.DecimalField(max_digits=6, decimal_places=0, default=0, null=True)
    valor_de_stock_baixo = models.DecimalField(max_digits=6, decimal_places=0, default=0, null=True)
    permitir_encomendas_pendentes = models.BooleanField(default=True)
    vender_individualmente = models.BooleanField(default=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    comprimento = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    largura = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    altura = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True)
    permitir_avaliacoes_de_clientes = models.BooleanField(default=True)
    nota_da_encomenda = models.FileField(null=True)
    preco_promocional = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    preco_normal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    categorias = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    etiquetas = models.ImageField(upload_to='etiquetas/', blank=True, null=True) 
    classes_de_envio = models.CharField(max_length=20, null=True)
    imagens = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    limite_de_descarregamento = models.DecimalField(max_digits=6, decimal_places=0, default=0, null=True)
    dias_para_expirar_o_descarregamento = models.DecimalField(max_digits=6, decimal_places=0, null=True)
    pai = models.CharField(max_length=20, null=True)
    produtos_agrupados = models.CharField(max_length=50, null=True)
    aumenta_vendas = models.BooleanField(default=False, null=True)
    vendas_cruzadas = models.BooleanField(default=False, null=True)
    url_externo = AutoSlugField(populate_from='id')
    texto_do_botao = models.CharField(max_length=15, null=True)
    posicao = models.CharField(max_length=20, null=True)
    marca = models.ForeignKey(Marca, related_name='products', on_delete=models.CASCADE)

    class Meta: 
        ordering = ('-em_destaque',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return f'/{self.categorias.slug}/{self.url_externo}/'

    def get_image(self):
            if self.imagens:
                return 'http://127.0.0.1:8000' + self.imagens.url
            return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.imagens:
                self.thumbnail = self.make_thumbnail(self.imagens)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, imagens, size=(300, 200)):
        img = Image.open(imagens)        
        img = img.convert("RGB")        
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=imagens.name)
        return thumbnail

    def get_price(self):
        if self.preco_promocional:
            return self.preco_promocional
        return self.preco_normal

    

