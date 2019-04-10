<template>
  <DataTable
    :columns="columns"
    :items="items"
    :small="small"
    :actions="actions"
  />
</template>

<script>
import DataTable from '@/components/lists/DataTable'
import { mapGetters, mapMutations } from 'vuex'

export default {

  name: 'IngredientsDataTable',

  components: {
    DataTable
  },

  props: {
    columns: {
      type: Array,
      required: true
    },
    items: {
      type: Array,
      required: true
    },
    small: {
      type: Boolean,
      default: false
    }
  },

  computed: mapGetters('user', ['cartContains']),

  data () {
    return {
      actions: {
        isSelected: (item) => this.cartContains(item.id),
        onSelection: (item) => this.addCartItem(item.id),
        onDeselection: (item) => this.removeCartItem(item.id)
      }
    }
  },

  methods: mapMutations('user', ['addCartItem', 'removeCartItem'])

}
</script>
