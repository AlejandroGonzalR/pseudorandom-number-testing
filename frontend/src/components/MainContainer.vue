<template>
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
        <div class="file has-name is-boxed">
          <label class="file-label">
            <input class="file-input" type="file" name="resume">
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                Escoge tus datos!
              </span>
            </span>
            <span class="file-name">
              {{ this.filename || 'Aun no has seleccionado nada' }}
            </span>
          </label>
        </div>
        <div class="control">
          <label v-for="(test, index) in testOptions" :key="index" class="radio">
            <input :id="test" :value="test" type="radio" v-model="optionSelected">
            {{ test }}
          </label>
        </div>
        <button class="button is-primary is-light">Cargar</button>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: 'MainContainer',
  data: () => {
    return {
      filename: null,
      testOptions: [
          'Chi 2',
          'Poker',
          'paloma',
          'abbie'
      ],
      optionSelected: null,
    }
  }
}
</script>

<style scoped>

</style>
