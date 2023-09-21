<template>
<div class="menu">
    <nav>
    <router-link to="/">Board</router-link> | 
    <router-link to="/week">Week</router-link> | 
    <router-link to="/role">Role</router-link>
  </nav>
  <router-view/>
  <div>
    Hello!
  </div>
</div>
    
</template>

<script>

export default{
    name:'MenuComp'
}
</script>