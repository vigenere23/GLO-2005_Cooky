<template>
  <table
    class="data-table"
    :class="{ small }"
  >
    <thead>
      <tr>
        <th v-if="actionIcon" />
        <th
          v-for="(column, i) in columns"
          :key="i"
          :class="{ first: i === 0 }"
        >
          <span
            :class="{ sortable: column.sortable }"
            @mousedown="updateSorting(column)"
          >
            {{ column.text }}
            <i
              v-if="showSortingArrow(column)"
              class="material-icons sorting-arrow"
              :class="{ ascending: ascendingSorting }"
            >arrow_downward</i>
          </span>
        </th>
      </tr>
    </thead>
    <tbody v-if="items.length">
      <tr
        v-for="(item, i) in items"
        :key="item.id || i"
      >
        <td
          v-if="actionIcon"
          class="action"
        >
          <a class="material-icons">
            {{ actionIcon }}
          </a>
        </td>
        <td
          v-for="(column, j) in columns"
          :key="j"
          :class="{ first: j === 0 }"
        >
          <template v-if="item[column.name]">
            {{ item[column.name] }}
          </template>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {

  name: 'DataTable',

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
    },
    actionIcon: {
      type: String,
      default: ''
    }
  },

  data () {
    return {
      currentSorting: null,
      ascendingSorting: null
    }
  },

  mounted () {
    this.currentSorting = this.columns.find(col => col.defaultSorting)
    if (this.currentSorting) {
      this.ascendingSorting = this.currentSorting.defaultSorting !== 'desc'
      this.sortItems()
    }
  },

  methods: {
    showSortingArrow (column) {
      return column.sortable && this.currentSorting && this.currentSorting.name === column.name
    },
    updateSorting (column) {
      if (column.sortable) {
        if (column.name === this.currentSorting.name) {
          this.ascendingSorting = !this.ascendingSorting
        } else {
          this.currentSorting = column
          this.ascendingSorting = false
        }

        this.sortItems()
      }
    },
    sortItems () {
      if (this.currentSorting.comparator) {
        this.items.sort((a, b) => this.currentSorting.comparator(a[this.currentSorting.name], b[this.currentSorting.name]))
      } else {
        this.items.sort((a, b) => {
          return a[this.currentSorting.name] < b[this.currentSorting.name]
        })
      }

      if (this.ascendingSorting) {
        this.items.reverse()
      }
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.data-table {
  width: 100%;
  max-width: 720px;
  margin: 16px auto;
  background-color: white;
  font-size: 14.5px;
  border-radius: 4px;
  border-collapse: collapse;
  border: $faded-border;
  @include mdElevation(2);

  &.small {
    max-width: 360px;
    margin-left: initial;
    margin-right: initial;
  }

  thead tr, tbody tr:not(:last-child) {
    border-bottom: $faded-border;
  }

  thead tr {
    border-width: 2px;
  }

  th {
    color: $secondary-text-color;
    font-weight: 500;
    font-size: 13.5px;

    .sorting-arrow {
      font-size: 18px;
      padding-left: 2px;
      vertical-align: bottom;
      transition: transform 0.1s ease-in-out;

      &.ascending {
        transform: rotate(-180deg);
      }
    }

    span.sortable {
      cursor: pointer;
    }
  }

  td, th {
    text-align: center;
    vertical-align: center;
    padding: 12px 0 12px 16px;

    &.first {
      text-align: left;
      padding-left: 16px;
    }

    &:last-child {
      text-align: right;
      padding-right: 16px;
    }
  }

  .action {
    text-align: left;
    width: 32px;
    color: $secondary-text-color;
  }
}
</style>
