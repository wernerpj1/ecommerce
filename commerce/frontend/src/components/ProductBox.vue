<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-2">
                <img class="imgprod" v-bind:src="product.get_thumbnail">
            </figure>

            <h3 class="is-size-6">{{ product.nome }}</h3>
            <p class="is-size-6 has-text-danger">R${{ product.get_price }}</p>
            <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Ver detalhes</router-link>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>
<style scoped>
 

.box{
    height: 325px;
    width: 325px;
    box-shadow: none;
    
}
.imgprod {
    margin-left: auto;
    margin-right: auto;
    height: 150px;
    width: auto;
    
}
.button.is-dark.mt-4 {
    background-color: rgb(20, 20, 20);
    opacity: 85%;
}

</style>