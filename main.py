
from github import Github
ACCESS_TOKEN = 'da92ec3fca51bc602d252f67ed15a94ca5d519ed '
g = Github(ACCESS_TOKEN)
filePath = 'fileappnew.csv'
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# def search_github(keyword):
#     rate_limit = g.get_rate_limit()
#     rate = rate_limit.search
#     if rate.remaining == 0:
#         print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
#         return
#     else:
#         print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
#
#     query = f'"{keyword} english" in:repo  extension:xml'
#     result = g.search_repositories()
#
#     max_size = 100
#     print(f'Found {result.totalCount} file(s)')
#     if result.totalCount > max_size:
#         result = result[:max_size]
#
#     for file in result:
#         print(f'{file.download_url}')


# Press the green button in the gutter to run the script. keyctl-unmask
if __name__ == '__main__':
    # repositories = g.search_code(query =('AndroidManifest.xml path:hellisfull/MyAppPicaso/tree/master/app/src/main user:hellisfull')
    # repositories = g.search_code('AndroidManifest in:path user:hellisfull extension:xml')
    # repos = g.get_user('dguenms').get_repos()
    # print(repositories.totalCount)
    # if repositories.totalCount > 0:
    #     a = open(filePath, 'w')
    #     for repo in repositories:
    #         a.write(repo.url+'\n')
    #         print(repo.repository)
            # print(repo.path)
    listone = [1, 2, 3]
    listtwo = [4, 5, 6]


joinedlist = listone + listtwo

print(joinedlist)
