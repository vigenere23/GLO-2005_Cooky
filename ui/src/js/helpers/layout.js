import { constants } from '@/js/helpers/constants'

export class LayoutHelper {
  static isSmallScreen () {
    return window.innerWidth <= constants.tabletWidth
  }
}
