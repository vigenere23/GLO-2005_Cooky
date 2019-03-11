import { constants } from '@/js/constants'

export class LayoutHelper {
  static isSmallScreen () {
    return window.innerWidth <= constants.tabletWidth
  }
}
