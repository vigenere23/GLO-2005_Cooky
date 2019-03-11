export const NavItems = [
  {
    name: 'explore',
    items: [
      {
        text: 'Explore recipes',
        icon: 'restaurant_menu',
        link: () => '/recipes',
        current: true
      },
      {
        text: 'Find ingredients',
        icon: 'spa',
        link: () => '/ingredients'
      }
    ]
  },
  {
    name: 'personal',
    items: [
      {
        text: 'Recipe book',
        icon: 'book',
        link: (userId) => `/users/${userId}/recipes`
      },
      {
        text: 'Liked recipes',
        icon: 'favorite',
        link: (userId) => `/users/${userId}/likes`
      },
      {
        text: 'Shopping cart',
        icon: 'shopping_cart',
        link: () => '/cart'
      },
      {
        text: 'Commands',
        icon: 'receipt',
        link: () => '/commands'
      }
    ]
  },
  {
    name: 'account',
    items: [
      {
        text: 'Profile',
        icon: 'person',
        link: (userId) => `/users/${userId}`
      },
      {
        text: 'Settings',
        icon: 'settings',
        link: () => '/settings'
      },
      {
        text: 'Logout',
        icon: 'exit_to_app',
        link: () => '/logout'
      }
    ]
  }
]
