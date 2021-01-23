import os
import subprocess
import sys
from time import sleep

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        print("Defaulting and making you wait because you're lazy smh")
        sleep(2)
        path = "/home/james/Documents/Programming/"
    except:
        raise

    print("Pulling all directories first.\n")
    for dir in os.listdir(path):
        os.chdir(path + dir)
        pwd = str(subprocess.check_output(["pwd"]))
        pwd = pwd.replace(path, "").replace("b'", "").replace("\\n'", "")
        print("\nPulling " + str(pwd))
        subprocess.call(["git", "pull"])

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
