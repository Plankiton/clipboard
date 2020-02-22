# Clipboard

A utility for copy and paste using the terminal.

Copying text:

```sh
$ echo "this text will be copied."| clip
this text will be copied.
```

```sh
$ clip "this text will be copied."
this text will be copied.
```

Pasting text:

```sh
$ clip paste
this text did paste.
```

For more informations type `clip -h` on terminal

## Installing

First run this command to add the requirements of project:
> You need of `pip` on your computer for install the requeriments

```sh
$ wget -O- https://raw.githubusercontent.com/RoboCopGay/clipboard/master/requirements.txt | xargs pip --user install
```

After is just run this command to install the clip:

```sh
$ [[ -e "$HOME/.local/bin" ]] || mkdir -p "$HOME/.local/bin" && wget -c "https://raw.githubusercontent.com/RoboCopGay/clipboard/master/clip" && chmod +x clip && mv clip "$HOME/.local/bin/"
```

Verify if `$HOME/.local/bin` are on `$PATH` environment variable.
