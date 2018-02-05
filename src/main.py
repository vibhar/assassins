from assassinsManagerIO import AssassinsManagerCmdInterpreter 

def main():
    prompt = AssassinsManagerCmdInterpreter()
    prompt.prompt = '> '
    prompt.cmdloop("Start Playing Assassins... type 'help' for documentation")

if __name__ == '__main__': main()