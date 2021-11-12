<template>
  <div>
    <button @click= 'randomPick'>Pick</button>
    <p><img :src="imageSrc" alt=""></p>
  </div>
</template>

<script>
import _ from 'lodash'

import { mapState } from 'vuex'

export default {
  name: 'Random',
  data: function(){
    return{
      randomMovie: '',
      imageSrc: '',
      randomMovieSrc: ''
    }
  },
  
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  },  
  methods: {
    randomPick: function () {
      this.randomMovie= _.sampleSize(this.$store.state.movieCards, 1),
      this.randomMovieSrc= this.randomMovie[0].poster_path
      this.imageSrc= `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${this.randomMovieSrc}`
    },
  }
}
</script>

<style>

</style>