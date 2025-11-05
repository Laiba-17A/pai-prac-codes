# Create a function that asks the user to enter a sentence then writes the sentence to a text file
# named "questions.txt" if it's a question. Handle all possible exceptions as well.
def save_question():
    try:
        sentence = input("Enter a sentence: ")
        if sentence.strip().endswith("?"):
            with open("questions.txt", "a") as f:
                f.write(sentence + "\n")
            print("Question saved successfully.")
        else:
            print("This is not a question. Nothing saved.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

save_question()
