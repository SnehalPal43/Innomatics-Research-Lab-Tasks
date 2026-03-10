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


# DAY 2 - Q1
@app.get("/products/filter")
def filter_products(min_price: int = 0, max_price: int = 10000):

    filtered = [p for p in products if min_price <= p["price"] <= max_price]

    return {
        "filtered_products": filtered,
        "count": len(filtered)
    }

    # Q2 — GET /products/{product_id}/price
@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"name": product["name"], "price": product["price"]}
    return {"error": "Product not found"}

#Q3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

feedback = []

class CustomerFeedback(BaseModel):
    customer_name: str = Field(..., min_length=2)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=300)

@app.post("/feedback")
def submit_feedback(feedback_data: CustomerFeedback):
    feedback.append(feedback_data.dict())
    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback_data.dict(),
        "total_feedback": len(feedback)
    }

#Q4
# Q4: Product Summary Dashboard
@app.get("/products/summary")
def products_summary():
    total_products = len(products)
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_of_stock_count = total_products - in_stock_count

    # Cheapest product
    cheapest = min(products, key=lambda x: x["price"])
    # Most expensive product
    most_expensive = max(products, key=lambda x: x["price"])

    # Unique categories
    categories = list(set([p["category"] for p in products]))

    return {
        "total_products": total_products,
        "in_stock_count": in_stock_count,
        "out_of_stock_count": out_of_stock_count,
        "cheapest": {"name": cheapest["name"], "price": cheapest["price"]},
        "most_expensive": {"name": most_expensive["name"], "price": most_expensive["price"]},
        "categories": categories
    }

#Q5
from pydantic import BaseModel, Field
from typing import List

# List to store bulk orders
bulk_orders = []

# Pydantic Models
class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=50)

class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: str = Field(..., min_length=5)
    items: List[OrderItem] = Field(..., min_items=1)

# Q5: POST /orders/bulk
@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):
    confirmed = []
    failed = []
    grand_total = 0

    for item in order.items:
        # Check if product exists
        product = next((p for p in products if p["id"] == item.product_id), None)
        if not product:
            failed.append({"product_id": item.product_id, "reason": "Product not found"})
            continue
        # Check stock
        if not product["in_stock"]:
            failed.append({"product_id": item.product_id, "reason": f"{product['name']} is out of stock"})
            continue
        # Calculate subtotal
        subtotal = product["price"] * item.quantity
        grand_total += subtotal
        confirmed.append({"product": product["name"], "qty": item.quantity, "subtotal": subtotal})

    # Save order (optional)
    order_record = {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": grand_total
    }
    bulk_orders.append(order_record)

    return order_record

#Bonus
# List to store normal orders (for bonus)
orders = []
order_counter = 1  # unique order_id generator

class OrderItemSimple(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=50)

class OrderSimple(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: str = Field(..., min_length=5)
    items: List[OrderItemSimple] = Field(..., min_items=1)

# POST /orders → new orders start as "pending"
@app.post("/orders")
def create_order(order: OrderSimple):
    global order_counter
    order_record = {
        "order_id": order_counter,
        "company_name": order.company_name,
        "contact_email": order.contact_email,
        "items": [{"product_id": i.product_id, "quantity": i.quantity} for i in order.items],
        "status": "pending"
    }
    orders.append(order_record)
    order_counter += 1
    return order_record

# GET /orders/{order_id} → view single order
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders if o["order_id"] == order_id), None)
    if not order:
        return {"error": "Order not found"}
    return order

# PATCH /orders/{order_id}/confirm → confirm pending order
@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):
    order = next((o for o in orders if o["order_id"] == order_id), None)
    if not order:
        return {"error": "Order not found"}
    order["status"] = "confirmed"
    return order