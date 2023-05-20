import os


def deleteXmlFiles(args):
    """Delete XML file gotten from my camera"""

    if len(args) < 3:
        print("Directory argument expected")
        exit(1)

    directory = args[2]


    print(f'\nDeleting .XML files in {directory}')
    user_response = input("Are you sure? 🤔 (y/n): ")

    if user_response == '' or user_response == 'n':
        print('Aborting operation 😶')
        return
    
    for file in os.listdir(directory):
        if file.endswith(".XML"):
            filepath = f'{directory}/{file}'
            os.remove(filepath)

    print(f'\nSuccessfully Deleted! 🤝')
