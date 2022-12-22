import os
import shutil


print(os.listdir())  # prints /absolute/path/to/{{cookiecutter.project_slug}}
print(".github")
print(os.listdir(".github/"))  # prints /absolute/path/to/{{cookiecutter.project_slug}}
print(".github/workflows")
print(
    os.listdir(".github/workflows")
)  # prints /absolute/path/to/{{cookiecutter.project_slug}}


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
    else:
        print(f"file not found: {filepath}")
        print(f"current files in: {os.listdir('.github/workflows')}")


if "{{cookiecutter.deploy_cloud}}" == "":
    remove_files = [
        ".github/workflows/github-actions-gcp.yaml",
        ".github/workflows/github-actions-aws.yaml",
        "aws.Dockerfile",
        "gcp-deploy.sh",
    ]

if "{{cookiecutter.deploy_cloud}}" == "aws":
    remove_files = [
        ".github/workflows/github-actions-gcp.yaml",
        ".github/workflows/github-actions.yaml",
        "gcp-deploy.sh",
    ]

if "{{cookiecutter.deploy_cloud}}" == "gcp":
    remove_files = [
        ".github/workflows/github-actions.yaml",
        ".github/workflows/github-actions-aws.yaml",
        "aws.Dockerfile",
    ]

for remove_file in remove_files:
    remove(os.path.join(os.getcwd(), remove_file))
