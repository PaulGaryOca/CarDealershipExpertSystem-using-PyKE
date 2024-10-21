import os
import shutil
import sys
import time  # Import time for delay

# Adding the path to Pyke to the system path
sys.path.append(r"C:\Users\Mangoda\Downloads\pyke3")

from pyke import knowledge_engine, krb_traceback

def run_engine():
    # Path to the directory you want to remove
    folder_path = r'C:\Users\Mangoda\Downloads\pyke3\ess\compiled_krb'

    # Check if the directory exists and is not empty
    if os.path.exists(folder_path) and os.listdir(folder_path):
        # If the directory is not empty, remove its contents
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error while deleting {file_path}: {e}")

    # Print the directory from where the engine is loading files
    print(f"Loading KB from: {__file__}")

    engine = knowledge_engine.engine(__file__)

    engine.reset()

    print("Activating knowledge base...")
    engine.activate('fc_rules')

    print("Proving goal...")
    advice_list = []  # Initialize an empty list to store the advice
    try:
        with engine.prove_goal('fc_rules.car_dealership_advice($advice)') as gen:
            found = False
            for vars, plan in gen:
                advice_list.append(str(vars['advice']))  # Convert advice to string and append to the list
                found = True
            if not found:
                print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        krb_traceback.print_exc()
        sys.exit(1)

    # Print the collected advice list
    if advice_list:
        print("\nYou should buy a/an:")
        for advice in advice_list:
            print(advice)
    else:
        print("No car available.")

while True:
    run_engine()
    try_again = input("Do you want to try again? (y/n): ").strip().lower()
    if try_again != 'y':
        break

# Path to the directory you want to remove
folder_path = r'C:\Users\Mangoda\Downloads\pyke3\ess\compiled_krb'

# Remove the folder and all its contents
try:
    shutil.rmtree(folder_path)
    # print("Folder and all its contents removed successfully")
except Exception as error:
    print(f"Error: {error}")

print("Thank you for using the car dealership expert system!")
