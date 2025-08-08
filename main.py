# main.py
from ffmpeg_streamer import launch_stream
import json

def print_available_platforms(platform_dict):
    s = []
    for platform in platform_dict.keys():
        s.append(platform)
    platforms = ", ".join(s)
    print("Available Platforms: ")
    print(platforms)

def get_number_of_platforms():
    num = input("Enter the number of platforms: ")
    return int(num)

def get_platform_names(number):
    plat_list = []
    for i in range(number):
        platform = input(f"Enter the Platform #{i+1} name: ")
        plat_list.append(platform)
    return plat_list

def get_platform_info(plat_list):
    platform_dict = {}
    for platform in plat_list:
        url = input(f"Enter the Platform URL for {platform}: ")
        streamkey = input(f"Enter the Streamkey for {platform}: ")
        platform_dict[platform] = {"url": url, "stream_key": streamkey}
    print(platform_dict)
    return platform_dict

def go_live(platform_dict):
    answer = input("Do you want to play live? (Y/N): ")
    if answer == "Y":
        launch_stream(platform_dict)
    else:
        print("Goodbye")

def add_new_platform(platform_dict):
    name = input("Enter the Platform name: ")
    url = input("Enter the Platform URL: ")
    stream_key = input(f"Enter the Streamkey for {name}: ")
    new_platform = {
        f"{name}": {
            "url": url,
            "stream_key": stream_key
        }
    }
    platform_dict.append(new_platform)
    with open("saved_platforms.json", "r+") as file:
        try:
            file.seek(0)
            json.dump(platform_dict, file, indect = 4)
            file.truncate()
        except json.JSONDecodeError:
            print("Invalid JSON format.")

def remove_platform(platform_dict):
    print_available_platforms(platform_dict)
    name = input("Enter the Platform name you wish to delete: ")
    del platform_dict[f"{name}"]

def load_file():
    with open('saved_platforms.json', 'r') as file:
        platform_info = json.load(file)
    return platform_info

def ask_user_action():
    print("Please confirm your next action.")
    print("1. Add Platform")
    print("2. Remove Platform")
    print("3. Edit Platform")
    print("4. Continue")
    print("5. Exit")
    action = input()
    return int(action)


if __name__ == "__main__":
    print("Welcome to Restream's CLI")
    saved_answer = input("Do you wish to load saved platforms? Press Y/N:")
    if saved_answer == "Y":
        platform_info = load_file()
        print_available_platforms(platform_info)
        action = ask_user_action()
        match action:
            case 1:
                add_new_platform(platform_info)
            case 2:
                remove_platform(platform_info)
            # case 3:
            #     edit_platform(platform_info)
            # case 4:
            #     continue
            # case 5:
            #     exit(0)



    # # print(platform_info["platforms"]["YouTube"].get("url"))
    # else:
    #     number_of_platforms = get_number_of_platforms()
    #     platform_names = get_platform_names(number_of_platforms)
    #     platform_info = get_platform_info(platform_names)
    # print("Starting restream service...")
    # go_live(platform_info)

# {'Youtube': {'url': 'abc', 'stream_key': 'zxy'}, 'Facebook': {'url': 'abc', 'stream_key': 'zxy'}}