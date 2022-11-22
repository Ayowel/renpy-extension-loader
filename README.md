# Ren'Py Extension Loader

[![Itch link](https://img.shields.io/static/v1?label=store&message=itch.io&color=blueviolet)](https://ayowel.itch.io/renpy-extension-loader)
[![Release status](https://img.shields.io/github/workflow/status/ayowel/renpy-extension-loader/Release?label=release)](https://github.com/Ayowel/renpy-extension-loader/actions/workflows/release.yml)
[![Release version](https://img.shields.io/github/v/release/ayowel/renpy-extension-loader)](https://github.com/Ayowel/renpy-extension-loader/releases/latest)
[![License](https://img.shields.io/github/license/ayowel/renpy-extension-loader)](LICENSE)

This extension loads other Ren'Py extensions with a stable load order. This is usefull when using multiple extensions that rely on other extensions in Ren'Py versions older than 7.5.3/8.0.3.

Extension files must be in the right subdirectory to be loaded.

## Usage

* Copy a released `extension_loader.rpe` file into the Ren'Py game's `game` folder.
* Create a `game/extensions` subdirectory
* Add all extensions except `extension_loader.rpe` in the new directory (subdirectories may be created to ease sorting)
* At game start, the extensions will be loaded based on their names
