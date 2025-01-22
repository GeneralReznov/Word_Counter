def countwords(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    userinput = input("Please enter a sentence or paragraph: ").strip()
    
    # Check if the input is empty
    if not userinput:
        print("Error: You entered an empty input. Please provide some text.")
        return  # Exit the program if input is empty
    
    # Count the number of words in the input
    wordcount = countwords(userinput)
    
    # Display the word count to the user
    print(f"The number of words in your input is: {wordcount}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()