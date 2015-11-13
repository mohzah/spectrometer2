from git import Repo
import time
import yaml

class GitHandler:
    def __init__(self, moduel_name):
        self.repo = self.get_modules_repo(moduel_name)

    def get_modules_repo(self, moduel_name):
        """
            finds a modules repository address from repositories.json file
            and returns a Repo object for the repository
            @:param module's name
            @:return repository object for the module
        """
        bare = True
        # todo: remove test and bare
        if moduel_name == 'test':
            bare = False
        with open('./repositories.yaml') as file:
            repositories = yaml.load(file)
        repo_address = repositories[moduel_name]['repo']
        return Repo.init(repo_address, bare=bare)

    def get_commits_stat(self):
        stats = {'commits':[]}
        for commit in self.repo.head.commit.iter_parents():
            commit_dic={
                'hash':commit.hexsha,
                'lines':commit.stats.total,
                'time':time.strftime("%d %b %Y %H:%M", time.gmtime(commit.committed_date)),
                'commiter':commit.author.name,
                'email':commit.author.email
            }
            stats['commits'].append(commit_dic)
        return stats
