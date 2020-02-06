<template>
    <body class="login-body">
      <div class="signup-form">
          <form method="post" @submit="checkForm">
              <h1>315 Printer</h1>
              <div class="form-group">
                  <div class="col-xs-6">
                      <label class="form-control-label password-label">Password</label>
                      <input type="password" class="form-control" name="password" placeholder="password"
                          required="required" v-model="password">
                  </div>
                  <br/>
                  <button type="submit" class="btn btn-success btn-lg btn-block" @click.prevent="login">Register Now</button>
              </div>
          </form>
      </div>
    </body>
</template>

<script>
// import axios from "axios"
import router from "@/router/router";

export default {
  name: 'LoginPage',
  props: {
    msg: String
  },
  data() {
    return {
      password: "",
      info: ""
    };
  },
  methods: {
    login: function() {
        let password = this.password;
        this.$store
        .dispatch("login", { "creds": password })
        .then(() => {
            router.push({name:"print"})
            console.log()
        })
        .catch(err => {
            this.password = ''
            console.log(err)
        });
    },
     checkForm: function (e) {
      if (this.password) {
        return true;
      }
      this.errors = [];
      if (!this.password) {
        this.errors.push('Password required.');
      }
      e.preventDefault();
    }
  } 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#app {
    height: 100%;
}
.login-body {
    color: #fff;
    background-color: #4d94ff;
    font-family: 'Roboto', sans-serif;
}


.form-control:focus {
    border-color: #5cb85c;
}

.form-control,
.btn {
    border-radius: 3px;
}

.password-label {
    font-weight: bold;
}

.signup-form {
    width: 400px;
    margin: 0 auto;
    padding: 30px 0;
    box-shadow: inset;
}

.signup-form h1 {
    color: #636363;
    margin: 0 0 15px;
    position: relative;
    text-align: center;
}

.signup-form .hint-text {
    color: #999;
    margin-bottom: 30px;
    text-align: center;
}

.signup-form form {
    color: #999;
    border-radius: 3px;
    margin-bottom: 15px;
    background: #f2f3f7;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    padding: 30px;
}

.signup-form .form-group {
    margin-bottom: 20px;
}

.signup-form input[type="checkbox"] {
    margin-top: 3px;
}

.signup-form .btn {
    font-size: 16px;
    font-weight: bold;
    min-width: 140px;
    outline: none !important;
}

.signup-form .row div:first-child {
    padding-right: 10px;
}

.signup-form .row div:last-child {
    padding-left: 10px;
}

.signup-form a {
    color: #fff;
    text-decoration: underline;
}

.signup-form a:hover {
    text-decoration: none;
}

.signup-form form a {
    color: #5cb85c;
    text-decoration: none;
}

.signup-form form a:hover {
    text-decoration: underline;
}
</style>
