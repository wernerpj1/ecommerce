<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.nome }}</router-link></td>
        <td>${{ item.valorTotal }}</td>
        <td>
            
            <button class="button is-small is-danger is-outlined" @click="decrementQuantity(item)">-</button>
            {{ item.quantity }}
            <button class="button is-small is-success is-outlined" @click="incrementQuantity(item)">+</button>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object,
        
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.valorTotal
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>