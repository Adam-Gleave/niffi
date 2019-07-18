# niffi
Convenient scripts to wrap Niftools' PyFFI functionality

## Install
Clone this repository recursively, making sure to also clone the PyFFI submodule:
```
> git clone --recurse-submodules https://github.com/Adam-Gleave/niffi
```
Do not separate the `niffi` scripts from PyFFI, it will not end well...

## Usage

Syntax for the texture replacer is as follows:

__File mode__ (modify textureset paths for one .nif file)
```
> .\path\to\texture_replacer.py <pattern to replace> <replacement string> --file=\path\to\random_model.nif 
```

__Directory mode__ (modify textureset paths for all .nif files in a directory)
```
> .\path\to\texture_replacer.py <pattern to replace> <replacement string> --dir=\path\to\nif_directory
```
