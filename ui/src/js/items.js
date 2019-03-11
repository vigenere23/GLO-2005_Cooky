export const NavItems = [
  {
    name: 'explore',
    items: [
      {
        text: 'Explore recipes',
        icon: 'restaurant_menu',
        link: '/recipes',
        current: true
      },
      {
        text: 'Find ingredients',
        icon: 'spa',
        link: '/ingredients'
      }
    ]
  },
  {
    name: 'personal',
    items: [
      {
        text: 'Recipe book',
        icon: 'book',
        link: '/users'
      },
      {
        text: 'Liked recipes',
        icon: 'favorite',
        link: '/users'
      },
      {
        text: 'Shopping cart',
        icon: 'shopping_cart',
        link: '/cart'
      },
      {
        text: 'Commands',
        icon: 'receipt',
        link: '/users'
      }
    ]
  },
  {
    name: 'account',
    items: [
      {
        text: 'Profile',
        icon: 'person',
        link: '/users'
      },
      {
        text: 'Settings',
        icon: 'settings',
        link: '/users'
      },
      {
        text: 'Logout',
        icon: 'exit_to_app',
        link: '/logout'
      }
    ]
  }
]
