# task02:Simple Grocery Bill Calculator

price = float(input("Enter item price: ₹"))
quantity = int(input("Enter item quantity: "))

total = price * quantity
gst = total * 0.18
final_amount = total + gst

print(f"\nTotal: ₹{total:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Final Bill: ₹{final_amount:.2f}")
