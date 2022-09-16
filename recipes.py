import ingredients
def roundBy(grams, round):
  return int(grams//round * round)

def Recipe(id, name, breakfast, secondbreakfast, lunch, dinner, kcals, *ingredientsAndProportions):
  proportionSum = 0
  proportionIndex = 0
  i = 0
  print(name)
  ingrList = [] # list of ingredients
  propList = [] # list of proportions
  List = [] #list of product.
  sumGrams = 0
  for ingredient in ingredientsAndProportions:
    print(type(ingredient))
    if type(ingredient) == int or type(ingredient) == float:
      propList.append(ingredient)
      sumGrams += ingredient
    else:
      ingrList.append(ingredient.name)
      List.append(ingredient)
    
  print(ingrList, propList)
 # for ingr in range(len(propList)):
  #  proportionSum += propList[ingr]/sumGrams *kcals /
  #proportionIndex = round(kcals/proportionSum, 2)
  
  
  for ingr in List:
    #print(propList[i]/sumGrams,kcals)
    kcal = propList[i]/sumGrams * kcals
    grams = roundBy(kcal /List[i].kcal * 100, List[i].rounding)
    kcalss = int(grams/100 * List[i].kcal)
    print(grams,'g produktu',ingr.name,' ma kcal:',kcalss)
    i +=1
  

Recipe(1, 'Sałatka marchew jabłko', True, True, True, True, 500, ingredients.ingredient_jablkoswiezyowoc, ingredients.ingredient_marchewsurowa, 100, 150)
Recipe(2, 'Kurczak z ryżem i parmezanem', False, False, True, True, 800, ingredients.ingredient_pierszkurczaka, ingredients.ingredient_ryzbasmati_tesco, ingredients.ingredient_olejrzepakowy_auchan, ingredients.ingredient_czosnek, ingredients.ingredient_maslo, ingredients.ingredient_winobiale_chardonnay, ingredients.ingredient_buliondrobiowy_knorr, ingredients.ingredient_serparmezan, 200, 200, 20, 10, 25, 100, 750, 150)
  
  


  
#surowka_marchewka_jablko = {'Nazwa': 'Surówka marchewka jabłko', 'Składniki': #ingredients.ingredient_jablkoswiezyowoc ingredient_marchewsurowa}


