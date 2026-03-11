from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct!" in message

# Fixed the test which only checked the outcome, not the message, which had the bug. Now it checks both.
def test_guess_too_high():
    # Bug was: "Too High" returned "Go HIGHER!" — should say "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER!" in message

# Fixed the test which only checked the outcome, not the message, which had the bug. Now it checks both.
def test_guess_too_low():
    # Bug was: "Too Low" returned "Go LOWER!" — should say "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message
