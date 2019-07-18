# niffi
Convenient scripts to wrap Niftools' PyFFI functionality. Works with Python 3.7.

## Install
Install Python 3.7 and make sure it is on your path.

Clone this repository recursively, making sure to also clone the PyFFI submodule:
```
> git clone --recurse-submodules https://github.com/Adam-Gleave/niffi
```
Do not separate the `niffi` scripts from PyFFI, it will not end well...

## Usage

Syntax for the texture replacer is as follows:

__File mode__ (modify textureset paths for one .nif file)
```
> python .\path\to\texture_replacer.py <pattern to replace> <replacement string> --file=\path\to\model.nif 
```

__Directory mode__ (modify textureset paths for all .nif files in a directory)
```
> python .\path\to\texture_replacer.py <pattern to replace> <replacement string> --dir=\path\to\nif_dir
```

## Examples
```
> python .\texturepath_replacer.py A:\SteamLibrary\steamapps\common\Skyrim\Data\Textures\ textures\ 
  --dir=C:\Users\example\Documents\nifs\

> python .\texturepath_replacer.py A:\SteamLibrary\steamapps\common\Skyrim\Data\Textures\ textures\ 
  --file=C:\Users\example\Documents\Nifs\example.nif
```
