<template>
  <v-app>
    <v-main>

      <mark-app-bar/>
      <mark-content/>
      <mark-footer/>
     
    </v-main>
  </v-app>
</template>

<script>

import MarkFooter from "./components/Footer.vue"
import MarkContent from "./components/Content.vue"
import MarkAppBar from "./components/Header.vue"

export default {
  name: 'App',

  components: {
    MarkAppBar,
    MarkContent,
    MarkFooter
  },

  data: () => ({
    //
  }),
};
</script>
