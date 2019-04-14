<template>
  <div class="data-table-wrapper">
    <table
      v-if="items.length"
      class="data-table"
      :class="{ small }"
    >
      <thead>
        <tr>
          <th v-if="actions" />
          <th
            v-for="(column, i) in columns"
            :key="i"
            :class="{ first: i === 0 }"
          >
            <span
              class="column-text"
              :class="{ sortable: column.sortable, sorting: isCurrentSorting(column) }"
              @mousedown="updateSorting(column)"
            >
              {{ column.text }}
              <i
                class="material-icons sorting-arrow"
                :class="{ reverse: reverseSorting }"
              >arrow_upward</i>
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, i) in sortedItems"
          :key="item.id || i"
        >
          <td
            v-if="actions"
            class="action"
          >
            <SelectionIcon
              :is-selected="actions.isSelected(item)"
              @selection="actions.onSelection(item)"
              @deselection="actions.onDeselection(item)"
            />
          </td>
          <td
            v-for="(column, j) in columns"
            :key="j"
            :class="{ first: j === 0 }"
          >
            <template v-if="column.parser && column.parser(item[column.name]) !== null && column.parser(item[column.name]) !== undefined">
              {{ column.parser(item[column.name]) }}
            </template>
            <template v-else-if="item[column.name] !== null && item[column.name] !== undefined">
              {{ item[column.name] }}
            </template>
          </td>
        </tr>
      </tbody>
    </table>
    <NoContent v-else />
  </div>
</template>

<script>
import SelectionIcon from '@/components/SelectionIcon'
import NoContent from '@/components/NoContent'

export default {

  name: 'DataTable',

  components: {
    SelectionIcon,
    NoContent
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
    },
    actions: {
      type: Object,
      default: null
    }
  },

  computed: {
    sortedItems () {
      if (this.currentSorting) {
        const sortedItems = this.items
        if (this.currentSorting.comparator) {
          sortedItems.sort((a, b) => this.currentSorting.comparator(a[this.currentSorting.name], b[this.currentSorting.name]))
        } else {
          sortedItems.sort((a, b) => {
            return a[this.currentSorting.name] > b[this.currentSorting.name]
          })
        }

        if (this.reverseSorting) {
          sortedItems.reverse()
        }
        return sortedItems
      } else {
        return this.items
      }
    }
  },

  data () {
    return {
      currentSorting: null,
      reverseSorting: null
    }
  },

  mounted () {
    this.currentSorting = this.columns.find(col => col.initiallySorted)
    if (this.currentSorting) {
      this.reverseSorting = this.currentSorting.defaultSorting === 'desc'
    }
  },

  methods: {
    isCurrentSorting (column) {
      return column.sortable && this.currentSorting && this.currentSorting.name === column.name
    },
    updateSorting (column) {
      if (column.sortable) {
        if (column.name === this.currentSorting.name) {
          this.reverseSorting = !this.reverseSorting
        } else {
          this.currentSorting = column
          this.reverseSorting = this.currentSorting.defaultSorting === 'desc'
        }
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

  th .column-text {
    color: $secondary-text-color;
    font-weight: 500;
    font-size: 13.5px;

    &:not(.sorting) .sorting-arrow {
      display: none;
    }

    &.sortable {
      cursor: pointer;
    }

    &.sorting {
      color: $primary-color;
    }

    .sorting-arrow {
      font-size: 18px;
      padding-left: 2px;
      vertical-align: bottom;
      transition: transform 0.1s ease-in-out;

      &.reverse {
        transform: rotate(180deg);
      }
    }
  }

  td, th {
    text-align: center;
    vertical-align: middle;
    line-height: 1.4em;
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
    color: $primary-color;
  }
}
</style>
