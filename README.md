# Flashy - French Flashcard Learning App

An interactive flashcard application for learning French vocabulary. The app displays French words and automatically flips to show English translations, helping users learn through spaced repetition.

## Features

- **Interactive Flashcards**: Click-based card flipping system
- **Auto-Flip Cards**: Cards automatically flip after 3 seconds to show translations
- **Progress Tracking**: Removes known words from learning deck
- **Persistent Learning**: Saves progress to CSV file for continued learning sessions
- **Visual Design**: Clean card-based interface with custom graphics
- **Smart Algorithm**: Focuses on words you haven't mastered yet
- **Immediate Feedback**: Mark words as known or unknown with visual buttons

## How It Works

1. **Card Display**: Shows a French word on the front of a flashcard
2. **Auto Translation**: After 3 seconds, automatically flips to show English translation
3. **User Input**: Click ✓ if you knew the word, ✗ if you didn't
4. **Progress Saving**: Known words are removed from the learning deck
5. **Continuous Learning**: Focus on remaining unknown words

## Requirements

- Python 3.x
- tkinter (built-in with Python)
- pandas (`pip install pandas`)

## Project Structure

```
flashy-flashcards/
│
├── main.py                    # Main application file
├── data/
│   ├── french_words.csv      # Original vocabulary database
│   └── words_to_learn.csv    # Remaining words to learn (auto-generated)
└── images/
    ├── card_front.png        # Front card background image
    ├── card_back.png         # Back card background image
    ├── right.png             # Checkmark button icon
    └── wrong.png             # X button icon
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/flashy-flashcard-app.git
```

2. Install required dependencies:
```bash
pip install pandas
```

3. Make sure you have the required image files in the `images/` folder:
   - `card_front.png` - Front of flashcard
   - `card_back.png` - Back of flashcard  
   - `right.png` - Checkmark icon
   - `wrong.png` - X icon

4. Create your vocabulary database in `data/french_words.csv`:
```csv
French,English
le,the
de,of
et,and
être,to be
avoir,to have
```

## Usage

Run the application:
```bash
python main.py
```

### Controls
- **✓ Button**: Mark word as known (removes from learning deck)
- **✗ Button**: Mark word as unknown (keeps in learning deck)
- **Auto-flip**: Cards automatically flip after 3 seconds

## Features Explained

### Smart Learning Algorithm
- Starts with complete vocabulary from `french_words.csv`
- Creates `words_to_learn.csv` with remaining unknown words
- Focuses study sessions on words you haven't mastered
- Resumes from where you left off in previous sessions

### Progress Persistence
- Automatically saves learning progress
- Removes mastered words from future sessions
- Tracks remaining vocabulary count
- Continues learning from last session

### User Interface
- Clean, card-based design
- Visual feedback with color changes
- Automatic timing for optimal learning
- Simple two-button interaction system

## Customization

### Adding New Vocabulary
Edit `data/french_words.csv` to add new French-English word pairs:
```csv
French,English
bonjour,hello
merci,thank you
au revoir,goodbye
```

### Changing Flip Timer
Modify the flip timer duration in the code:
```python
flip_timer = window.after(5000, func=flip_card)  # 5 seconds instead of 3
```

### Custom Styling
Update colors and fonts in the code:
```python
BACKGROUND_COLOR = "#YOUR_COLOR"  # Change background color
font=("Arial", 50, "bold")        # Modify font settings
```

## Learning Tips

1. **Daily Practice**: Use for 15-20 minutes daily for best results
2. **Honest Assessment**: Only mark words as "known" if you're confident
3. **Regular Review**: Restart with full vocabulary periodically to reinforce learning
4. **Focus Sessions**: Let the app filter to your problem words

## Future Enhancements

- [ ] Multiple language support
- [ ] Difficulty levels and categories
- [ ] Audio pronunciation
- [ ] Statistics and progress tracking
- [ ] Spaced repetition algorithm
- [ ] Import/export vocabulary lists
- [ ] Dark mode theme
- [ ] Mobile app version

## Contributing

Feel free to fork this project and submit pull requests for new features or improvements.

## Acknowledgments

Built for effective language learning using the proven flashcard method with modern UI design.
