# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo('/Users/louisekirkham/Documents/Projects/data-science-models---docker')

# Your mock repo
mock_repo = git.Repo('/Users/louisekirkham/Documents/Projects/github_mock_repos/mock_repo_rm_ds_models_docker', search_parent_directories=True)

importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
print("prpme")
