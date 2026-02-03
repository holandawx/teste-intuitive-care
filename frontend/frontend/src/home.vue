<template>
  <div style="padding:20px">
    <h1>Operadoras</h1>

    <input 
      v-model="busca" 
      placeholder="Buscar por CNPJ ou Razão Social"
      style="margin-bottom:10px"
    />

    <table border="1" width="100%">
      <tr>
        <th>CNPJ</th>
        <th>Razão Social</th>
        <th>UF</th>
        <th>Modalidade</th>
      </tr>

      <tr v-for="op in operadoras" :key="op.cnpj">
        <td>
          <router-link :to="`/operadora/${op.cnpj}`">
            {{ op.cnpj }}
          </router-link>
        </td>
        <td>{{ op.razao_social }}</td>
        <td>{{ op.uf }}</td>
        <td>{{ op.modalidade }}</td>
      </tr>
    </table>

    <br/>

    <button @click="prev">Anterior</button>
    <button @click="next">Próximo</button>

    <h2>Distribuição de despesas por UF</h2>
    <canvas id="grafico"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Chart from 'chart.js/auto'

const operadoras = ref([])
const page = ref(1)
const busca = ref("")

async function carregar() {
  const res = await axios.get(
    `https://humble-guide-v64r5xvjp77gfw7gx-8000.app.github.dev/api/estatisticas`
  )
  operadoras.value = res.data.data
}

async function carregarGrafico() {
  const res = await axios.get('https://humble-guide-v64r5xvjp77gfw7gx-8000.app.github.dev/api/operadoras')

  const labels = res.data.por_uf.map(i => i.uf)
  const valores = res.data.por_uf.map(i => i.total)

  new Chart(document.getElementById('grafico'), {
    type: 'bar',
    data: {
      labels,
      datasets: [{ data: valores }]
    }
  })
}

function next() {
  page.value++
  carregar()
}

function prev() {
  if (page.value > 1) {
    page.value--
    carregar()
  }
}

onMounted(() => {
  carregar()
  carregarGrafico()
})
</script>
