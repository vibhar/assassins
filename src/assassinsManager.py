import random

class AssassinsManager():

    assassins = [] # List of assassins
    assassins_target_graph = {} # A : (B, C) => A has Target B, word C
    assassins_source_graph = {} # A : B => Target B's Assassin is A
    dictionary = [] # dictionary
    kill_counter = {} # A : n => A has n kills

    # Adds an assassin to the game
    # Input: (STR)
    def add_assassin(self, assassin):
        if (self.assassins.__contains__(assassin)):
            print "Assassin already exists in the list"
        else:
            self.assassins.append(assassin)
        return None


    def __addKillCounter(self):
        return dict((self.__mapToDict(a), a) for a in self.assassins)
    
    def __mapToDict(self, a):
        self.kill_counter[a] = 0

    # Creates assassins graph
    # No input
    def create_graph(self):
        # Randomize list
        random.shuffle(self.assassins) 

        # Load dictionary
        self.dictionary = [line.rstrip() for line in open('words.txt')]

        # Create kill counter
        self.__addKillCounter()

        # Draw dependency line from 0->1, 1->2,... n-1->0
        if (len(self.assassins) < 2):  
            print "You need at least two players"
        else:
            i = 0
            while i < (len(self.assassins) - 1):             
                randomWordIndex = random.randint(0, len(self.dictionary) - 1)
                self.assassins_target_graph[self.assassins[i]] = (self.assassins[i+1], self.dictionary[randomWordIndex])
                self.assassins_source_graph[self.assassins[i+1]] = self.assassins[i]
                self.dictionary.remove(self.dictionary[randomWordIndex])
                i += 1
            randomWordIndex2 = random.randint(0, len(self.dictionary) - 1)
            self.assassins_target_graph[self.assassins[i]] = (self.assassins[0], self.dictionary[randomWordIndex2])
            self.assassins_source_graph[self.assassins[0]] = self.assassins[i]
            self.dictionary.remove(self.dictionary[randomWordIndex2])
            print "Created graph."
        return None
    
    # Removes deleted assassin from the assassin graph
    # Input: (STR)
    def remove_assassin(self, assassin):
        if self.assassins_target_graph.has_key(assassin):
            assassinTargetTuple = self.assassins_target_graph[assassin]
            killer = self.assassins_source_graph[assassin]

            self.assassins_target_graph[killer] = assassinTargetTuple
            self.assassins_source_graph[assassinTargetTuple[0]] = killer
            del self.assassins_target_graph[assassin]
            del self.assassins_source_graph[assassin]

            if (len(self.assassins_target_graph) == 1):
                print killer + ": YOU ARE THE WINNER!!"
            else:
                self.kill_counter[killer] += 1
                print killer + ": Nice! We recorded your kill, now type `$get_target_for " + killer + "` to see your next target."
        else :
            print "Doesn't seem like you're playing this round"
        return None
        
    # Prints out the target and kill word for a given assassin
    # INPUT: (STR)
    def get_target(self, assassin):
        if self.assassins_target_graph.has_key(assassin):
            print "Target: " + self.assassins_target_graph[assassin][0]
            print "Kill Word: " + self.assassins_target_graph[assassin][1]
            print "Finished reading your target? Type `$clear`"
        else :
            print "Doesn't seem like you're playing this round"
        return None

    # Prints out the assassin:target graph
    def print_target_graph(self):
        print self.assassins_target_graph
    
    # Prints out the target:assassin graph
    def print_source_graph(self):
        print self.assassins_source_graph

    # Prints out the kill counts for each person
    def print_kill_count(self):
        print self.kill_counter
