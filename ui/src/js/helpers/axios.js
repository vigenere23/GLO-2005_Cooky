import axios from 'axios'
import { EventBus } from '@/js/eventbus'

async function parseErrors (request) {
  try {
    const response = await request()
    return response.data
  } catch (error) {
    const message = error.response.data.error
      ? error.response.data.error
      : error.response.data
    console.error(message)
    const status = error.reponse.status
    if (error.response.status === 404) {
      EventBus.$emit('toast', { type: 'error', message: 'Page not found' })
    } else if (status === 500) {
      EventBus.$emit('toast', { type: 'error', message: 'An unexpected error occured' })
    } else if (status === 401 || status === 403) {
      EventBus.$emit('toast', { type: 'error', message: "You don't have access to that page" })
      // TODO return to login page
    } else {
      EventBus.$emit('toast', { type: 'error', message })
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
