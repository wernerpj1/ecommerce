<template>
    <div class="page-product">
        <div class="column is-multiline">
                <h1 class="title has-text-centered">Informações sobre o Produto</h1>
                
            </div>
        <div class="columns is-multiline">
            
       <div class="column is-6">
           <div>
                <figure class="image mb-6 img-magnifier-container">
                    <img id="myimage" class="imagem" v-bind:src="product.get_image">
                </figure>
            
            </div>
         </div>
            <div class="column is-1"></div>

            <div class="column is-3">
                <h2 class="title has-text-white">{{ product.nome }}</h2>
                
                <h2 class="has-text-white">{{ product.descricao_breve }}</h2>
                <br>
                <p class="has-text-white subtitle"><strong class="has-text-white">Preço: </strong> R$ {{ product.get_price }}</p>
                 <br>
                 <div class="field has-addons">
                    <div class="control">
                      <input type="text" class="input" :class="cep == '' ? 'is-danger':''"  placeholder="Digite seu CEP" v-model="cep">
                    </div>

                  </div>
                  <div class="field has-addons">
                      <div class="select" :class="tipo == '' ? 'is-danger':''">
                          <select v-model="tipo">
                            <option value="04510">PAC</option>
                            <option value="04014">Sedex</option>
                          </select>    
                      </div>
                      
                      <div class="control">
                      <button class="button is-success" @click="postCep()">
                          <span class="icon">
                          <i class="fas fa-search"></i>
                          </span>
                      </button>                      
                    </div>
                  </div>
                  <p v-if="tipo===''" class="help is-danger ">Selecione a forma de entrega</p>
                      <div class="control mt-1">
                         <span class="is-medium has-text-white"> <p>Valor da entrega:  R$ {{ dadosFrete.Valor }}</p></span>
                      </div>                         
                    <div class="control mt-1">
                         <span class="is-medium has-text-white"> <p>Prazo: {{ dadosFrete.PrazoEntrega }} dia(s)</p></span>                        
                    </div>
                    
                    <div class="control mt-1">
                        <p class="subtitle has-text-white">Valor Total: {{ valorTotal }}</p>

                        <div class="field has-addons mt-7">  
                    <div class="control" >
                        <input type="number" class="input" min="1" v-model="quantity" style="width: 70px">
                    </div>

                    <div class="control" v-if="parseFloat(dadosFrete.Valor) > 0">
                        <a class="button is-dark" @click="addToCart()">Colocar no carrinho</a>
                    </div>
                        </div>                  
                
                </div>
            </div>
            
            <div class="column is-9">
                <h1 class="title has-text-white">{{ product.nome }}</h1>
                <br/>
                <div class="has-text-white" v-html="product.descricao"></div>

                

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import "../glass.css";

export default {
    name: 'Product',
    
    data() {
        return {
            product: {},
            quantity: 1,
            cep: '',
            dadosFrete: '',
            tipo: '',
            valorTotal: '',
            
        }
    },
    mounted() {
        this.getProduct()
        
        function magnify(imgID, zoom) {
    var img, glass, w, h, bw;
    img = document.getElementById(imgID);
    /*create magnifier glass:*/
    glass = document.createElement("DIV");
    glass.setAttribute("class", "img-magnifier-glass");
    /*insert magnifier glass:*/
    img.parentElement.insertBefore(glass, img);
    /*set background properties for the magnifier glass:*/
    glass.style.backgroundImage = "url('" + img.src + "')";
    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;
    /*execute a function when someone moves the magnifier glass over the image:*/
    glass.addEventListener("mousemove", moveMagnifier);
    img.addEventListener("mousemove", moveMagnifier);
    /*and also for touch screens:*/
    glass.addEventListener("touchmove", moveMagnifier);
    img.addEventListener("touchmove", moveMagnifier);
    function moveMagnifier(e) {
      var pos, x, y;
      /*prevent any other actions that may occur when moving over the image*/
      e.preventDefault();
      /*get the cursor's x and y positions:*/
      pos = getCursorPos(e);
      x = pos.x;
      y = pos.y;
      /*prevent the magnifier glass from being positioned outside the image:*/
      if (x > img.width - (w / zoom)) {x = img.width - (w / zoom);}
      if (x < w / zoom) {x = w / zoom;}
      if (y > img.height - (h / zoom)) {y = img.height - (h / zoom);}
      if (y < h / zoom) {y = h / zoom;}
      /*set the position of the magnifier glass:*/
      glass.style.left = (x - w) + "px";
      glass.style.top = (y - h) + "px";
      /*display what the magnifier glass "sees":*/
      glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
    }
    function getCursorPos(e) {
      var a, x = 0, y = 0;
      e = e || window.event;
      /*get the x and y positions of the image:*/
      a = img.getBoundingClientRect();
      /*calculate the cursor's x and y coordinates, relative to the image:*/
      x = e.pageX - a.left;
      y = e.pageY - a.top;
      /*consider any page scrolling:*/
      x = x - window.pageXOffset;
      y = y - window.pageYOffset;
      return {x : x, y : y};
    }
  }
  //Image Magnifire Calls
  setTimeout(function(){ 
  magnify("myimage", 3);
   }, 1000);

        
    },

    
    methods: {
        postCep(){
            
            axios
                .post('/api/frete/?cep='+this.cep+
                '&tipo='+this.tipo+
                '&peso='+this.product.peso+
                '&altura='+this.product.altura+
                '&largura='+this.product.largura+
                '&comprimento='+this.product.comprimento)
                .then(response => {
                    this.dadosFrete = response.data
                    const valorProduct = parseFloat(String(this.product.get_price).replace(',', '.'))
                    const valorFrete = parseFloat(this.dadosFrete.Valor.replace(',', '.'));
                    
                    this.valorTotal = (valorFrete + valorProduct)
                    
                })
           
        },         

        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | Máquinas Ferreira'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity,
                valorTotal: this.valorTotal,
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'O produto foi adicionado no carrinho',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        },

    }
}
</script>

<style scoped>
.page-product {
    width: 90vw;
}
.imagem {
    
    max-height: 450px;
    max-height: 550px;
    
    box-shadow: 0 0 1em rgb(78, 78, 77)
    
}
.title.has-text-centered {
    padding: 3%;
    color: rgb(255, 255, 255);
}

</style>