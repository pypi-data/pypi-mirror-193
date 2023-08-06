import os
import shutil
import string
from pathlib import Path

import requests
import typer
from InquirerPy import inquirer
from tomlkit import dumps, parse

app = typer.Typer()

SUCCESS = typer.style("Success:", fg=typer.colors.GREEN)
FAIL = typer.style("Failed:", fg=typer.colors.RED)
BASE_PATH = Path(__file__).parent


def get_package_version(package_name):
    try:
        response = requests.get(f"https://pypi.python.org/pypi/{package_name}/json")
        data = response.json()
        return data["info"]["version"]
    except Exception as e:
        print(e)
        return "*"


@app.command()
def createproject():
    name = inquirer.text("Project Name:").execute()
    version = inquirer.text("Enter Version:", default="0.0.1").execute()
    database = inquirer.select(
        message="Choose an ORM:",
        choices=["SQLAlchemy", "Tortoise ORM", "Custom"],
    ).execute()
    project_templatetree = os.path.join(BASE_PATH, "template/project_name")
    project_destination = os.path.join(os.getcwd(), name)

    if os.path.exists(project_destination):
        typer.echo(
            f"{FAIL} {typer.style('Project already exist!', fg=typer.colors.RED)}"
        )
        return

    shutil.copytree(project_templatetree, project_destination)

    with open(os.path.join(project_destination, "pyproject.toml")) as f:
        data = parse(f.read())

    data["tool"]["poetry"]["name"] = name
    data["tool"]["poetry"]["version"] = version

    data["tool"]["poetry"]["dependencies"]["fastapi"] = get_package_version("fastapi")
    data["tool"]["poetry"]["dependencies"]["tzdata"] = get_package_version("tzdata")
    data["tool"]["poetry"]["dependencies"]["pytz"] = get_package_version("pytz")
    data["tool"]["poetry"]["dependencies"]["fastapi-mail"] = get_package_version(
        "fastapi-mail"
    )
    data["tool"]["poetry"]["dependencies"]["passlib"]["version"] = get_package_version(
        "passlib"
    )
    data["tool"]["poetry"]["dependencies"]["asgiref"] = get_package_version("asgiref")
    data["tool"]["poetry"]["dependencies"]["uvicorn"] = get_package_version("uvicorn")
    data["tool"]["poetry"]["dependencies"]["python-jose"] = get_package_version(
        "python-jose"
    )

    data["tool"]["poetry"]["group"]["dev"]["dependencies"][
        "black"
    ] = get_package_version("black")
    data["tool"]["poetry"]["group"]["dev"]["dependencies"][
        "isort"
    ] = get_package_version("isort")
    data["tool"]["poetry"]["group"]["dev"]["dependencies"][
        "pytest"
    ] = get_package_version("pytest")
    data["tool"]["poetry"]["group"]["dev"]["dependencies"][
        "httpx"
    ] = get_package_version("httpx")

    base_database_template = os.path.join(BASE_PATH, "template/database")
    match database:
        case "SQLAlchemy":
            shutil.copyfile(
                os.path.join(base_database_template, "register_db_sqlalchemy.py"),
                os.path.join(project_destination, "backend/register_db.py"),
            )
            data["tool"]["poetry"]["dependencies"]["sqlalchemy"] = get_package_version(
                "sqlalchemy"
            )
            print("SQLAlchemy as Database ORM")
        case "Tortoise ORM":
            shutil.copyfile(
                os.path.join(base_database_template, "register_db_tortoise.py"),
                os.path.join(project_destination, "backend/register_db.py"),
            )
            data["tool"]["poetry"]["dependencies"][
                "tortoise-orm"
            ] = get_package_version("tortoise-orm")
            print("Tortoise ORM as Database ORM")
        case "Pony":
            print("Pony not Supported yet")
        case "Piccolo ORM":
            print("Piccolo ORM Not Supported yet")
        case "Custom":
            shutil.copyfile(
                os.path.join(base_database_template, "register_db.py"),
                os.path.join(project_destination, "backend/register_db.py"),
            )
            print("An empty register_db.py file was created.")

    with open(os.path.join(project_destination, "pyproject.toml"), "w") as f:
        f.write(dumps(data))


@app.command()
def createapp():
    name = inquirer.text("App Name:").execute()
    app_templatetree = os.path.join(BASE_PATH, "template/app_name")
    app_destination = os.path.join(os.getcwd(), name)

    if os.path.exists(app_destination):
        typer.echo(f"{FAIL} {typer.style('App already exist!', fg=typer.colors.RED)}")
        return

    shutil.copytree(app_templatetree, app_destination)

    if os.path.exists(app_destination):
        for root, dirs, files in os.walk(app_destination):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    template = string.Template(f.read())
                with open(file_path, "w") as f:
                    f.write(template.substitute(name=name))
        typer.echo(f"{SUCCESS}: {name} created.")


@app.command()
def runserver(port: int = 3000, reload: bool = True):
    _run = os.path.join(os.getcwd(), "manage.py")

    if not os.path.exists(_run):
        typer.echo(f"{FAIL} {typer.style('No main.py found!', fg=typer.colors.RED)}")
        return


if __name__ == "__main__":
    app()
