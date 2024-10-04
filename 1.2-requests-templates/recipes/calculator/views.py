from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'strawberry': {
        'шоколад, плитка': 1,
        'сахар, ч.л': 2,
        'сметана, ч.л': 4,
        'клубника, шт': 5
    },
    'cutlets': {
        'фарш, г': 200,
        'рис, г': 50,
        'мука, ст': 0.8,
        'соль, ч.л.': 0.4
    }
}


def calculate_recipe_view(request, recipe_name):

    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                result[item] = new_value
            context = {
                'recipe_name': recipe_name,
                'recipe': result
            }
        else:
            context = {
                'recipe_name': recipe_name,
                'recipe': data
            }

    else:
        context = None

    return render(request, template_name='calculator/index.html', context=context)


def home_view(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='home/home.html', context=context)