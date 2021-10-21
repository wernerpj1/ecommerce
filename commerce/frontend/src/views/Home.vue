<template>  
  <div class="home">
    <section class="hero is-medium is-transparent mb-6">
      <p class="title mb-6 has-text-white">
        Bem Vindo(a) a Loja do Ferreira
      </p>
      <p class="subtitle is-black mb-6 has-text-white">
        A melhor loja de máquinas de costura de Curitiba
      </p>
    </section>
    
    <div class="columns is-multiline alinhar">
      <div class="column is-12">
          <p class="title has-text-centered has-text-white">Destaques</p> 
      </div>

      <div class="column  carousel-view"> 
        <transition-group class='carousel'
                          tag="ProductBox">      
                              <ProductBox 
                                class='slide'
                                v-for="product in listProducts"
                                v-bind:key="product.id"
                                v-bind:product="product" />
        </transition-group>
        <div class='carousel-controls'>
        <button class='carousel-controls__button btnprev' @click="previous">&#10094; Anterior</button>
        <button class='carousel-controls__button btnnext' @click="next">&#10095; Próximo</button>
        </div>
      </div>
     </div>
     
  
  <br>
   <br>
    <h2 class="title has-text-centered has-text-white">Grandes Marcas</h2>
    
    <p>{{brand}}</p>
    
    
    <article class="panelBrand columns is-multiline has-text-centered">
      
      
      
      <Brands id="singer" class="brandsSpace column" brand="singer"/>
      <Brands id="jenome" class="brandsSpace column" brand="jenome"/> 
      <Brands id="brother" class="brandsSpace column" brand="brother"/> 
     
    </article>
    
  
  <br>

  <article class="columns">
    <iframe width="560" height="315" class="column video" src="https://www.youtube.com/embed/videoseries?list=PL06oyL9cc1fq19Nz8gqk8g-fynv2fvV8Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" class="column video" src="https://www.youtube.com/embed/BgtwGK6JDfw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </article>
  <br>
  <div class="map">
    <section class="section map">
    <Map/>
  </section>
      
  </div>

  


  </div>
</template>
<script>
// @ is an alias to /src
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
import Map from '@/components/Map'
import Slider from '@/components/slider/Slider'
import carousel from '../components/slider/Carousel.vue'
import Brands from '@/components/Brands'


export default {
  name: 'Home',
  data() {
      return {
        listProducts: [],
        brand: '',
        brand1: null,
        brand2: 'jenome',
        brand3: 'brother'
      }
  },
  components: {
    ProductBox,
    Map,
    Slider,
    carousel,
    Brands
  },

    mounted() {
    this.getListProducts()
  },
  
  methods: {

    async getListProducts() {
      await axios
        .get('api/lista/',)
        .then(response => {
          this.listProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    next () {
      const first = this.listProducts.shift()
      this.listProducts = this.listProducts.concat(first)
    },
    previous () {
      const last = this.listProducts.pop()
      this.listProducts = [last].concat(this.listProducts)
    }
  }
  

   
  }

</script>
<style scoped>
  .carousel-view {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  width: 100%;
  justify-content: center;
  
}
.carousel {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  width: 70vw;
  min-height: 25em;
  
}
.carousel-controls {
  position: absolute;
  width: 95vw;
  
  
}
.slide {
  width: 50px;
  flex: 0 0 20em;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: transform 0.3s ease-in-out;
  
}
.slide:first-of-type {
  opacity: 0;
}
.slide:last-of-type {
  opacity: 0;
}
.btnprev, .btnnext {
  cursor: pointer;
  position: absolute;
  top: 40%;
  width: auto;
  padding: 16px;
  color: rgb(212, 209, 209);
  background-color: transparent;
  font-weight: bold;
  font-size: 18px;
  transition: 0.7s ease;
  text-decoration: none;
  user-select: none;
  border: none;
}
.btnnext {
  right: 0;
}
.btnprev {
  left: 0;
}
/* On hover, add a black background color with a little bit see-through */
.btnprev:hover, .btnnext:hover {
  background-color: black;
  color: white;
}
  .home {
    padding: 0%;
    margin: 0%;
    width: 100%;
    position: relative;
    background-repeat: no-repeat;
    background-size: 100%;    
    color: black;
    padding: 7%;
    box-shadow: 0 0 1em rgb(78, 78, 77);
    height: auto;
    justify-content: center;
    
  } 
 .panelBrand {   
    height: 700px;
    display: flex;
    align-content: center;
 }
.brandsSpace {
  padding: 3vw;
  cursor: pointer;
}
@media (max-width: 1350px) {
  .panelBrand {
    position: relative;
    display: flex;
    flex-direction: column;
    min-height: 1550px;
    align-content: center;
    
  }
}
.video {
  min-height: 300px;
}
 
  
</style>