using System;

namespace RockPaperScissors
{
    class Program
    {
        static void Main(string[] args)
        {
            PlayGame();
        }

        static void PlayGame()
        {
            Console.WriteLine("Welcome to Rock-Paper-Scissors!");
            string userChoice = GetUserChoice();
            string computerChoice = GetComputerChoice();
            Console.WriteLine($"You chose: {userChoice}");
            Console.WriteLine($"Computer chose: {computerChoice}");
            string result = DetermineWinner(userChoice, computerChoice);
            Console.WriteLine(result);
        }

        static string GetUserChoice()
        {
            Console.Write("Enter your choice (rock, paper, scissors): ");
            string userChoice = Console.ReadLine().ToLower();
            while (userChoice != "rock" && userChoice != "paper" && userChoice != "scissors")
            {
                Console.Write("Invalid choice. Please enter rock, paper, or scissors: ");
                userChoice = Console.ReadLine().ToLower();
            }
            return userChoice;
        }

        static string GetComputerChoice()
        {
            string[] choices = { "rock", "paper", "scissors" };
            Random random = new Random();
            int index = random.Next(choices.Length);
            return choices[index];
        }

        static string DetermineWinner(string userChoice, string computerChoice)
        {
            if (userChoice == computerChoice)
            {
                return "It's a tie!";
            }
            else if ((userChoice == "rock" && computerChoice == "scissors") ||
                     (userChoice == "paper" && computerChoice == "rock") ||
                     (userChoice == "scissors" && computerChoice == "paper"))
            {
                return "You win!";
            }
            else
            {
                return "Computer wins!";
            }
        }
    }
}

