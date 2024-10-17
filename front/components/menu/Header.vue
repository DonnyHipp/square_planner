<template>
  <header>


      <nav>
        <div class="menu">
          <div>
            <NuxtLink to="/">Логотип</NuxtLink>
          </div>
          <div v-for="link in links" :key="link.text">
            <NuxtLink exact active-class="active-btn" class="button" :to="link.url">{{ link.text }}</NuxtLink>
          </div>
        </div>

      </nav>

  </header>
</template>


<style scoped lang="scss">
header {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100px;

  nav {
    display: flex;
    align-items: center;
    justify-content: center;

    .menu {
      box-shadow:$box-shadow;
      padding-left: 15px;
      padding-right: 15px;
      padding-top: 15px;
      padding-bottom: 15px;
      border-radius: $border-radius;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      gap: 5px;

      > div {
        white-space: nowrap; // Это предотвратит перенос текста на новую строку
      }
    }
  }
}
</style>


<script>

export default {
  setup() {
    const links = ref([
      { text: 'Задачи', url: '/tasks' },
      { text: 'Календарь', url: '/calendar' },
      { text: 'Цели', url: '/aims' },
      { text: 'Квадрат', url: '/square' }
    ]);

    return {
      links
    };
  }
}
</script>