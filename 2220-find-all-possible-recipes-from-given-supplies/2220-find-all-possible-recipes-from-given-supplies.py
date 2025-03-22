class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        ans = []
        for r in range(len(recipes)):
            for i in range(len(recipes)):
                ingredient = ingredients[i]

                for ing in ingredient:
                    if ing not in supplies:
                        break
                else:
                    if recipes[i] not in ans:
                        ans.append(recipes[i])
                    supplies.add(recipes[i])
        
        return ans