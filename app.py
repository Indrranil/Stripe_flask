from flask import Flask, redirect, request
import stripe 

app = Flask(__name__, static_url_path="", static_folder="public")
stripe.api_key = "sk_test_51OubhsSAkfFPs5lWOLSJwE6IE7gBhEgGQNkiSPWAP7NQr3JotPH3iXJEmQ0ojXfBUdnLpFD5qEo7xI74IV3cKfES00QXSQYpoM"

YOUR_DOMAIN ="http://localhost:9090"

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            
            line_items = [
                {
                    'price': 'price_1OurwsSAkfFPs5lWzTSmtCVu',
                    'quantity':1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN +"success.html", 
            cancel_url=YOUR_DOMAIN +"cancel.html"
        
        )
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code=303)

if __name__ == "__main__":
    app.run(port=9090, debug=True)
    