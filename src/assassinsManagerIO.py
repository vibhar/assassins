import os
from cmd import Cmd
from assassinsManager import AssassinsManager

class AssassinsManagerCmdInterpreter(Cmd):

    assassins_manager = AssassinsManager()

    # This file controls the I/O for users to execute commands

    def do_add(self, args):
        """$add <assassin name> adds assassin to the game"""
        argument_list = args.split()
        if len(argument_list) < 1:
            self.__bad_arguments("add")
        else:
            print "Added " + args + "."
            AssassinsManager.add_assassin(self.assassins_manager, args.split()[0])
    
    def do_create_graph(self, args):
        """$create_graph > randomizes the list and creates the kill graph"""
        if (len(args.split()) > 0):
            self.__bad_arguments("create_graph")
        else:
            AssassinsManager.create_graph(self.assassins_manager)

    def do_kill(self, args):
        """$kill <assassin> use this command when an assassin died"""
        if (len(args.split()) < 1):
            self.__bad_arguments("kill")
        else:
            print "Killed " + args + "."
            player_killed = args.split()[0]
            AssassinsManager.remove_assassin(self.assassins_manager, player_killed)

    def do_get_target_for(self, args):
        """$get_target_for <assassin> > Prints out target name and kill word"""
        if (len(args.split()) < 1):
            self.__bad_arguments("get_target_for")
        else:
            AssassinsManager.get_target(self.assassins_manager, args.split()[0])

    # Comment out this capability in a real game
    # def do_graph(self, args):
    #     """$graph > Prints out target and source graphs"""
    #     if (len(args.split()) > 0):
    #         self.__bad_arguments("graph")
    #     else:
    #         AssassinsManager.print_target_graph(self.assassins_manager)
    #         AssassinsManager.print_source_graph(self.assassins_manager)

    def do_kill_counter(self, args):
        """$kill_couter > Prints out the kill count for each player"""
        if (len(args.split()) > 0):
            self.__bad_arguments("kill_counter")
        else:
            AssassinsManager.print_kill_count(self.assassins_manager)

    def do_clear(self, args):
        """$clear > Clears the screen so your opponents don't know your target"""
        if (len(args.split()) > 0):
            self.__bad_arguments("clear")
        else:
            os.system('clear')

    def do_end(self, args):
        """Stops the program."""
        print "END GAME"
        raise SystemExit

    def __bad_arguments(self, topic):
        print ("Sorry, your input is incorrect, please use 'help <" + topic + ">' to see how this command is used")