<template>
    <div id="page-resetpassword">
        <form @submit.prevent="submitForm">
        <div class="field">
            <label class="label has-text-white">Email</label>
            <div class="control has-icons-left has-icons-right" style="width: 30vw; min-width: 200px;">
                <input  class="input is-danger has-text-grey " v-model="email" type="email" placeholder="Example@example.com">
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
            <div class="control">
                <button class="button is-dark">Enviar</button>
            </div>
        </div>
        </form>
    </div>    
</template>
<script>
import { toast } from 'bulma-toast'
import axios from 'axios'
export default {
    name: 'resetpassword',
    data(){
        return {
            email: '',
            errors: []
        }
    },
    methods: {
        async submitForm(){
            this.$store.commit('setIsLoading', true)
            this.errors = []
            if (this.email === '') {
                this.errors.push('Insira o seu e-mail cadastrado')
            }
            if (!this.errors.length) {
                const formData = {
                    email: this.email
                }
                await axios
                    .post("/api/users/reset_password/", formData)
                    .then(response => {
                        toast({
                            message: 'Um e-mail foi enviado para o você com as instruções para alterar a senha',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        }) 
                        
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
            this.$store.commit('setIsLoading', false)
        }
    }

}
</script>
<style scoped>

@font-face {
    font-family: conforta;
    src: url('../assets/fonts/confortaa/Comfortaa-VariableFont_wght.ttf') format('truetype');
    src: local('conforta');
}
#page-resetpassword {
    font-family: conforta;
}
</style>