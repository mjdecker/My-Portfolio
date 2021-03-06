#include <iostream>
#include <fstream>
#include <string>
#include <vector>
// Author : Teague, Samuel
// Date : 18 November 2016. Updated 15 February 2018.


//function prototypes



void drawHangman(int);
std::string genSecretWord(const std::vector<std::string> & );
void showStatus(const std::string & );
char getGuess();
bool recordGuess(const std::string & , std::string &, char);
bool isWin(std::string);
void fillDictionaryFromFile(const std::string & fileName, std::vector<std::string> & dictionary);


int main()
{
    //constants
    const std::string INFILE_NAME = "words-alpha.txt";
    const int NUM_WRONG_ALLOWED = 7;

    //vector
    std::vector<std::string> dictionary;

    if (!fillDictionaryFromFile(INFILE_NAME, dictionary))   //if an error occurred reading from file
    {
        std::cerr << "Error reading from file\n";
        return 1;
    }

    //variables
    int numWrong = 0;
    char letter;
    std::string word;
    std::string guessWord;

    //filling the dictionary array


    do {
        system("cls");
        word = genSecretWord(dictionary);

        guessWord = "";
        for (int i = 0; i < word.length(); ++i)
            guessWord += " ";

        numWrong = 0;
        do {
            drawHangman(numWrong);
            showStatus(guessWord);
            letter = getGuess();


            if (!recordGuess(word, guessWord, letter))
                numWrong++;


        } while (!isWin(guessWord) && numWrong < NUM_WRONG_ALLOWED);

        if (!isWin(guessWord))
        {
            for (i = 0; i < word.length(); ++i)
                std::cout << ' ' << word[i] << ' ';

            std::cout << '\n';
            std::cout << "--------------------------\n";
            std::cout << "Game over. You lost.\n";
            std::cout << "--------------------------\n";
        }
        else
        {
            std::cout << "--------------------------\n";
            std::cout << "You Win!!!! :)\n";
            std::cout << "--------------------------\n";
        }
        std::cout << "Do you want to play again? [Y or N]";
        std::cin >> word;
    } while (toupper(word[0]) == 'Y');


    return 0;
}

bool fillDictionaryFromFile(const std::string & fileName, std::vector<std::string> & dictionary)
{
    std::ifstream infile;
    infile.open(fileName);

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            infile >> word;     
            dictionary.push_back(word);

        }
        infile.close();
        return true;
    }
    else
        return false;


}

std::string genSecretWord(const std::vector<std::string> & d )
{
    /*
    Function : genSecretWord()
    Description : Randomly select an index to the dictionary array (number between 0 and number of words-1.)
    Parameters : the dictionary
    Returns : the secret word
    */


    //get random index number
    std::srand(std::time(NULL));
    int index = std::rand() % d.size();

    

    return d[index];
}

char getGuess()
{
    /*
    Function : getGuess()
    Description : Get next guess from the player via the console window
    Parameters : none
    Returns : The guessed letter
    */

    //variable
    char l;
    bool isValid = false;   //added in update

    //get input
    do {    //loop added in update
        std::cout << "Enter your guess: ";
        std::cin >> l;

        //below code added in update
        isValid = isalpha(l);
        if (!isValid)
            std::cout << "Invalid, Please try again.\n";
    } while (!isValid);


    return tolower(l);
}

void showStatus(std::string guess)
{
    /*
    Function : showStatus()
    Description : Show current game status, i.e., each guessed letter is shown in its correct position within the secret word.
    Letters that have not been guessed yet are shown as “ _ “ to indicate missing letters.
    Parameters : Guess array of char containing currently guessed letters in their correct positions.
    Returns : none

    Update Note: Adjusted to use std::string instead of c-syle string. 
    */

    for (int i = 0; i < guess.length(); i++)
    {
        std::cout << ' ';
        if (guess[i] == ' ')
            std::cout << '_';
        else
            std::cout << guess[i];
        std::cout << ' ';
    }
    std::cout << '\n';
}

bool recordGuess(const std::string & word, std::string & guess, char letter)
{
    /*
    Function : recordGuess()
    Description : Place correctly guessed letter in array guess in its correct spot.
    Parameters : the correct word, the guess word so far, and the letter guessed

    Update Note: Adjusted to use std::strings instead of c-strings.
    */

    //variables
    int i = 0;
    bool correct = false;

    //processing
    while (i < word.length() && !correct)
    {
        correct = (word[i] == letter);
        i++;
    }

    if (correct)
        for (i = 0; i < word.length(); i++)
            if (letter == word[i])
                guess[i] = letter;

    return correct;

}

void drawHangman(int x)
{
    /*
    Function : drawHangman()
    Description : Draw hangman figure. Number of body parts shown corresponds to the current wrong turn. 
        Wrong turn 1 -> head, 2 -> body, etc.
    Parameters : Current amt of wrong answers (1 -> 6)
    Returns : none

    NOTE: Modify this function with extreme care. Output formatting on the console is hard to set up properly.
    */

    std::cout << "-------\n";
    std::cout << "|/    |\n";
    std::cout << "|     ";

    if (x > 0)
        std::cout << 'O';
    else
        std::cout << ' ';

    std::cout << '\n';
    std::cout << "|     ";

    if (x > 1)
        std::cout << '|';
    else
        std::cout << ' ';

    std::cout << '\n';
    std::cout << "|    ";

    if (x > 3)
        std::cout << '/';
    else
        std::cout << ' ';

    if (x > 2)
        std::cout << 'O';

    if (x > 4)
        std::cout << '\\';
    else
        std::cout << ' ';

    std::cout << '\n';
    std::cout << "|    ";

    if (x > 5)
        std::cout << '/';
    else
        std::cout << ' ';

    std::cout << ' ';

    if (x > 6)
        std::cout << '\\';
    else
        std::cout << ' ';

    std::cout << '\n';
    std::cout << '|' << '\n';
    std::cout << "----------------------------------\n";
}

bool isWin(std::string guess)
{
    /*
    Function : isWin()
    Description : Do we have a winner yet, i.e., are all characters in guess array not ‘ ‘ at this time?
    Parameters : guess string
    Returns : true if the whole word is revealed, false otherwise

    Update Note: Changed to use std::string instead of c-string
    */

    //variables
    bool isWin = true;
    int i = 0;

    //processing
    while (i < guess.length() && isWin)
    {
        if (guess[i] == ' ')
            isWin = false;
        i++;
    }

    return isWin;
}


