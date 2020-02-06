<template>
<div class="container">
    <br/>
    <button class="btn btn-primary logout" @click.prevent="logout">Log out</button>
    <div class="py-5 text-center">
        <img class="d-block mx-auto mb-4" src="/docs/4.4/assets/brand/bootstrap-solid.svg" alt="" width="72"
            height="72">
        <h2>Print form</h2>
        <p class="lead">Fill out the form below and click the Print button.</p>
    </div>

    <div class="row">
        <div class="col-md-12 order-md-1 justify-content-md-center">
            <form enctype="multipart/form-data" class="needs-validation" method="post">
                <div class="row justify-content-md-center">
                    <div class="col-md-6 mb-3">
                        <label class="form-control-label">Print Job Name</label>
                        <input type="text" class="form-control" name="jobName" placeholder="Enter a name for your job"
                          required="required" v-model="jobName">
                    </div>
                </div>

                <div class="row justify-content-md-center">
                    <div class="col-md-6 mb-3">
                        <label for="quantity">Number of Copies</label>
                        <div class="custom-file">
                            <input v-model="numberOfCopies" type="number" class="form-control" id="quantity">
                        </div>
                    </div>
                </div>

                <div class="row justify-content-md-center">
                    <div class="col-md-6 mb-3">
                        <div class="form-group mt-3">
                            <label class="mr-2">Upload your file:</label>
                            <b-form-file
                                v-model="file"
                                :state="Boolean(file)"
                                placeholder="Choose a file or drop it here..."
                                drop-placeholder="Drop file here..."
                                ></b-form-file>
                            <div class="mt-3">
                                Selected file: {{ file ? file.name : '' }}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-md-center">
                    <div class="col-md-6 mb-3">
                        <hr class="mb-4">
                        <button class="btn btn-primary btn-lg btn-block" type="submit" @click.prevent="sendToPrinter">Print</button>
                        <hr class="mb-4">
                    </div>
                </div>

            </form>
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios"
import router from "@/router/router";

export default {
  name: 'LoginPage',
  props: {
    msg: String
  },
  data() {
    return {
      jobName: "",
      numberOfCopies: 1,
      file: null
    };
  },
  methods: {
      sendToPrinter: function() {
        let formData = new FormData();
        formData.append('file', this.file);
        formData.append('name', this.jobName);
        formData.append('number', this.numberOfCopies);
        console.log('>> formData >> ', formData);
        axios
        .post(`${process.env.VUE_APP_API_URL}/print`, 
            formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
        )
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        });
        return

      },
      logout: function() {
        this.$store
        .dispatch("logout")
        .then(() => {
            router.push({name:"login"})
            console.log()
        })
        .catch(err => {
            console.log(err)
        });
      }
  } 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app {
    background: #fff;
}
.logout {
    float: right;
}
</style>
