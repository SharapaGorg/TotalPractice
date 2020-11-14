<template>
    <div style = "position : fixed; bottom: 0px; width : 100%">
        <v-footer
            color="#00ACC1"
            padless
        >

            <v-row
            justify="center"
            no-gutters
            >
            <v-btn
                v-for="link in links"
                :key="link"
                color="white"
                text
                rounded
                class="my-2"
            >
                {{ link }}
            </v-btn>
            <v-col
                class="#00ACC1 lighten-2 py-4 text-center white--text"
                cols="12"
            >
                {{ new Date().getFullYear() }} — <strong>Radolyn</strong>
            </v-col>
            </v-row>
        </v-footer>
    </div>
</template>

<script>
  export default {
    data: () => ({
      links: [
          'GitHub',
          'Support',
          'Discord'
      ],
    }),
  }
</script>