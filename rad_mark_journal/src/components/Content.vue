<template>
        <div style = "position : relative; top: 20px">
                <v-row justify = "center">
                        <v-col cols = "3" justify = "center">
                    <v-card>
                        <br>
                        <center>
                            <v-avatar color="#00ACC1" size = "65">
                            <v-icon dark>
                                mdi-account-circle
                            </v-icon>
                            </v-avatar>
                            <br><br>
                            <span>UserName</span><br>
                            <span>accound@mark.pi</span>
                        </center><br>
        
                        <center>
                            <v-btn align = "center" @click = "username()">
                                <span>Change UserName<v-icon>mdi-circle-edit-outline</v-icon></span>
                            </v-btn>
                        </center>

                        <div v-show = "show === 1"><br>
                            <v-card
                                class="mx-auto"
                                max-width="500"
                            >
                                <v-card-title class="title font-weight-regular justify-space-between">
                                <span>Change Username</span>
                                <v-icon>mdi-cached</v-icon>
                                </v-card-title>

                                <v-window>
                                <v-window-item :value="1">
                                    <v-card-text>
                                    <v-text-field
                                        label="New Username"
                                        placeholder="леша_пидорZavar"
                                    ></v-text-field>
                                    <span class="caption grey--text text--darken-1">
                                        This is input to enter your new UserName
                                    </span>
                                    </v-card-text>
                                </v-window-item>
                                </v-window>

                                <v-divider></v-divider>

                                <v-card-actions>
                                <v-spacer></v-spacer>
                                </v-card-actions>
                            </v-card>
                        </div>
                        
                            <br>

                            <center>
                                <v-btn align = "center" @click = "email()">
                                    <span>Change Email<v-icon>mdi-circle-edit-outline</v-icon></span>
                                </v-btn>
                            </center>

                            <br>

                        <div v-show = "show === 2">
                            <v-card
                                class="mx-auto"
                                max-width="500"
                            >
                                <v-card-title class="title font-weight-regular justify-space-between">
                                <span>Change Email</span>
                                <v-icon>mdi-cached</v-icon>
                                </v-card-title>

                                <v-window>
                                <v-window-item :value="1">
                                    <v-card-text>
                                    <v-text-field
                                        label="New Email"
                                        placeholder="new_email@hidbell.ru"
                                    ></v-text-field>
                                    <span class="caption grey--text text--darken-1">
                                        This is input to enter your new Email
                                    </span>
                                    </v-card-text>
                                </v-window-item>
                                </v-window>

                                <v-divider></v-divider>

                                <v-card-actions>
                                <v-spacer></v-spacer>
                                </v-card-actions>
                            </v-card>
                        </div>

                    </v-card>
                    </v-col>       
                </v-row>
        </div>
</template>

<script>
export default {
    data() {
        return {
            show : 0
        }
    },

    methods: {
        email() {
            if (this.show != 2) {
                this.show = 2;
            }
            else {
                this.show = 0;
            }
        },
        username() {
            if (this.show != 1) {
                this.show = 1;
            }
            else {
                this.show = 0;
            }
        }
    }
  }
</script>