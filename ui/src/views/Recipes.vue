<template>
  <div class="recipes-page">
    <h1>Explore recipes</h1>
    <SearchBar />
    <GridList
      :items="recipes"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import GridList from '@/components/lists/GridList'

export default {

  name: 'Recipes',

  components: {
    SearchBar,
    GridList
  },

  data () {
    return {
      recipes: [
        {
          title: 'Fruity smoothie bowl',
          description: 'Wake up energic and be ready for the day. This smoothie will get you everything you need to be productive, bright and perseverant during the entire day.',
          image: 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg'
        },
        {
          title: 'Greek vegetarian burger',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://midwestfoodieblog.com/wp-content/uploads/2019/01/FINAL-greek-burger-1-4.jpg'
        },
        {
          title: 'Spicy thai salmon poke bowl',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.heartfoundation.org.au//images/made/images/uploads/recipes/Poke_Bowl_Image_3_1200_630_85_s_c1.jpg'
        },
        {
          title: 'Butternut squash soup à la Indian',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/recipe-image-legacy-id-1074500_11.jpg'
        },
        {
          title: 'Fruity smoothie bowl',
          description: 'Wake up energic and be ready for the day. This smoothie will get you everything you need to be productive, bright and perseverant during the entire day.',
          image: 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg'
        },
        {
          title: 'Greek vegetarian burger',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://midwestfoodieblog.com/wp-content/uploads/2019/01/FINAL-greek-burger-1-4.jpg'
        },
        {
          title: 'Spicy thai salmon poke bowl',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.heartfoundation.org.au//images/made/images/uploads/recipes/Poke_Bowl_Image_3_1200_630_85_s_c1.jpg'
        },
        {
          title: 'Butternut squash soup à la Indian',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/recipe-image-legacy-id-1074500_11.jpg'
        },
        {
          title: 'Fruity smoothie bowl',
          description: 'Wake up energic and be ready for the day. This smoothie will get you everything you need to be productive, bright and perseverant during the entire day.',
          image: 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg'
        },
        {
          title: 'Greek vegetarian burger',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://midwestfoodieblog.com/wp-content/uploads/2019/01/FINAL-greek-burger-1-4.jpg'
        },
        {
          title: 'Spicy thai salmon poke bowl',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.heartfoundation.org.au//images/made/images/uploads/recipes/Poke_Bowl_Image_3_1200_630_85_s_c1.jpg'
        },
        {
          title: 'Butternut squash soup à la Indian',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/recipe-image-legacy-id-1074500_11.jpg'
        },
        {
          title: 'Fruity smoothie bowl',
          description: 'Wake up energic and be ready for the day. This smoothie will get you everything you need to be productive, bright and perseverant during the entire day.',
          image: 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg'
        },
        {
          title: 'Greek vegetarian burger',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://midwestfoodieblog.com/wp-content/uploads/2019/01/FINAL-greek-burger-1-4.jpg'
        },
        {
          title: 'Spicy thai salmon poke bowl',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.heartfoundation.org.au//images/made/images/uploads/recipes/Poke_Bowl_Image_3_1200_630_85_s_c1.jpg'
        },
        {
          title: 'Butternut squash soup à la Indian',
          description: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.',
          image: 'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/recipe-image-legacy-id-1074500_11.jpg'
        }
      ]
    }
  }

}
</script>
