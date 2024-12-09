#Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.

# The MSG1 variable is used when the command takes 1 parameter.
MSG0 = "\nLa commande {command_word} ne prend pas de paramètre.\n"
MSG1 = "\nLa commande {command_word} prend 1 seul paramètre.\n"


class Actions:
    

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, P).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        #get the direction from the list
        direction = list_of_words[1]
        #move the player to the specific direction
        player.move(direction)
        return True
        

    def get_back(game, list_of_words, number_of_parameters):
        """allows to go back in the previous place
        
        Args:

        game (Game): The game object.
        list_of_words (list): The list of words in the command.
        number_of_parameters (int): The number of parameters expected by the command.

           
        Returns:
            
        """

        player = game.player
        l = len(list_of_words)

        if l-1 != number_of_parameters :
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # going back to the previous room
        if not player.history:
            print("vous avez pas visité")
        else:
            previous_room = player.history.pop()  # Removed the last room
            player.current_room = previous_room
            print(f"\nVous êtes retourné dans la pièce précédente : {previous_room.name}.\n")
        
         # Showing up the new history
            history_names = ", ".join(room.name for room in player.history) if player.history else "aucun historique"
            print(f"\nHistorique des pièces visitées : {history_names}\n")
            if hasattr(previous_room, 'exits') and previous_room.exits:
                exits = [direction for direction, room in previous_room.exits.items() if room]
                exits_display = ", ".join(exits) if exits else "aucune direction disponible"
                print(f"Sorties disponibles depuis {previous_room.name} : {exits_display}\n")
            else:
                print("Les informations sur les sorties ne sont pas disponibles pour cette pièce.\n")

        
        

       
        return True
        
        




    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """
        #if the number of parameters is incorrect, print an error message and return False
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
    
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    

    def get_history(game,list_of_words,number_of_parameters):
        """allows to show up the previosu visited rooms 
        
        Args:
        
        game (Game): The game object.
        list_of_words (list): The list of words in the command.
        number_of_parameters (int): The number of parameters expected by the command.
           
        Returns:
            
        """
        player = game.player
        if player.history:
            print("\nPièces déjà visitées:\n")
            for i in player.history:
                print ("",i.name)
        return True
    
    