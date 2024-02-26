<template>
  <div>

    <p>{{ a.count }}</p>
    <p>{{ a.upper }}</p>
    <button @click="fetch_results">
      Clicker

      <div v-show7="count">
        <li v-for="number in 20" :key="number">{{ a.count }}</li>
      </div>
    </button>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive } from "vue"
import AxiosU from '../configs/apisender'
const a = reactive({ count: null, upper: false })

function fetch_results(){
  AxiosU
  .get('/user/test')
  .then(response => (a.count = response.data))
  .catch(error => console.log(error));
}

console.log(12)



</script>


<style scopped>
  li{
    width: 50%;
    height: 30px;
    background-color: rgb(186, 186, 186);
    border: 1px solid gray;
  }
</style>