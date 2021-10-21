<template>
  <div id="myCarousel" class="carousel container slide">
<div class="carousel-inner">
        <div class="active item one"></div>
        <div class="item two"></div>
        <div class="item three"></div>
</div>
</div>
</template>
<script>
export default {
  name: "Slider",
  data() {
    return {
      
    }
  },

  mounted() {
    $(document).ready(function() {
    $('.carousel').carousel({interval: 7000});
  });
  },

  methods: {
    
  },

  computed: {
    
  },
}
</script>
<style scoped>
.carousel { z-index: -99; } /* keeps this behind all content */
.carousel .item {
    position: fixed; 
    width: 100%; height: 100%;
    -webkit-transition: opacity 1s;
    -moz-transition: opacity 1s;
    -ms-transition: opacity 1s;
    -o-transition: opacity 1s;
    transition: opacity 1s;

}
.carousel .one {
    background: url('../../assets/carrousel/carousel1.jpg');
    background-size: cover;
    -moz-background-size: cover;
}
.carousel .two {
    background: url('../../assets/carrousel/carousel2.png');
    background-size: cover;
    -moz-background-size: cover;
}
.carousel .three {
    background: url('../../assets/carrousel/carousel3.png');
    background-size: cover;
    -moz-background-size: cover;
}
.carousel .active.left {
    left:0;
    opacity:0;
    z-index:2;
}
</style>