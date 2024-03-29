# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Trello

This app uses the Trello API to manage to-do items. You'll need to sign up for a Trello account and generate an app key and token by following the instructions [here](https://trello.com/app-key). Then, create a board to store your to-do items in. There should be three columns: To Do, Doing, and Done. You'll need to add the app key and token and the board ID to your `.env` file.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Running the app in a VM

You can provision a VM from an Ansible Control Node and run the app that way. To do so:

- SSH into the control node, i.e. `ssh ec2-user@35.177.122.252`
- Make sure you're in the `ansible` directory, i.e. `cd ansible`
- Run `ansible-playbook playbook.yml -i inventory.ini`

The app should now be running on the managed node - go to `http://:35.177.223.76:5000`!

### Running the app in Docker

You can build and run development and production containers in Docker. 

To build the development container, run
`docker build --target development --tag todo-app:dev .`
and then run
`docker run --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev`
to run it.

If you visit https://localhost:5000 in your browser, the app should be running, and if you make changes to your app code it should reload the app (hot reloading!).

For the production container, first run
`docker build --target production --tag todo-app:prod .`
and then
`docker run --env-file .env -p 5000:8000 todo-app:prod`.
As before, you should see the app running at https://localhost:5000, but it won't have any hot reloading.

## Tests

To add new tests, create a file in the `tests` folder and make sure it starts with `test_` or it won't be picked up. Similarly, make sure all test methods defined in the file are named such that they start with `test_`.

### Running the tests

Making sure all the dependencies have been installed, run `poetry run pytest` to run all the tests. Alternatively, click the canonical flask icon in the lefthand bar of VS Code to open the Testing tab and run them from here. 

### Running the tests in Docker

You can run the tests in Docker by first running
`docker build --target test --tag test-image .`
followed by
`docker run test-image`

### Running specific tests

You can run:

- tests within a module by running `poetry run pytest <directory>/<filename.py>`, e.g. `poetry run pytest tests/test_view_model.py`
- tests within a directory by running `poetry run pytest <directory>` e.g. `poetry run pytest tests`
- a specific test within a module by running `poetry run pytest <module>::<method>` e.g. `poetry run pytest tests/test_view_model.py::test_view_model_to_do_items_returns_to_do_items`

You can also do all of the above through the Testing tab by hovering over the test/module/directory you want to run and clicking the play 'Run Test' button.

## Deploying the app

The app is hosted at `https://emipat-todoapp.azurewebsites.net/`. To update the site with any code changes:

1. Log into DockerHub locally by running `docker login` and entering your credentials when prompted. Make sure to have Docker desktop running or you will get an error about not being able to locate the Docker daemon!
2. Build the image by running `docker build --target production --tag <image_tag>` where `<image_tag>` is of the format `<username>/<image name>:<tag>`, e.g. `docker build --target production --tag emilypatsko/todo-app:module8`.
3. Push the image to DockerHub by running `docker push <image_tag>`. You can view the image [here](https://hub.docker.com/layers/emilypatsko/todo-app/module8/images/sha256-086b70f33e6f241e2278b1c7e9cd5035c6bd207c7c8a6fa9f71fe1a0559d77c1?context=repo).
4. Go the the app service's page in the Azure portal and go to _Deployment Center_. Locate and copy the webhook URL. 
5. Run `curl -dH -X POST <webhook>` to restart the app and pull the latest version of the container image. **Make sure to escape the `$` with a backslash!**