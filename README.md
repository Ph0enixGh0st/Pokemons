# Pokemons
Pokemon GO helper

![image](https://user-images.githubusercontent.com/108229516/203812625-b8078b29-4e29-421c-a44e-53fa4f19c3cb.png)

## What is it for?
Site's main goal is to help track pokemons for 'Pokemon GO' game.

Pokemons periodically appear and disappear on the map, therefpre any player could go and catch them to improve collection.
Several pokemons of one type can be shown on the map simultaneously.

Evolution feature is also implemented: thus Bulbasaur can evolve to Ivysaur and next to Venusaur.

## How to install
Using GitHub CLI:
```bash
gh repo clone Ph0enixGh0st/Pokemons
```

Or download and unpack ZIP file from GIT Hub repository: https://github.com/Ph0enixGh0st/Pokemons.git

# Environment Variables
Some project settings are taken from environment variables.
In order to run the server you will need to create a '.env' file next to your 'manage.py' and add following data to it:
```
DEBUG=True
SECRET_KEY=REPLACE_ME
```

# Prerequisites
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

After all requirements are met - run the server:
```
python3 manage.py runserver
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
