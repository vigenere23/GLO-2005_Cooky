from random import *
from app import db
from app.routes.users.model import UserModel
from app.routes.users.dao import UserDao
from app.routes.ingredient.model import IngredientModel
from app.routes.ingredient.dao import IngredientDao
from app.routes.recipe.model import RecipeModel
from app.routes.recipe.dao import RecipeDao
from app.routes.cart.model import CartModel
from app.routes.cart.dao import CartDao
from app.routes.rating.model import RatingModel
from app.routes.rating.dao import RatingDao

lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pulvinar pharetra bibendum. Ut eget risus nec risus finibus hendrerit in non tortor. Pellentesque maximus ligula et turpis faucibus cursus. Donec vel nunc metus. Quisque sagittis mattis dui vel varius. Aliquam iaculis interdum lacinia. Nam euismod lectus id maximus sodales. Nam id magna dictum, semper nisl vel, ornare ligula. Sed condimentum metus quis leo pharetra, quis semper urna aliquam. Fusce consectetur accumsan augue sit amet iaculis. Suspendisse volutpat urna vitae fermentum eleifend. Maecenas sapien leo, gravida vitae pellentesque quis, efficitur in erat. Maecenas elementum euismod hendrerit. Mauris sagittis massa a orci."
listeMot = ["Hogym", "Celloggimbur", "Laglesgim", "Sylcyllis", "Morbir", "Limgem", "Silgimculnir", "Narmar", "Solgamberthi", "Cyllig", "Thalomorn", "Rluggum", "Ornbar", "Merhosyl", "Callisthunir", "Thaligber", "Limbarmar", "Lishalllumcal", "Berthe", "Hathulemhe", "Colmorhi", "Salthalegorn", "Birmircyl", "Bermor", "Morlag", "Barbirorn", "Burmir", "Humarhamur", "Leglam", "Hugimirn", "Berburthamur", "Lasloglum", "Gomlamthi", "Narmarborern", "Lomlos", "Urnlasho", "Hical", "Hisol", "Leshe", "Gumsalculsil", "Morcalsul", "Barlugha", "Salhu", "Celmorgember", "Byrhebyr", "Birhogim", "Helisloshi", "Syllas", "Gymcalhober", "Gimcullegirn", "Borlessil", "Thitha", "Cylcelnor", "Borbyrhulys", "Loglistha", "Silbartha", "Orncilbirgom", "Lasnormer", "Lumsolthalig", "Burlyscul", "Murgomhellhi", "Thatheluslag", "Lyshallluslam", "Mirborcil", "Nircalbur", "Barlugarn", "Gimcul", "Thulam", "Hecolha", "Ornmur", "Lamber", "Sulleshe", "Lomlember", "Loscal", "Calornthilog", "Limlesgam", "Thigomcul", "Laglyslomlis", "Erngomlig", "Gamlusmorcol", "Syllag", "Hothoirnlug", "Hesolmar", "Lugcul", "Thicolthu", "Narlescul", "Nirmersolurn", "Logcel", "Lasloglag", "Lessellamyrn", "Gymlys", "Thasal", "Silurnsellag", "Hallloslysbur", "Ligbir", "Burcylcel", "Narlisho" ,"Hosal","Liscal", "Sulbarmornar", "Tyfoxe", "Xusini", "Kidoxa", "Piphafy", "Chirra", "Rrobysu", "Jasu", "Quacy", "Laqui", "Nophe", "Mmyjyhe", "Quelli", "Jazo", "Mmichera", "Rroky", "Mmelli", "Girre", "Kibi", "Zafu", "Nowomi", "Dunummo", "Phasone", "Gipho", "Kyjado", "Senoze", "Gocahy", "Mmoha", "Mata", "Vupo", "Lochu", "Zeto", "Cycaci", "Llollace", "Cuphiwa", "Thexe", "Billu", "Matuko", "Rruxigu", "Bogu", "Vesi", "Wetu", "Jegi", "Gake", "Chullene", "Rruno", "Hyza", "Poru", "Nyxichi", "Fadylu", "Lajyse", "Phuxu", "Thehyko", "Quovavu", "Lleji", "Kynugy", "Mmyte", "Pakufa", "Sychecha", "Thine", "Sidemi", "Mmeka", "Jyfybo", "Mmuquoby", "Vuci", "Raci", "Zyhi", "Sujytho", "Cukemo", "Mixevo", "Thyxuwu", "Muphaba", "Pehide", "Thaserra", "Byjuwi", "Geka", "Zurruca", "Hymmy", "Thuju", "Rydu", "Jeduty", "Lluzali", "Rroce", "Sala", "Sipehu", "Pazasi", "Hagyga", "Nophy", "Rrammyca", "Kevygu", "Hellu", "Jimiru", "Llommiga", "Fasopy", "Navede", "Wireju", "Kotherru", "Cuphu", "Lloto", "Lledagy", "Syqua", "Zajerry", "Wipugo", "Sixare", "Gyka", "Bibowo", "Poje", "Mechiwi", "Juzuke", "Nyjige", "Zycu", "Govopy", "Nibo", "Tysy", "Viri", "Mmoxuby", "Boxemmi", "Xathe", "Mmocho", "Rycho", "Pijoly", "Mexo", "Thytha", "Gequo", "Rycypy", "Boquirri", "Zapu", "Gichu", "Rethu", "Gully", "Quoquafa", "Vozella", "Fibonu", "Dodyra", "Theky", "Sozawy", "Cehypy", "Rrotyhu", "Mowe", "Chusuny", "Pyru", "Dypu", "Juhuta", "Polo", "Phikotho", "Polymmo", "Hyse", "Suquajo", "Lletyjo", "Phata", "Fille", "Medy", "Cephellu", "Wogaha", "Quarrythy", "Mmanure", "Tumu", "Rothe", "Hapha", "Loxocho", "Coquawi", "Bonephe", "Suchu", "Mmiweso", "Mallyzy", "Wimma", "Rriwufi", "Nopho", "Pima", "Gyki"]


def generateUser():
        userDao = UserDao()
        for i in range(100):
                tmp = UserModel(id=None, username=listeMot[i])
                userDao.save(tmp)

def generateIngredients():        
        ingredientDao = IngredientDao()
        for i in range(100):
                ingredientDao.save(IngredientModel(id=None, id_IngredientType=(randint(1, 13)),
                        id_QuantityUnit=(randint(1,20)), name=listeMot[i], baseCost=(randint(0, 15)), baseQuantity=(randint(0,4))))

def generateRecipes():
        recipeDao = RecipeDao()
        for i in range(100):
                recipeDao.save(RecipeModel(id=None, id_User=(randint(1, 100)), name=listeMot[i], directives=lorem))

def generateCart():
        cartDao = CartDao()
        for i in range(100):
                cartDao.save(CartModel(id=None, id_User=(randint(1, 100)), totalCost=(randint(20, 250))))


def generateRating():
        ratingDao = RatingDao()
        for i in range(100):
                ratingDao.save(RatingModel(id=None, id_Recipe=(randint(1, 100)), id_User=(randint(1, 100)), value=(uniform(0, 5))))


if __name__ == "__main__":
        #generateUser()
        #generateIngredients()
        #generateRecipes()
        #generateCart()
        generateRating()