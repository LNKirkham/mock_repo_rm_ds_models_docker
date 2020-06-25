# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/louisekirkham/Documents/projects/data-science-models---docker")

# Your mock repo
mock_repo = git.Repo("/Users/louisekirkham/Documents/my_projects/mock_repo_rm_ds_models_docker")
importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['louisek@gmail.com', 'louise.kirkham@royalmail.com'])
print("kppcv")
print("vhuln")
