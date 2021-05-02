class Solution(object):
    def suggestedProducts(self, products, searchWord):
        ret = []
        products.sort()
        for i in range(0, len(searchWord)):
            products = [p for p in products if len(
                p) > i and p[i] == searchWord[i]]
            ret.append(products[:3] if len(products) > 3 else products)
        return ret
