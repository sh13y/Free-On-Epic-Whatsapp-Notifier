# Free On Epic WhatsApp Notifier

🎮 **Free On Epic WhatsApp Notifier** is a fun little project that fetches free games from the Epic Games Store and sends notifications to your WhatsApp group using the Green API. Because who doesn't love free games and WhatsApp notifications?

## How It Works

1. **Fetch Free Games**: The script fetches the latest free games from the Epic Games Store.
2. **Send Notifications**: It sends a beautifully crafted message with game details and an image to your WhatsApp group using the Green API.

## Setup

### Prerequisites

- Python 3.x
- A WhatsApp account (duh!)
- Green API account (to send WhatsApp messages)

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/sh13y/free-on-epic-whatsapp-notifier.git
    cd free-on-epic-whatsapp-notifier
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory and add your Green API credentials and WhatsApp number:
    ```env
    API_URL=apiUrl
    GREEN_API_INSTANCE_ID=your_instance_id
    GREEN_API_API_TOKEN=your_api_token
    WHATSAPP_NUMBER=your_whatsapp_number_with_country_code
    ```

### Usage

Run the script:
```sh
python script.py
```

Sit back, relax, and watch as your WhatsApp group gets flooded with notifications about free games. 🎉

## Code Overview

### `script.py`

- **Imports**: We import `requests` for making HTTP requests, `dotenv` for loading environment variables, `os` for accessing environment variables, and `datetime` for formatting dates.
- **Environment Variables**: Load your Green API credentials and WhatsApp number from the `.env` file.
- **Fetch Free Games**: Fetches free games from the Epic Games Store.
- **Format Date**: Formats the date to be more human-readable.
- **Send WhatsApp Notification**: Sends a WhatsApp message with game details and an image using the Green API.
- **Main Function**: Fetches games and sends notifications.

## Green API

Green API is a service that allows you to send WhatsApp messages programmatically. It's like having a personal WhatsApp butler who sends messages for you. 🧑‍💼

### Why Green API?

- **Easy to Use**: Simple API endpoints for sending messages.
- **Reliable**: Ensures your messages are delivered.
- **Affordable**: Great pricing for hobby projects.

### Documentation

For more details, check out the [Green API documentation](https://green-api.com/en/docs/).

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Let's make this project even more awesome together! 🚀

## License

This project is licensed under the WTFPL License. See the [LICENSE](LICENSE) file for details.

---

Happy coding! And may your WhatsApp group always be filled with free games! 🎮📱
