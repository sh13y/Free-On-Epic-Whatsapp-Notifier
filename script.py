
import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv("API_URL")
GREEN_API_INSTANCE_ID = os.getenv("GREEN_API_INSTANCE_ID")
GREEN_API_API_TOKEN = os.getenv("GREEN_API_API_TOKEN")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")  # WhatsApp number to send the notification to (with country code)

def fetch_free_games():
    """Fetch free games from the Epic Games Store."""
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching free games: {e}")
        return []

    free_games = []
    for game in data.get("data", {}).get("Catalog", {}).get("searchStore", {}).get("elements", []):
        if game.get("promotions"):
            for promo in game["promotions"].get("promotionalOffers", []):
                for offer in promo.get("promotionalOffers", []):
                    discounted_price = game.get("price", {}).get("totalPrice", {}).get("discountPrice", 0)
                    
                    if discounted_price == 0:  # Check if it's free
                        # Extract namespace and id for constructing the URL
                        namespace = game.get("namespace")
                        id_value = game.get("id")
                        
                        if namespace and id_value:  # Ensure both values are present
                            purchase_url = f"https://store.epicgames.com/purchase?offers=1-{namespace}-{id_value}"
                            free_games.append({
                                "title": game.get("title"),
                                "description": game.get("description", "No description available."),
                                "original_price": "Free",
                                "discounted_price": "Free",
                                "url": purchase_url,
                                "image_url": game.get("keyImages", [{}])[0].get("url", ""),
                                "end_date": offer.get("endDate")
                            })
    return free_games

def format_date(date_str):
    """Format the date to be more human-readable."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_obj.strftime("%B %d, %Y at %I:%M %p")

def send_whatsapp_notification(free_games):
    """Send a WhatsApp message with details about free games."""
    if not free_games:
        print("No free games to notify.")
        return
    
    for game in free_games:
        # Create the message with clickable 'Claim Now' link
        message = "🎮 *Free Games on Epic Games Store!*\n\n"
        message += f"📌 *{game['title']}*\n"
        message += f"💬 {game['description']}\n"
        message += f"💰 *Original Price*: ${game['original_price']}\n"
        message += f"💰 *Discounted Price*: ${game['discounted_price']}\n"
        message += f"🔗 *Claim Now*({game['url']})\n"  # This is the clickable link
        message += f"🕒 *Valid until*: {format_date(game['end_date'])}\n"

        # Send the message with image via Green API
        image_url = game['image_url']
        if image_url:
            payload = {
                "chatId": f"{WHATSAPP_NUMBER}@g.us",  # WhatsApp group id
                "urlFile": image_url,
                "fileName": "game_image.jpg",
                "caption": message
            }
            url = f"{API_URL}/waInstance{GREEN_API_INSTANCE_ID}/sendFileByUrl/{GREEN_API_API_TOKEN}"
            headers = {
                'Content-Type': 'application/json'
            }
            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
                print("WhatsApp notification with image sent successfully!")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send WhatsApp notification with image: {e}")


def main():
    """Main function to fetch games and send notifications."""
    print("Fetching free games...")
    free_games = fetch_free_games()
    if free_games:
        print("Free games found! Sending WhatsApp notification...")
        send_whatsapp_notification(free_games)
    else:
        print("No free games available at the moment.")

if __name__ == "__main__":
    main()
