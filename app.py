import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# Bug was: st.session_state.attempts to zero instead of one, which caused the first guess to be counted as attempt 0 and messed up the scoring and attempt limit logic. Now it initializes to zero so the first guess is attempt 1.
if "attempts" not in st.session_state:
    st.session_state.attempts = 0 # BUG FIX: was initialized to 1, causing an off-by-one error where the first submit counted as attempt 2 and "Attempts left" showed one fewer than it should.

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    #Bug was: The prompt didn't update with the correct range and attempt limit based on difficulty. Now it dynamically shows the correct range and attempts left.
    f"Guess a number between {low} and {high}. "
    #if st.session_state.attempts < attempt_limit else 0
    f"Attempts left: {attempt_limit - st.session_state.attempts }."
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts + 1)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)  # BUG FIX: was hardcoded randint(1, 100); now respects the selected difficulty range.
    st.session_state.score = 0       # BUG FIX: score was never reset on new game, so it carried over from the previous round.
    st.session_state.status = "playing"  # BUG FIX: status was never reset, so a won/lost game could never be replayed without a page refresh.
    st.session_state.history = []    # BUG FIX: history was never cleared on new game, polluting the debug panel with old guesses.
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.balloons()
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # BUG FIX: Removed the even/odd type-switching. secret is now always the integer from session state, so check_guess gets consistent types on every attempt
        # if st.session_state.attempts % 2 == 0:
        #    secret = str(st.session_state.secret)
        # else:
        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )
    st.rerun() # BUG FIX: This triggers an immediate second rerun after all session state updates, so the attempts count and history will display correctly right away.

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
