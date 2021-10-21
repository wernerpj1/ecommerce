<template>
    <div class="page-search">
        <div class="column">
            <div class="column is-full">
                <h1 class="title has-text-white">Procurar</h1>

                <h2 class="is-size-5 has-text-white">Procurando por: "{{ query }}"</h2>
            </div>
            <div class="prodSearch">
                
            <ProductBox class="productSearch"
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product" />
            
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
    name: 'Search',
    components: {
        ProductBox
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Procurar no site'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/products/search/', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
<style scoped>
.page-search {
    width: 95.5vw;
}
.prodSearch {
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
.productSearch {
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