import os

workspace = os.environ.get('GITHUB_WORKSPACE')
if not workspace:
    raise Exception('No workspace is set')

print("here")
print(workspace)
print(os.listdir(workspace))
os.system(f'cd {workspace} && ls -lA')