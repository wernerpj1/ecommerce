<template>
    <div class="brandWrapper has-text-centered" @click="redirectToBrandsView">
        <label class="brandLabel title has-text-white ">{{brand}}</label>
        <div class="brandRotate">      
            <ProductBox 
            class="brandProduct"
            :class="brandSize"
            v-for="product in brands.products"
            v-bind:key="product.id"
            v-bind:product="product" />
      </div>
    </div>
</template>
<script>

import axios from 'axios'
import ProductBox from '@/components/ProductBox'
export default {
    name: 'Brands',
    props:
        ['brand']
    ,
    data() {
        return {
            brands: { products: [],
            
            }

        }
    }, 
    components: {
        ProductBox        
        },
    mounted() {
        this.getListBrands()
    },
    methods: {

        async getListBrands() {
            await axios
            .get('api/marca/'+this.brand+'/')
            .then(response => {
                this.brands = response.data
            })
            .catch(error => {
                console.log(error)
            })
        },
        async redirectToBrandsView() {
             this.$router.push(
        {
          path: '/marca/'+this.brand+'/'
        } )
           
        }
    }
}
</script>
<style scoped>
.brandSize {
    width: 50px;
        
}
.brandWrapper {
    width: 30vw;
    height: 40vw;
    transform-style: preserve-3d;
    perspective: 1000px;
    align-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
}
.brandLabel {
    text-transform: capitalize;
}
.brandRotate {
     background-color: chartreuse;
    position: absolute;
    animation: brandsAnimate 45s ease-in-out infinite; 
    transform-style: preserve-3d;
    align-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
    width: 200px;
    
}
.brandRotate div {
    margin-top: 100px;
    width: 300px;
    height: 300px;
    position: absolute;
    
}

.brandProduct:nth-child(1)
{
    transform: translateZ(135px);   
}
.brandProduct:nth-child(2)
{
    transform: rotateY(90deg) translateZ(185px);
    
}
.brandProduct:nth-child(3)
{
    transform: rotateY(90deg) rotateX(90deg) translateZ(140px);
    
}
.brandProduct:nth-child(4)
{
    transform: rotateY(180deg) rotateZ(90deg) translateZ(185px);
    
}
.brandProduct:nth-child(5)
{
    transform: rotateY(-90deg) rotateZ(90deg) translateZ(140px);
    
}
.brandProduct:nth-child(6)
{
    transform: rotateX(-90deg) translateZ(185px); 
    
}

    @keyframes brandsAnimate {
        from,to{
            transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
        }
        16%{
            transform-origin: 80px 150px 0px;
            transform: rotateY(-90deg);
        }
        33%{
            transform-origin: -50px 100px 150px;
            transform: rotateY(-90deg) rotateZ(90deg);
        }
        50% {
            transform-origin: 20px 150px 0px;
            transform: rotateY(-180deg) rotateZ(90deg);
        }
        66% {
            transform-origin: 0px 150px 50px;
            transform: rotateY(-270deg) rotateX(90deg);
        }
        83% {
            transform-origin: 0px 300px 0px;
            transform: rotateX(90deg);
        }
    }   
</style>