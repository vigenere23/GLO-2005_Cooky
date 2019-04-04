<template>
  <div class="commands-page">
    <h1>Commands</h1>
    <h2>Ongoing</h2>
    <DataTable
      :columns="ongoingColumns"
      :items="ongoingCommands"
      :default-sorted="{ name: 'created_on' }"
    />
    <h2>Completed</h2>
    <DataTable
      :columns="completedColumns"
      :items="completedCommands"
      :default-sorted="{ name: 'date' }"
    />
  </div>
</template>

<script>
import DataTable from '@/components/lists/DataTable'

export default {

  name: 'Commands',

  components: {
    DataTable
  },

  data () {
    return {
      ongoingColumns: [
        { name: 'created_on', text: 'Created on', sortable: true },
        { name: 'status', text: 'Status', sortable: true },
        { name: 'total', text: 'Total ($)', sortable: true }
      ],
      ongoingCommands: [
        {
          created_on: '02-04-2019',
          status: 'Shipped',
          total: 39.95
        },
        {
          created_on: '02-05-2019',
          status: 'Packing',
          total: 119.27
        }
      ],
      completedColumns: [
        { name: 'date', text: 'Date', sortable: true },
        { name: 'status', text: 'Status', sortable: true },
        { name: 'total', text: 'Total ($)', sortable: true }
      ],
      completedCommands: [
        {
          date: '02-04-2019',
          status: 'Received',
          total: 37.48
        },
        {
          date: '02-05-2019',
          status: 'Received',
          total: 75.64
        },
        {
          date: '02-04-2019',
          status: 'Received',
          total: 37.48
        },
        {
          date: '02-05-2019',
          status: 'Cancelled',
          total: 75.64
        },
        {
          date: '02-04-2019',
          status: 'Received',
          total: 37.48
        },
        {
          date: '02-05-2019',
          status: 'Received',
          total: 75.64
        },
        {
          date: '02-04-2019',
          status: 'Cancelled',
          total: 37.48
        },
        {
          date: '02-05-2019',
          status: 'Received',
          total: 75.64
        }
      ]
    }
  }

}
</script>
