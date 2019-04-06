### return all users
`GET /users`

### return user by id
`GET /users/<id>`

### return all recipes from user id
`GET /users/<id>/recipes`

### return liked recipes from user id
`GET /users/<id>/likes`

### return profile from user id
`GET /users/<id>/profile`

### return all cart from user id
`GET /users/<id>/cart`

### return all recipes
`GET /recipes`

### return recipe from recipe id
`GET /recipes/<id>`

### return all ingredients from recipe id
`GET /recipes/<id>/ingredients`

### return all ingredients
`GET /ingredients`

### return ingredient by name
`GET /ingredients/<name>`

### return all carts
`GET /cart`

### return cart items from the cart id
`GET /cart/<id>/cartItems`

### return the command from the cart id
`GET /cart/<id>/command`

### return the new userId and userName if created
### body : {username: <username>}
`Post /users`

### return new cartItem
### body : {
###   id_Ingredient: <id_Ingredient>,
###   subCost: <subCost>
###}
### Note : always add one item and add to current Cart
`Post /cart/<id>/cartItems`

### return new likeRecipe
### body : {
###   id_User: <id_User>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/like`

### return new ratingRecipe
### body : {
###   id_User: <id_User>,
###   value: <value>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/rate`

### return new comment
### body : {
###   id_User: <id_User>,
###   text: <text>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/comment`

### return new recipe
### body : {
###   id_User: <id_User>,
###   name: <name>,
###   directives: <directives>
###}
`Post /recipes`
