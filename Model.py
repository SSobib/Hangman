import glob


class Model:

    def __init__(self):
        # English car model hangman_words_en.db
        self.database_name = "databases/hangman_words_ee.db"
        self.image_files = glob.glob("images/*.png")                            # All hangman images
        # New Game
        self.new_word = None                                                    # Random word from database
        self.user_word = []                                                     # User find letter
        self.all_user_chars = []                                                # Any letter entered incorrectly
        self.counter = 0                                                        # Error counter (wrong letters)
        # Leaderboard
        self.player_name = "UNKNOWN"
        self.leaderboard_file = "leaderboard.txt"
        self.score_data = []                                                    # Leaderboard list sisu


