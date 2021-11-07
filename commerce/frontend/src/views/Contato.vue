<template>
    <div class="page-category">

        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered has-text-white">Contato</h2>
                
            </div>
        </div>
<div class="columns is-multiline">
<div class="column is-half has-text-centered">
    <h2 class="title has-text-white has-text-centered">Assistência Técnica</h2>
    <p class="subtitle has-text-white is-5 has-text-centered">A Máquinas de Costura Ferreira conta com profissionais treinados e capacitados para garantir a melhor assistência técnicas aos clientes com segurança e qualidade.
Aqui você tem a garantia dos melhores serviços do mercado!</p>
<div class="box"  style="height: 500px">
    <iframe class="videoInst" src="https://www.youtube.com/embed/JnXGBPvdo_s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>
<div class="column"></div>
<div class="column is-5">
        
        <form @submit.prevent="submitForm" v-if="!$store.state.isAuthenticated">
        <div class="field" >
        <label class="label has-text-white">Email</label>
        <div class="control has-icons-left has-icons-right">
            <input  class="input is-danger has-text-grey" v-model="email" type="email" placeholder="Email de cadastro">
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
                    <label class="label has-text-white">Senha:</label>
                    <div class="control">
                        <input class="input" v-model="password" type="password" placeholder="Insira sua senha">
        </div>
        </div>
        <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
        <div class="control">
            <button class="button is-link">Entrar</button>
        </div>
        </form>
        <div class="field" v-if="$store.state.isAuthenticated">
        <label class="label has-text-white">Assunto</label>
        <div class="control">
            <div class="select" :class="orderService == '' ? 'is-danger':''">
            <select v-model="orderService">
                <option>Sugestões</option>
                <option>Assistência</option>
            </select>
            <p v-if="orderService===''" class="help is-danger ">Selecione o assunto</p>
            </div>
        </div>
        </div>
        <br>
        <form v-if="$store.state.isAuthenticated && orderService==='Assistência'" @submit.prevent="submitService">
            <div class="field">
            <label class="label has-text-white" >Endereço</label>
            <input type="text" class="input" v-model="address">
            </div>
            <div class="field">
            <label class="label has-text-white" >CEP</label>
            <input type="tel" class="input" v-model="zipcode">
            </div>
            <div class="field">
            <label class="label has-text-white" >Ponto de referência</label>
            <input type="tel" class="input" v-model="place">
            </div>
            <div class="field">
            <label class="label has-text-white" >Telefone</label>
            <input type="tel" class="input" v-model="phone">
            <label class="label has-text-white" >Modelo da máquina</label>
            <input type="text" class="input" v-model="product">
            </div>
            <div class="field" >
            <label class="label has-text-white">Mensagem</label>
            <div class="control">
                <textarea class="textarea" placeholder="Textarea" v-model="txService"></textarea>
            </div>
            </div>

            <div class="field is-grouped" >
            <div class="control">
                <button class="button is-link">Enviar</button>
            </div>
            <div class="control">
                <button class="button is-link is-light">Cancelar</button>
            </div>
            </div>
        </form>
        <form v-else-if="$store.state.isAuthenticated && orderService==='Sugestões'" @submit.prevent="submitSugestion">
            <div class="field" >
            <label class="label has-text-white">Mensagem</label>
            <div class="control">
                <textarea class="textarea" placeholder="Insira sua sugestão" v-model="txService"></textarea>
            </div>
            </div>

            <div class="field is-grouped" >
            <div class="control">
                <button class="button is-link">Enviar</button>
            </div>
            <div class="control">
                <button class="button is-link is-light">Cancelar</button>
            </div>
            </div>
        </form>
              
</div>

</div>           
            
            
        
        </div>
    
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Contato',
    data() {
        return {
            orderService: '',
            email: '',
            password: '',
            errors: [],
            address: '',
            zipcode: '',
            place: '',
            phone: '',
            txService: '',
            product: '',
            username: '',
            token: '',
        }
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      this.token = this.$store.state.token

      
    },
    mounted() {
        this.username = localStorage.username
        document.title = 'Contato - Máquinas Ferreira'

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
    },
        submitService() {
          
          const data = {
              'address': this.address,
              'zipcode': this.zipcode,
              'place': this.place,
              'phone': this.phone,
              'txService': this.txService,
              'product': this.product,
          }
          
               axios 
                .post('/api/assistencia/', data)
                .then(response => {
                    toast({
                        message: response.data + 'Ordem de serviço cadastrada com sucesso. Entraremos em contato em até 48h ',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 5000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                    toast({
                        message: 'Ops algo errado. Por favor tente novamente.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })   
             
        },
        submitSugestion() {
            const data = {
                'sugestao': this.txService,
            }
            axios 
                .post('/api/sugestao/', data)
                .then(response => {
                    toast({
                        message: response.data + 'Sugestão cadastrada com sucesso. Entraremos em contato em até 48h ',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 5000,
                        position: 'bottom-right',
                    })
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                    toast({
                        message: 'Ops algo errado. Por favor tente novamente.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })   
        }

}  
}

</script>
<style scoped>

.page-category {
    width: 95vw;
}
.videoInst {
    width: 100%;
    height: 100%;
}
.box {
    background-color: transparent;
}
</style>