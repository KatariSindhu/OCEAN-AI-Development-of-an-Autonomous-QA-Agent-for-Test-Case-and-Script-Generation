# Product Specifications - Checkout Module

## 1. Pricing & Discounts
- **Base Logic**: Total price is calculated as sum of item prices.
- **Discount Codes**: 
  - The code `SAVE15` applies a **15% discount** on the total price.
  - The code `OCEAN20` applies a **20% discount**.
  - Any other code should display an error: "Invalid Code".

## 2. Shipping Policies
- **Standard Shipping**: Free ($0). Delivery in 5-7 days.
- **Express Shipping**: Flat rate of **$10**. Added to the total after discount.

## 3. Payment Rules
- Supported methods: Credit Card, PayPal.
- If "Pay Now" is clicked and form is valid, display "Payment Successful!".