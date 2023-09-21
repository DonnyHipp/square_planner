<template>
  <div class="app">
    <MenuComp/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <router-view/>
  </div>
  
</template>

<script>
import MenuComp from '@/components/Head/MenuComp.vue'
import HelloWorld from '@/components/HelloWorld.vue'


export default{
  components: MenuComp, HelloWorld
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
