<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered has-text-white">{{ category.name }}</h2>
            </div>
            
        
            
            <nav class="column categoryList ">                
            <ProductBox class="categoryItem"
                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product" />
            </nav>
            
        
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProductBox from '../components/ProductBox.vue'

export default {
    name: 'Category',
    components: {
        ProductBox
    },
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/products/categoria/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = 'Máquinas de Costura - ' + this.category.name 
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.',
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
.page-category {
    justify-content: center;
}
.categoryList {
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
.categoryItem {
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