from git import Repo
import time
import yaml

def get_modules_repo(moduel_name):
    """
        finds a modules repository address from repositories.json file
        and returns a Repo object for the repository
        @:param module's name
        @:return repository object for the module
    """
    bare = True
    if moduel_name == 'test':
        bare = False
    with open('./repositories.yaml') as file:
        repositories = yaml.load(file)
    repo_address = repositories[moduel_name]['repo']
    return Repo.init(repo_address, bare=bare)

def commits_stat(module_name):
    stats = {'commits':[]}
    repo = get_modules_repo(module_name)
    for commit in repo.head.commit.iter_parents():
        commit_dic={
            'hash':commit.hexsha,
            'lines':commit.stats.total,
            'time':time.strftime("%d %b %Y %H:%M", time.gmtime(commit.committed_date)),
            'commiter':commit.author.name,
            'email':commit.author.email
        }
        stats['commits'].append(commit_dic)
    return stats


if __name__ == '__main__':
    print commits_stat('test')