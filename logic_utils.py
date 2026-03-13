def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200  # BUG FIX: original app.py used (1, 50) for Hard, which is *easier* than Normal. Changed to (1, 200).
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Refactored check_guess logic into logic_utils.py using Claude, 
# and fixed the bug where "Too High" returned "Go HIGHER!" and "Too Low" returned "Go LOWER!" — 
# should say "Go LOWER!" and "Go HIGHER!" respectively.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!" # BUG FIX: original app.py had the direction messages swapped — "Too High" said "Go HIGHER!" Fixed here to just return the outcome; the UI layer adds the message.
        else:
            return "Too Low", "📈 Go HIGHER!" # BUG FIX: original app.py "Too Low" said "Go LOWER!" — also wrong. Fixed by returning only the correct outcome label.

    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!" # BUG FIX: same swapped-message fix applied to the TypeError fallback branch.
        return "Too Low", "📈 Go HIGHER!" # BUG FIX: same swapped-message fix applied to the TypeError fallback branch.

# FIX: Refactored update_score logic into logic_utils.py using Claude, and fixed the bug where the score didn't update correctly based on the outcome and attempt number.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # BUG FIX: original code awarded +5 points on even-numbered attempts for a wrong "Too High" guess.
        # Wrong guesses should always cost points, not reward the player.
        # if attempt_number % 2 == 0:
        #     return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score