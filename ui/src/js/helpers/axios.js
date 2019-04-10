import axios from 'axios'
import { EventBus } from '@/js/eventbus'

async function parseErrors (request) {
  try {
    const response = await request()
    return response.data
  } catch (error) {
    const message = error.response.status === 404
      ? 'Page not found'
      : error.response.data.error
        ? error.response.data.error
        : error.response.data
    console.error(message)
    EventBus.$emit('toast', { type: 'error', message })
    if (error.status === 401 || error.status === 403) {
      // return to login page
    }
    return null
  }
}

export class AxiosHelper {
  static axiosGet (url, options) {
    return parseErrors(() => axios.get(url, options))
  }

  static axiosPost (url, body, options) {
    return parseErrors(() => axios.post(url, body, options))
  }

  static axiosPut (url, body, options) {
    return parseErrors(() => axios.put(url, body, options))
  }

  static axiosDelete (url, options) {
    return parseErrors(() => axios.delete(url, options))
  }
}
