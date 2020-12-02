<template>
  <section>
    <div class="is-flex is-justify-content-center">
      <article id="header" class="panel is-primary has-text-centered my-6">
        <p class="panel-heading">
          Pruebas de numeros Pseudo-aleatorios
        </p>
        <div class="panel-block is-flex is-flex-direction-column">
          <h2>
            Selecciona un archivo en formato <kbd>.txt</kbd>,
            escoge un tipo de <strong>prueba</strong> y da click en cargar!
          </h2>
          <div class="file is-boxed">
            <label class="file-label">
              <input class="file-input" type="file" name="data" @change="fileSelected">
              <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                {{ this.filename || 'Escoge tus datos!' }}
              </span>
            </span>
            </label>
          </div>
          <div class="control">
            <label v-for="(test, index) in testOptions" :key="index" class="radio">
              <input :id="test" :value="test" type="radio" v-model="selectedTest">
              {{ test }}
            </label>
          </div>
          <button class="button is-primary is-light" @click="sendData" :disabled="!dataFile || !selectedTest">
            Cargar
          </button>
        </div>
      </article>
    </div>

    <div class="m-6">
      <div class="tile is-ancestor">
        <div class="tile">
          Data table
        </div>
        <div class="tile">
          Procedure
        </div>
      </div>
    </div>

  </section>

</template>

<script>
import axios from 'axios';

const SERVICE_URL = 'http://localhost:5000/testing'

export default {
  name: 'MainContainer',
  data: () => {
    return {
      testOptions: [
        'Chi 2',
        'Poker',
        'paloma',
        'abbie'
      ],
      selectedTest: null,
      dataFile: null,
      filename: '',
    }
  },
  methods: {
    fileSelected(event) {
      this.dataFile = event.target.files || event.dataTransfer.files;
      this.filename = this.dataFile[0].name;
    },
    sendData() {
      let formData = new FormData();
      formData.append('file', this.dataFile[0]);
      formData.append('test', this.selectedTest);
      axios
          .post(SERVICE_URL, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            console.error(error);
          });
    }
  }
}
</script>

<style scoped>

</style>
