<template>
  <div class="about">
    <h1>This is an about page {{ privet }}</h1>
    <router-link to="/" class="chicha">Home</router-link> 



<div class="tester">
  <form @submit.prevent>
    <input type="text" v-model="user.name" placeholder="name">
    <input type="text" v-model="user.pass">
  </form>

</div>

  </div>

  
</template>


<script>


export default{
  
  data(){
    return{
      privet: 'Привет, это круто!',
      user:{
        name:'',
        pass:'',
      }
    }
  },
  methods: {
    // createUser(){
    //   this.user.name:
    // }
  }

}

</script>


