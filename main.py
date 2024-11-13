from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

customer = {
    "name": "CustomerName",
    "email": "CustomerEmail",
    "address": "CustomerAddress"
}

items = [
    {"name": "Product 1", "quantity": 2, "price": 10.00},
    {"name": "Product 2", "quantity": 3, "price": 15.00}
]

taxRate = 0.05

def calculateTotal(items, taxRate):
    totalBeforeTax = sum(item["quantity"] * item["price"] for item in items)
    tax = totalBeforeTax * taxRate
    total = totalBeforeTax + tax
    return totalBeforeTax, tax, total

def generateInvoice(customer, items, taxRate, filename="Invoice.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setTitle("Invoice")

    c.drawString(100, 750, f"Invoice for {customer['name']}")
    c.drawString(100, 735, f"Email {customer['email']}")
    c.drawString(100, 720, f"Address {customer['address']}")

    y=680
    for item in items:
        line = f"{item['name']}: RS {item['price']} x {item['quantity']}"
        c.drawString(100, y, line)
        y -= 15
    
    totalBeforeTax, tax, total = calculateTotal(items, taxRate)
    c.drawString(100, y-20, f"Total Before Tax: {totalBeforeTax:.2f}")
    c.drawString(100, y-35, f"Tax: {tax:.2f}")
    c.drawString(100, y-50, f"Total: {total:.2f}")

    c.save()

generateInvoice(customer, items, taxRate)