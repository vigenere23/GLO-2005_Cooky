import axios from 'axios'

async function parseErrors (request) {
  try {
    const response = await request()
    return response.data
  } catch (err) {
    // TODO plug banner here
    // do something with response.error.data ({ error: 'message' })
    return null
  }
}

export class AxiosHelper {

  static axiosGet(url, options) {
    return parseErrors(() => axios.get(url, options))
  }

  static axiosPost(url, body, options) {
    return parseErrors(() => axios.post(url, body, options))
  }

  static axiosPut(url, body, options) {
    return parseErrors(() => axios.put(url, body, options))
  }

  static axiosDelete(url, options) {
    return parseErrors(() => axios.delete(url, body, options))
  }

}
