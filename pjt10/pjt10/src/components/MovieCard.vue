<template>
  <div>
    <h1>{{ movieCard.title }}</h1>
    <p><img :src="imageSrc" alt=""></p>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  },
  data: function(){
    return{
      imageSrc: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${this.movieCard.poster_path}`
    }
  },
}
</script>

<style>

</style>