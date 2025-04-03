<template>
  <div class="container">
    <h1>Busca de Operadoras ANS</h1>
    <input v-model="termo" @input="buscar" placeholder="Digite o nome da operadora" />

    <div v-if="resultado.length > 0">
      <ul>
        <li v-for="operadora in resultado" :key="operadora.registro_ans">
          <strong>{{ operadora.nome_fantasia }}</strong> - {{ operadora.uf }} ({{ operadora.modalidade }})
        </li>
      </ul>
    </div>

    <div v-else-if="termo.length > 2">
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const termo = ref("")
const resultado = ref([])

async function buscar() {
  if (termo.value.length < 3) {
    resultado.value = []
    return
  }

  const res = await fetch(`http://127.0.0.1:5000/buscar?q=${termo.value}`)
  resultado.value = await res.json()
}
</script>

<style>
.container {
  max-width: 600px;
  margin: 40px auto;
  font-family: sans-serif;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 20px;
}
li {
  margin-bottom: 10px;
}
</style>
