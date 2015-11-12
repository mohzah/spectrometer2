from git import Repo
import time

def get_modules_repo(moduel_name):
    """
        finds a modules repository address from repositories.json file
        and returns a Repo object for the repository
        @:param module's name
        @:return repository object for the module
    """
    bare = True
    if moduel_name == 'test':
        # directed to a git repository on the machine
        repo_address = './.'
        bare = False
    return Repo.init(repo_address, bare=bare)

stats = []
def commits_stat(module_name):
    repo = get_modules_repo(module_name)
    for commit in repo.head.commit.iter_parents():
        commit_dic={
            'lines':commit.stats.total,
            'time':time.strftime("%d %b %Y %H:%M", time.gmtime(commit.committed_date)),
            'commiter':commit.author.name,
            'email':commit.author.email
        }
        stats.append(commit_dic)
    return stats


if __name__ == '__main__':
    print commits_stat('test')