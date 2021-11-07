<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <hr>
            <div class="column is-12">
                <h1 class="title has-text-white">Minha Conta</h1>
            </div>
            <br>
            <div class="column is-2">
                <button @click="logout()" class="button is-danger btn">Sair</button>
            </div>
            
            <hr>
            <br>
            <div class="column is-12">
                <h2 class="subtitle has-text-white">Minhas Ordens</h2>
                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import OrderSummary from '@/components/OrderSummary.vue'
export default {
    name: 'MyAccount',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'Minha conta - Máquinas Ferreira'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/orders/')
                .then(response => {
                    this.orders = response.data
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
.page-my-account {
    min-width: 70vw;
    min-height: 100vh;
    margin-top: 10vh;
}
.btn {
    width: 150px;
}
</style>