# Telegram Bot Project

This project is a Telegram bot designed to provide educational content on topics related to sexual health, including information on pregnancy, Sexually Transmitted Diseases, contraceptives, and consent. 

## Project Structure

```
telegram-bot-project
├── src
│   ├── bot.py                # Main entry point for the Telegram bot
│   ├── handlers              # Contains command and button handlers
│   │   ├── commands.py       # Command handlers for the bot
│   │   ├── buttons.py        # Button callback handlers
│   │   └── quiz.py           # Quiz functionality logic
│   ├── utils                 # Utility functions
│   │   └── keyboards.py      # Keyboard layouts for user interaction
│   └── data                  # Content data for the bot
│       └── content.py        # Holds quiz questions and educational content
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (e.g., bot token)
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd telegram-bot-project
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add your Telegram bot token:
   ```
   TELEGRAM_TOKEN=your_bot_token_here
   ```

4. **Run the bot:**
   Execute the main bot script:
   ```
   python src/bot.py
   ```

## Usage

- Start the bot by sending the `/start` command.
- Use the buttons provided in the bot's messages to navigate through the educational content.
- Participate in the quiz to test your knowledge on the topics covered.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.