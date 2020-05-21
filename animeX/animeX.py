import argparse

import animeX.utils as utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='anime downloader')
    parser.add_argument('--name', type=str, help='\nWhat anime do you wanna download today:::')
    parser.add_argument("--version", "-v", action="version", version="%(prog)s " + str(utils.get_version()), )
    args = parser.parse_args()

    print("\nAll anime are gotten from www.animeout.xyz/")

    anime_name = args.name
    search_result = utils.get_search_result(anime_name)
    print(args.name)

    print("\nSearch results for", anime_name)
    for i, j in enumerate(search_result):
        print(i + 1, " - " + j["name"])
    choice = int(input("\nWhich one? Enter the number of your choice::: "))

    anime = search_result[choice - 1]
    anime["name"] = "".join([i if i.isalnum() else "-" for i in anime["name"]])
    episodes = utils.get_anime_episodes(anime["url"])

    utils.make_directory(anime["name"])
    print("\nPress CTRL + C to cancel your download at any time")
    for i in episodes:
        download_url = utils.get_download_url(i)
        utils.download_episode(anime["name"], download_url)

    print("\nFinished downloading all episodes of", anime["name"])
