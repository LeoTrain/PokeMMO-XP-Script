NAME=srcs/main.py
PYTHON=python
SETUP=setup/setup.sh

all:
	. $(SETUP) && $(PYTHON) $(NAME)

clean:
	deactivate pokemmo_env
	rm -rf pokemmo_env
