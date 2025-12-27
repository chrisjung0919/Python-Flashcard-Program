import random
import json

# Save flashcards
def save_flashcards(flashcards):
    with open("flashcards.json", "w") as file:
        json.dump(flashcards, file)

# Load flashcards
def load_flashcards():
    try:
        with open("flashcards.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Show the menu to choose
def show_menu():
    print("1. Add flashcard")
    print("2. Delete flashcard")
    print("3. Show flashcard")
    print("4. Quiz flashcard")
    print("5. Exit")

# Add a new flashcard
def add_flashcards(flashcards):
    print("Enter the question: ")
    question = input()

    print("Enter the answer: ")
    answer = input()

    flashcard = {"Question: ": question, "Answer: ": answer}

    flashcards.append(flashcard)

    print("New flashcard added!")

    return flashcards

# Delete a flashcard
def delete_flashcards(flashcards):

    delete_choice = 0

    if len(flashcards) == 0:
        print("No flashcards to delete!!!")
        return flashcards
    
    print("Flashcards:")
    for i in range(len(flashcards)):
        print("Flashcard ", i + 1)
        print("Question: ", flashcards[i]["Question: "])
        print("Answer: ", flashcards[i]["Answer: "])
        print("")

    print("Choose the flashcard to delete: ")
    delete_choice = int(input())

    if delete_choice < 1 or delete_choice > len(flashcards):
        print("Invalid choice")
        return flashcards

    flashcards.pop(delete_choice - 1)
    print("Removed flashcard # ", delete_choice)

    return flashcards

# Display the list of flashcards
def show_flashcards(flashcards):
    if len(flashcards) == 0:
        print("No flashcards!!!")
        return
    
    print("Flashcards:")
    print("")
    
    for i in range(len(flashcards)):
        print("Flashcard ", i + 1)
        print("Question: ", flashcards[i]["Question: "])
        print("Answer: ", flashcards[i]["Answer: "])
        print("")

# Quiz flashcards
def quiz_flashcards(flashcards):
    if len(flashcards) == 0:
        print("No flashcards!!!")
        return
    
    random_question = random.randint(0, len(flashcards) - 1)
    
    print("Question: ", flashcards[random_question]["Question: "])

    guess = input()

    if guess == flashcards[random_question]["Answer: "]:
        print("Correct!")
    else:
        print("Wrong! The answer is ", flashcards[random_question]["Answer: "])

def main():

    userchoice = 0
    flashcards = load_flashcards()

    print("Welcome to flashcards program!!!!!")

    while userchoice != 5:
        show_menu()

        userchoice = int(input())

        if userchoice == 1:
            flashcards = add_flashcards(flashcards)
        elif userchoice == 2:
            flashcards = delete_flashcards(flashcards)
        elif userchoice == 3:
            show_flashcards(flashcards)
        elif userchoice == 4:
            quiz_flashcards(flashcards)
        # Exit the program
        elif userchoice == 5:
            save_flashcards(flashcards)
            print("Flashcards saved. Goodbye!")
    
if __name__ == "__main__":
    main()
