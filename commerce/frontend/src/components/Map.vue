<template>

    <div>
    <h2 class="title has-text-centered has-text-white">Localização</h2>
    <div class="columns is-multiline">
        <iframe class="mapFrame" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3603.218765865701!2d-49.27850988498577!3d-25.430948683787975!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94dce40d1efac67f%3A0x49e3007f924137af!2sR.%20Cruz%20Machado%2C%20385%20-%20Centro%2C%20Curitiba%20-%20PR%2C%2080410-170!5e0!3m2!1spt-BR!2sbr!4v1630105844580!5m2!1spt-BR!2sbr" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
    </div>
    </div>
</template>
<script>

export default {
   name: 'Map' 
}
</script>
<style scoped>
    .columns.is-multiline {
        width: 90vw;
        box-shadow: 0 0 1em rgb(78, 78, 77);
        height: 100vh;
    }
    .mapFrame {
        position: relative;
        min-height: 100%;
    }
</style>