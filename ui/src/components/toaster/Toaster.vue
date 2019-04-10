<template>
  <div id="toaster">
    <Toast
      v-for="(toast, i) in toasts"
      :key="toast.id"
      @delete="removeToast(i)"
      :type="toast.type"
      :message="toast.message"
    />
  </div>
</template>

<script>
import Toast from '@/components/toaster/Toast'
import { EventBus } from '@/js/eventbus'
import uuid from 'uuid/v4'

export default {
  name: 'Toaster',
  components: {
    Toast
  },
  data () {
    return {
      toasts: []
    }
  },
  created () {
    EventBus.$on('toast', this.addToast)
  },
  destroyed () {
    EventBus.$off('toast', this.addToast)
  },
  methods: {
    addToast (toast) {
      toast.id = uuid()
      this.toasts.push(toast)
      if (this.toasts.length > 3) {
        this.removeToast(0)
      }
    },
    removeToast (i) {
      this.toasts.splice(i, 1)
    }
  }
}
</script>

<style>
#toaster {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  max-width: 480px;
  margin: auto;
  padding: 0 8px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  z-index: 99;
}
</style>
