<template>
    <div id="activate">
    <form @submit.prevent="submitForm">
        <label class="has-text-centered title has-text-white">Insira uma nova senha para atualizar o cadastro</label>
      <br>
        <div class="field">
                        <label class=" has-text-white">Senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password1">
                        </div>
                    </div>
                    <div class="field">
                        <label class=" has-text-white">Repita a senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>
      <div class="field">
          <div class="control">
              <button class="button is-dark">Redefina</button>
          </div>
      </div>
               
      </form>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
    export default {
        name: 'SignupActivate',
        data() {
            return {
                errors: [],
                password1: '',
                password2: '',
                uid: '',
                token: '',
            }
        },
        mounted() {
         
        this.uid = this.$route.params.uidb64
        this.token = this.$route.params.token
          
        },
        
        methods: {
        submitForm() {
            //axios.defaults.xsrfHeaderName = 'x-csrftoken'
            //axios.defaults.xsrfCookieName = 'csrftoken'
            //axios.defaults.withCredentials = true  
              
                const formData = {
                   "uid": this.uid,
                   "token": this.token,
                   "new_password": this.password1,
                   "re_new_password": this.password2
                }
            axios
                .post("/api/users/reset_password_confirm/", formData, { headers: {'X-CSRFToken': this.CSRFtoken} })
                .then(response => {
                    toast ({
                        message: 'Tudo pronto! Pode fazer o Login',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/login')
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


    
</script>
<style scoped>
#activate {
    margin-top: 7vh;
    height: 100vh;
}
</style>