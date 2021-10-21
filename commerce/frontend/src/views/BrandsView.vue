<template>
    <div class="page-brand">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered has-text-white">{{ brands.name }}</h2>
            </div>
            
        
            
            <nav class="column brandList ">                
            <ProductBox class="brandItem"
                v-for="product in brands.products"
                v-bind:key="product.id"
                v-bind:product="product" />
            </nav>
            
        
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
export default {
    name: 'BrandsView',
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
        this.listProducts()
    },
     watch: {
        $route(to, from) {
            if (to.name === 'BrandsView') {
                this.listProducts()
            }
        }
    },
   
    methods: {
        async listProducts() {
             const brandsSlug = this.$route.params.brands_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/marca/${brandsSlug}/`)
                .then(response => {
                    this.brands = response.data

                    document.title = 'Máquinas de Costura - ' + this.brands.name 
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Ops, algo deu errado tente de novo.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
<style scoped>
.page-brand {
    justify-content: center;
}
.brandList {
    display: flex;
    flex-wrap: wrap;
    max-width: 95.5vw;
    background-color: white;
    margin-left: auto;
    margin-right: auto;
    border-radius: 20px;
    align-items: center;
    align-content: center;
    justify-content: center;
}
.brandItem {
    max-width: 350px;
    width: fit-content;
    box-shadow: 0 0 1em gray;
    animation: comeon 1.5s;
    margin: 3%;
}
@keyframes comeon {
    from {
        transform: translateX(-700px);
    }
    to {
        transform: translateX(100px);
    }
}


</style>