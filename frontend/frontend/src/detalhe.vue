<template>
  <div style="padding:20px">
    <h1>{{ operadora.razao_social }}</h1>

    <p><b>CNPJ:</b> {{ operadora.cnpj }}</p>
    <p><b>UF:</b> {{ operadora.uf }}</p>
    <p><b>Modalidade:</b> {{ operadora.modalidade }}</p>

    <h2>Histórico de Despesas</h2>

    <ul>
      <li v-for="d in despesas" :key="d.data">
        {{ d.data }} - R$ {{ d.valor }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()
const cnpj = route.params.cnpj

const operadora = ref({})
const despesas = ref([])

onMounted(async () => {
  const op = await axios.get(
    `https://humble-guide-v64r5xvjp77gfw7gx-8000.app.github.dev/`
  )
  operadora.value = op.data

  const d = await axios.get(
    ``https://humble-guide-v64r5xvjp77gfw7gx-8000.app.github.dev/
  )
  despesas.value = d.data
})
</script>
