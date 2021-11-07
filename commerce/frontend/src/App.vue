<template>
  <div id="wrapper">
      <nav class="navbar is-black is-fixed-top" style="position: -webkit-sticky; position: sticky; top: 0;">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <figure class="image mb-2">
                <img src="./assets/logo1.png">
            </figure>
          </router-link>

          <a role="button" class="navbar-burger login" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div class="navbar-menu " id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
         <div class="navbar-start">
           <div class="navbar-item">
             <form method="get" action="/search">
             <div class="field has-addons search">
                
               <div class="control">
                 <input type="text" class="input is-rounded" placeholder="    O que você está procurando?    " name="query">
               </div>
                <div class="control">
                 <button class="button site-color has-text-primary-light is-rounded no-border">
                   <span class="icon">
                     <i class="fas fa-search"></i>
                   </span>
                 </button>
               </div>
              
             </div>
             </form>
           </div>
         </div>
          <div class="navbar-end">
            
            
            <div class="navbar-item">
              <div class="buttons">
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="button has-background-black has-text-white no-border"><span class="icon"><i class="fas fa-user"></i></span> <span>Minha Conta</span></router-link>
                </template>
                <template v-else>
                  <router-link to="/login" class="button is-light has-text-white has-background-black">
                  <span class="icon"><i class="fas fa-user"></i></span> <span>Login</span></router-link>
                </template>
                <router-link to="/cart" class="button has-text-white has-background-black no-border">
                  <span class="icon"><i class="fas fa-cart-plus"></i></span>
                  <span>Carrinho ({{ cartTotalLength }})</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
     
  <section class="category">  
    
      <a role="button" class="navbar-burger has-text-white has-background-black" aria-label="menu" aria-expanded="false" data-target="navbar-categ" @click="dropDown = !dropDown">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
     <div id="navbar-categ" class="navbar-menu navbar-categ" v-bind:class="{'is-active dropcat': dropDown}"> 
      
            <router-link to="/domesticas" class="navbar-item dropitem">Domésticas</router-link>
            <router-link to="/industriais" class="navbar-item dropitem">Industriais</router-link>
            <router-link to="/overlocks" class="navbar-item dropitem">Overlock's</router-link>
            <router-link to="/bordadeiras" class="navbar-item dropitem">Bordadeiras</router-link>
            <router-link to="/pecas_e_acessorios" class="navbar-item dropitem">Peças e Acessórios</router-link>
            <router-link to="/patchwork" class="navbar-item dropitem">Patchwork</router-link> 
            <router-link to="/contato" class="navbar-item dropitem">Assistência Técnica e Contato</router-link>
   </div>
  </section>

  <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

  <section class="section router">  
    <router-view/>
  </section> 
  
  <div class='layout' style="background-color: blue">
    <!-- ommited -->
    <SocialChat
      icon
      class="whats-chat"
      :attendants="attendants"
    >
      <template #header>
        <p>Clique para falar com um dos nossos atendentes</p>
      </template>
      <template #button >
        <img
          src="https://raw.githubusercontent.com/ktquez/vue-social-chat/master/src/icons/whatsapp.svg"
          alt="icon whatsapp"
          aria-hidden="true"
        >      
      </template>
      <template #footer>
        <small>Aberto: das 8:00 às 18:00</small>
      </template>
    </SocialChat>
  </div>
  
  <footer class="footer">
    <div class="columns is-multiline has-text-centered">
      <div class="column">
        <h1 class="title">Localização</h1>
        <p class="subtitle ">R. Cruz Machado N°385 <br>Centro Curitiba</p>
      </div>
      <div class="column">
        <h1 class="title">Horário (loja fisica)</h1>
        <p class="subtitle">Seg. à Sex. Das 8:00 às 18:00 <br> Sábado das 8:00 às 12:00</p>
      </div>
      <div class="column">
        <h1 class="title">Contato</h1>
        <p class="subtitle">(41)3225-2797</p>
      </div>
    </div>
    <p class="has-text-centered"> Author: Werner Purens Jacob </p>
    <p class="has-text-centered"><i class="fas fa-star-of-david"></i> Direitos reservados a Mashiach, Inc 2021 <i class="fas fa-star-of-david"></i></p>
  </footer>

  </div>
</template>

<script>
import axios from 'axios'
import Slider from './components/slider/Slider.vue'
import Carousel from './components/slider/Carousel.vue'
import image1 from './assets/carrousel/sewing1.jpg'
import image2 from './assets/carrousel/sewing2.jpg'
import image3 from './assets/carrousel/tail.jpg'
import image4 from './assets/carrousel/emb1.jpg'
import image5 from './assets/carrousel/emb2-red.jpg'
import { SocialChat } from 'vue-social-chat'
import 'vue-social-chat/dist/style.css'


export default {
  components: { Carousel, Slider, SocialChat },
     

    data() {
      return {
        showMobileMenu: false,
        dropDown: false,
        cart: {
          items: []
        },
        slides: [
            image1,
            image2,
            image3,
            image4,
            image5
        ],
               
      }
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    mounted() {
      this.cart = this.$store.state.cart
      
    },
    computed: {
      cartTotalLength() {
        let totalLength = 0

        for (let i = 0; i < this.cart.items.length; i++) {
            totalLength += this.cart.items[i].quantity
        }
        return totalLength
      }
    },
     setup () {
    const attendants = [
      {
        app: 'whatsapp',
        label: 'Suporte Técnico',
        name: 'Afonso',
        number: '5541984820780',
        avatar: {
          src: require('./assets/afonso.png'),
          alt: 'Afonso Ferreira'
        }
      },
      // ...
    ]

    return { attendants }
  }

}
</script>

<style lang="scss">
@charset "utf-8";
@import '../node_modules/bulma';
#navbar-menu {
  background-color: black;  
}

#wrapper {
  width: 100vw;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  backface-visibility: hidden;
  animation: slideBg 300s linear infinite;
  animation-timing-function:ease-in-out;
  background-image: url('./assets/carrousel/carousel2.png');
  padding: 0%;
  margin: 0%;
  justify-content: center;
  
}
@keyframes slideBg {
   0%, 
   20% {
     background-image: url('./assets/carrousel/carousel2.png');
   }
   25%, 
   45% {
     background-image: url('./assets/carrousel/emb2.jpg');
   }
   50%,
   70% {
     background-image: url('./assets/carrousel/carousel1.jpg');
   }
   75%, 
   100% {
     background-image: url('./assets/carrousel/sewing2.jpg');
   }
   
}
.navbar-burger.login {
  margin-left: 1vh;
}
.navbar-burger.has-text-white {
  margin-left: 0vh;
}
#navbar-categ {
  background-color: black;
}
.navbar-item.dropitem {
  color: white;
}

.is-active {
  position: absolute;
  left: 0px;
  z-index: 1;
  opacity: 85%;
  animation: slideLeft 500ms ease-in-out;
}
@keyframes slideLeft {
  from {
        transform: translateX(-300px);
        opacity: 0%;
    }
    to {
        transform: translateX(0px);
        opacity: 85%;
    }
}
@media (min-width: 1009px) {
  #navbar-categ {
    background-color: rgb(54, 54, 54);
    width: 100vw;
    justify-content: center;
  }
  .navbar-item.dropitem:hover {
  background-color: rgb(54, 54, 54);
  
}
}
.site-color {
  background-color: rgb(218, 86, 38);
}
.no-border {
  border: 0px;
}
.no-border:hover {
  border: 0.5px white solid;
}
.section { 
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  animation: routerView 1.5s;
  margin: 0%;
  padding: 0%;
}
@keyframes routerView {
  from {
        transform: translateX(1000px);
    }
    to {
        transform: translateX(0px);
    }
}

.category {
    animation: categoryMenu 1.5s;    
}
@keyframes categoryMenu {
    from {
        transform: translateX(-1000px);
    }
    to {
        transform: translateX(0px);
    }
  }

@media (max-width: 1080px) {

}
.whats-chat {
  --vsc-bg-button: green;
}


.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

</style>
