import os
import subprocess
import sys
from time import sleep

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        print("Defaulting and making you wait because you're lazy smh")
        sleep(5)
        path = "/home/james/Documents/Programming/"
    except:
        raise

    for dir in os.listdir(path):
        try:
            os.chdir(path + dir)
            subprocess.call(["git", "commit", "-am", "automated commit :)"])
            print("")
            pwd = str(subprocess.check_output(["pwd"]))
            pwd = pwd.replace(path, "").replace("b'", "").replace("\\n'", "")
            psuz = input("\nPush " + str(pwd) + "?\n")
            if psuz == "y":
                subprocess.call(["git", "push"])
        except KeyboardInterrupt:
            quit = input("Quit? ")
            if quit != "n":
                exit()
            continue
        except:
            raise
