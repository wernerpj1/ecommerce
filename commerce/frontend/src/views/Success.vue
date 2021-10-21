<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Obrigado</h1>

                <p>Sua ordem será processda em 48h</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Compra feita - Máquinas Ferreira'
    },
}
</script>