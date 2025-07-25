NAME=srcs/main.py
PYTHON=python
SETUP=setup/setup.sh

all:
	. $(SETUP) && $(PYTHON) $(NAME)

clean:
	rm -rf env
