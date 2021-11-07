<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <br>
                <h1 class="title has-text-white">Log-In</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                    <label class="label has-text-white">Email</label>
                    <div class="control has-icons-left has-icons-right">
                        <input  class="input is-danger has-text-grey" v-model="email" type="email" placeholder="Example@example.com">
                        <span class="icon is-small is-left">
                        <i class="fas fa-envelope"></i>
                        </span>
                        <span class="icon is-small is-right">
                        <i class="fas fa-exclamation-triangle"></i>
                        </span>
                    </div>
                    <p v-if="verificaEmail" class="help is-danger">Este e-mail é inválido</p>
                    </div>

                    <div class="field">
                        <label class="has-text-white">Senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field columns">
                        <div class="control column">
                            <button class="button is-dark has-text-white">Entrar</button>
                        </div>
                        
                    </div>
                     
                    <div class="column is-12" v-if="isHidden">
                        <reset-password/>
                    </div>
                    <hr>

                    <label for="" class="has-text-white">   Ou <router-link to="/sign-up">clique aqui</router-link> para se cadastrar!</label>
                </form>
                <div class="control column">
                    <button v-on:click="isHidden = !isHidden" class="button is-danger btn">Mudar senha</button>                
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ResetPassword from '../components/resetPassword.vue'
export default {
    name: 'LogIn',
    data() {
        return {
            email: '',
            password: '',
            errors: [],
            isHidden: false,
        }
    },
    components: {
        ResetPassword
    },
    mounted() {
        document.title = 'Logar - Máquinas Ferreira'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                email: this.email,
                password: this.password
            }

            await axios
                .post("/api/token/login/", formData)
                .then(response => {
                    const user = this.email
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    this.$store.commit('setUser', this.email)
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    localStorage.setItem("username", user)

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                    
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Ops, algo de errado aconteceu. Por favor tente de novo')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>

<style scoped>
.page-log-in {
    width: 70vw;
    min-height: 100vh;
}
</style>