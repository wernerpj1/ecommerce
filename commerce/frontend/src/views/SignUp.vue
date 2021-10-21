<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title has-text-white">Cadastre-se</h1>

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
                        <label class=" has-text-white">Senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label class=" has-text-white">Repita a senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Cadastre</button>
                        </div>
                    </div>

                    <hr>

                    <p class="has-text-white"> Ou <router-link to="/log-in">clique aqui</router-link> para entrar! </p>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            email: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('O e-mail de cadastro está faltando')
            }

            if (this.password === '') {
                this.errors.push('A senha é muito curta')
            }

            if (this.password !== this.password2) {
                this.errors.push('As senhas devem ser iguais')
            }

            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password
                }

                axios
                    .post("/api/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Conta criada, por favor faça o Log-in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Ops, algo errado aconteceu. Por favor tente novamente')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>
<style scoped>
.page-sign-up {
    width: 70vw;
    min-height: 100vh;
}
</style>