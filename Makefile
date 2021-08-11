.PHONY: build

build:
	rm -rf dist
	pyinstaller main.py --onefile --noconsole
