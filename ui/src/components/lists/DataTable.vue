<template>
  <table class="data-table">
    <thead>
      <tr>
        <th
          v-for="(column, i) in columns"
          :key="i"
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
          v-for="(column, j) in columns"
          :key="j"
        >
          <template v-if="!j">
            <a class="material-icons action">add_circle</a>
          </template>
          <template v-else>
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
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.data-table {
  width: 100%;
  max-width: 720px;
  margin: 32px auto;
  background-color: white;
  border-radius: 4px;
  border-collapse: collapse;
  border: $faded-border;
  @include mdElevation(2);

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
    padding: 12px 16px 12px 0;

    &:first-child {
      width: 60px;
      padding-left: 16px;
    }

    &:first-child, &:nth-child(2) {
      text-align: left;
    }

    &:last-child {
      text-align: right;
    }
  }

  .action {
    color: $secondary-text-color;
  }
}
</style>

<!--
      Name       Quantity      Price
+    Orange       1 unit       0.85 $
-->
