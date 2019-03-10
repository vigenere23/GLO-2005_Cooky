export const NavItems = [
  {
    type: 'divider',
    text: 'explore'
  },
  {
    type: 'item',
    text: 'Explore recipes',
    icon: 'restaurant_menu',
    link: '/recipes',
    current: true
  },
  {
    type: 'item',
    text: 'Find ingredients',
    icon: 'spa',
    link: '/ingredients'
  },
  {
    type: 'divider',
    text: 'user'
  },
  {
    type: 'item',
    text: 'My recipes',
    icon: 'book',
    link: '/users'
  },
  {
    type: 'item',
    text: 'Liked recipes',
    icon: 'favorite',
    link: '/users'
  },
  {
    type: 'item',
    text: 'Shopping cart',
    icon: 'shopping_cart',
    link: '/cart'
  },
  {
    type: 'divider',
    text: 'account'
  },
  {
    type: 'item',
    text: 'Profile',
    icon: 'person',
    link: '/users'
  },
  {
    type: 'item',
    text: 'Settings',
    icon: 'settings',
    link: '/users'
  },
  {
    type: 'item',
    text: 'Logout',
    icon: 'exit_to_app',
    link: '/logout'
  }
]
