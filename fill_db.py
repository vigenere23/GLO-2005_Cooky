import random
from app import db
import datetime
from app.routes.users.model import UserModel
from app.routes.users.dao import UserDao
from app.routes.ingredient.model import IngredientModel
from app.routes.ingredient.dao import IngredientDao
from app.routes.recipe.model import RecipeModel
from app.routes.recipe.dao import RecipeDao
from app.routes.recipeIngredient.dao import RecipeIngredientDao
from app.routes.recipeIngredient.model import RecipeIngredientModel
from app.routes.cart.model import CartModel
from app.routes.cart.dao import CartDao
from app.routes.rating.model import RatingModel
from app.routes.rating.dao import RatingDao
from app.routes.comment.model import CommentModel
from app.routes.comment.dao import CommentDao
from app.routes.likeRecipe.model import LikeRecipeModel
from app.routes.likeRecipe.dao import LikeRecipeDao
from app.routes.address.model import AddressModel
from app.routes.address.dao import AddressDao
from app.routes.account.model import AccountModel
from app.routes.account.dao import AccountDao
from app.routes.commands.model import CommandsModel
from app.routes.commands.dao import CommandsDao

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pulvinar pharetra bibendum. Ut eget risus nec risus finibus hendrerit in non tortor. Pellentesque maximus ligula et turpis faucibus cursus. Donec vel nunc metus. Quisque sagittis mattis dui vel varius. Aliquam iaculis interdum lacinia. Nam euismod lectus id maximus sodales. Nam id magna dictum, semper nisl vel, ornare ligula. Sed condimentum metus quis leo pharetra, quis semper urna aliquam. Fusce consectetur accumsan augue sit amet iaculis. Suspendisse volutpat urna vitae fermentum eleifend. Maecenas sapien leo, gravida vitae pellentesque quis, efficitur in erat. Maecenas elementum euismod hendrerit. Mauris sagittis massa a orci."
loremBio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
words = ["Hogym", "Celloggimbur", "Laglesgim", "Sylcyllis", "Morbir", "Limgem", "Silgimculnir", "Narmar", "Solgamberthi", "Cyllig", "Thalomorn", "Rluggum", "Ornbar", "Merhosyl", "Callisthunir", "Thaligber", "Limbarmar", "Lishalllumcal", "Berthe", "Hathulemhe", "Colmorhi", "Salthalegorn", "Birmircyl", "Bermor", "Morlag", "Barbirorn", "Burmir", "Humarhamur", "Leglam", "Hugimirn", "Berburthamur", "Lasloglum", "Gomlamthi", "Narmarborern", "Lomlos", "Urnlasho", "Hical", "Hisol", "Leshe", "Gumsalculsil", "Morcalsul", "Barlugha", "Salhu", "Celmorgember", "Byrhebyr", "Birhogim", "Helisloshi", "Syllas", "Gymcalhober", "Gimcullegirn", "Borlessil", "Thitha", "Cylcelnor", "Borbyrhulys", "Loglistha", "Silbartha", "Orncilbirgom", "Lasnormer", "Lumsolthalig", "Burlyscul", "Murgomhellhi", "Thatheluslag", "Lyshallluslam", "Mirborcil", "Nircalbur", "Barlugarn", "Gimcul", "Thulam", "Hecolha", "Ornmur", "Lamber", "Sulleshe", "Lomlember", "Loscal", "Calornthilog", "Limlesgam", "Thigomcul", "Laglyslomlis", "Erngomlig", "Gamlusmorcol", "Syllag", "Hothoirnlug", "Hesolmar", "Lugcul", "Thicolthu", "Narlescul", "Nirmersolurn", "Logcel", "Lasloglag", "Lessellamyrn", "Gymlys", "Thasal", "Silurnsellag", "Hallloslysbur", "Ligbir", "Burcylcel", "Narlisho" ,"Hosal","Liscal", "Sulbarmornar", "Tyfoxe", "Xusini", "Kidoxa", "Piphafy", "Chirra", "Rrobysu", "Jasu", "Quacy", "Laqui", "Nophe", "Mmyjyhe", "Quelli", "Jazo", "Mmichera", "Rroky", "Mmelli", "Girre", "Kibi", "Zafu", "Nowomi", "Dunummo", "Phasone", "Gipho", "Kyjado", "Senoze", "Gocahy", "Mmoha", "Mata", "Vupo", "Lochu", "Zeto", "Cycaci", "Llollace", "Cuphiwa", "Thexe", "Billu", "Matuko", "Rruxigu", "Bogu", "Vesi", "Wetu", "Jegi", "Gake", "Chullene", "Rruno", "Hyza", "Poru", "Nyxichi", "Fadylu", "Lajyse", "Phuxu", "Thehyko", "Quovavu", "Lleji", "Kynugy", "Mmyte", "Pakufa", "Sychecha", "Thine", "Sidemi", "Mmeka", "Jyfybo", "Mmuquoby", "Vuci", "Raci", "Zyhi", "Sujytho", "Cukemo", "Mixevo", "Thyxuwu", "Muphaba", "Pehide", "Thaserra", "Byjuwi", "Geka", "Zurruca", "Hymmy", "Thuju", "Rydu", "Jeduty", "Lluzali", "Rroce", "Sala", "Sipehu", "Pazasi", "Hagyga", "Nophy", "Rrammyca", "Kevygu", "Hellu", "Jimiru", "Llommiga", "Fasopy", "Navede", "Wireju", "Kotherru", "Cuphu", "Lloto", "Lledagy", "Syqua", "Zajerry", "Wipugo", "Sixare", "Gyka", "Bibowo", "Poje", "Mechiwi", "Juzuke", "Nyjige", "Zycu", "Govopy", "Nibo", "Tysy", "Viri", "Mmoxuby", "Boxemmi", "Xathe", "Mmocho", "Rycho", "Pijoly", "Mexo", "Thytha", "Gequo", "Rycypy", "Boquirri", "Zapu", "Gichu", "Rethu", "Gully", "Quoquafa", "Vozella", "Fibonu", "Dodyra", "Theky", "Sozawy", "Cehypy", "Rrotyhu", "Mowe", "Chusuny", "Pyru", "Dypu", "Juhuta", "Polo", "Phikotho", "Polymmo", "Hyse", "Suquajo", "Lletyjo", "Phata", "Fille", "Medy", "Cephellu", "Wogaha", "Quarrythy", "Mmanure", "Tumu", "Rothe", "Hapha", "Loxocho", "Coquawi", "Bonephe", "Suchu", "Mmiweso", "Mallyzy", "Wimma", "Rriwufi", "Nopho", "Pima", "Gyki"]
addr = ["St", "Ave", "Blvd", "Rd"]

def generateUsers():
  userDao = UserDao()
  for i in range(100):
    userModel = UserModel(
      username=words[i],
      bio=loremBio
    )
    userDao.save(userModel)

def generateIngredients():
  ingredientDao = IngredientDao()
  for i in range(100):
    ingredientModel = IngredientModel(
      id_IngredientType=random.randint(1, 13),
      id_QuantityUnit=random.randint(1, 13),
      name=words[i],
      baseCost=round(random.random() * 15, 2),
      baseQuantity=random.randint(1, 12)
    )
    ingredientDao.save(ingredientModel)

def generateRecipes():
  recipeDao = RecipeDao()

  for i in range(100):
    ingredients = []
    ingredient_ids = []
    for _ in range(random.randint(5, 10)):
      ingredient_id = random.randint(1, 100)
      while ingredient_id in ingredient_ids:
        ingredient_id = random.randint(1, 100)

      ingredient_ids.append(ingredient_id)
      recipeIngredientModel = RecipeIngredientModel(
        id_Ingredient=ingredient_id,
        id_QuantityUnit=random.randint(1,10), # TODO À CHANGER!
        totalQuantity=random.randint(1, 10)
      )
      ingredients.append(recipeIngredientModel)

    recipeModel = RecipeModel(
      id_User=random.randint(1, 100),
      name=words[i],
      directives=lorem,
      description=lorem
    )
    recipeDao.save(recipeModel, ingredients)

def generateCarts():
  cartDao = CartDao()
  for _ in range(100):
    cartModel = CartModel(
      id_User=random.randint(1, 100),
      totalCost=random.randint(20, 250)
    )
    cartDao.save(cartModel)

def generateRatings():
  ratingDao = RatingDao()
  for _ in range(100):
    ratingModel = RatingModel(
      id_Recipe=random.randint(1, 100),
      id_User=random.randint(1, 100),
      value=random.randint(0, 5)
    )
    ratingDao.save(ratingModel)

def generateComments():
  commentDao = CommentDao()
  for _ in range(100):
    commentModel = CommentModel(
      id_Recipe=random.randint(1, 100),
      id_User=random.randint(1, 100),
      text=lorem
    )
    commentDao.save(commentModel)

def generateLikes():
  likeRecipeDao = LikeRecipeDao()
  for _ in range(100):
    likeRecipeModel = LikeRecipeModel(
      id_Recipe=random.randint(1, 100),
      id_User=random.randint(1, 100)
    )
    likeRecipeDao.save(likeRecipeModel)

def generateAdresses():
  adressDao = AddressDao()
  for _ in range(100):
    apartment = None if (random.randint(1,4) % 2 == 0) else (random.randint(0, 1000))
    addressModel = AddressModel(
      number=random.randint(1, 99),
      apartment=apartment,
      street=random.choice(words) + " " + random.choice(addr),
      city=random.choice(words),
      country=random.choice(words)
    )
    adressDao.save(addressModel)

def generateAccounts():
    accountDao = AccountDao()
    for _ in range(100):
      lastName = random.choice(words)
      firstName = random.choice(words)
      accountModel = AccountModel(
        id_User=random.randint(1, 100),
        id_Address=random.randint(1, 100),
        firstName=firstName,
        lastName=lastName,
        email=firstName + "." + lastName + "@gmail.com",
        password=random.choice(words)+random.choice(words)+random.choice(words)
      )
      accountDao.save(accountModel)

def generateCommands():
  commandDao = CommandsDao()
  for _ in range(100):
    current_time = datetime.datetime.now()
    commandModel = CommandsModel(
      id_Cart=random.randint(1, 100),
      creationDate=current_time,
      arrivalDate=current_time
    )
    commandDao.save(commandModel)


if __name__ == "__main__":
  generateUsers()
  generateIngredients()
  generateRecipes()
  generateCarts()
  generateRatings()
  generateLikes()
  generateComments()
  generateAdresses()
  generateAccounts()
  generateCommands()
