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
          :class="{ first: i == 0 }"
        >
          {{ column.text }}
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
          :class="{ first: j == 0 }"
        >
          <template v-if="item[column.for]">
            {{ item[column.for] }}
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
  border-radius: 4px;
  border-collapse: collapse;
  border: $faded-border;
  @include mdElevation(2);

  &.small {
    width: auto;
    max-width: 320px;
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
  }

  td, th {
    text-align: center;
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
