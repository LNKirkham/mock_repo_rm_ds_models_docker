# SEE: https://danielnmai.medium.com/import-contributions-from-bitbucket-to-github-afd9160eaf6d

# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo('/Users/louisekirkham/Documents/Projects/data-science-models---docker')

# Your mock repo
mock_repo = git.Repo('/Users/louisekirkham/Documents/Projects/github_mock_repos/mock_repo_rm_ds_models_docker')

importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['louisek@gmail.com', 'louise.kirkham@royalmail.com'])

importer.import_repository()
