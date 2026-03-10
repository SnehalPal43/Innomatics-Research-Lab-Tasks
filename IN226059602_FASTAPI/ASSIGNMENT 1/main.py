from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True}
]
products.append({"id":5,"name":"Laptop Stand","price":999,"category":"Electronics","in_stock":True})
products.append({"id":6,"name":"Mechanical Keyboard","price":2499,"category":"Electronics","in_stock":True})
products.append({"id":7,"name":"Webcam","price":1599,"category":"Electronics","in_stock":False})

#Q1:
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


#Q2:
@app.get("/products/category/{category_name}")
def get_category(category_name: str):

    result = [p for p in products if p["category"].lower() == category_name.lower()]

    if not result:
        return {"error": "No products found in this category"}

    return result

#Q3:
@app.get("/products/instock")
def in_stock_products():

    result = [p for p in products if p["in_stock"]]

    return {
        "in_stock_products": result,
        "count": len(result)
    }

#Q4:
@app.get("/store/summary")
def store_summary():

    in_stock = len([p for p in products if p["in_stock"]])
    out_stock = len(products) - in_stock

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock,
        "out_of_stock": out_stock,
        "categories": categories
    }


#Q5
@app.get("/products/search/{keyword}")
def search_product(keyword: str):

    result = [p for p in products if keyword.lower() in p["name"].lower()]

    if not result:
        return {"message": "No products matched your search"}

    return {
        "matched_products": result,
        "count": len(result)
    }

#Bonus
@app.get("/products/deals")
def deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }