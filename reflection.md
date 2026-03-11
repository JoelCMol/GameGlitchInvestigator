# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    - One bug I encountered occurred when I guessed 80 and the game told me to go lower. I then guessed 70, even though the secret number was 85, which indicates the feedback logic may be incorrect.
    Additionally, the 1–100 range appears to be misconfigured. When the secret number was 1, the game repeatedly told me to guess lower, and when it was 100, it sometimes told me to guess higher. 
    - After a game over, and clicking on (New Game) button it does not start a new game.
    - The game shows the message "Out of attempts", and what the secret number is when there's still has one attempt left.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? ChatGPT, and Copilot
  Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  In check_guess, when the guess is too high it says "Go HIGHER!" and when too low it says "Go LOWER!" — both are backwards.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  No misleading or incorrect suggestions given

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I played the game multiple times to see if the bug had been fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the tests using pytest and it would show 100%, meaning all of the test cases passed.
- Did AI help you design or understand any tests? How?
  I used Claude to help me write a new test case targeting the bug we had fixed, about the check_guess function.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Be very specific with your prompts about the bug or feature that you want to implement. 
- What is one thing you would do differently next time you work with AI on a coding task?
  Provide context about the project am working on, and work on solving a bug independently on its own chat window.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Its very important to undestand the proposing changes AI wants to make before you accept them into your code. Althought, the code might seem to work fine, write multiple test cases, and very functionality on the front end.