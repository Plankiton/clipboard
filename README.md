# Clip Ultil

A ultility for copy and paste using the terminal.

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

Run the nexts commands on a terminal:

```sh
$ [[ -e "$HOME/.local/bin" ]] || mkdir -p "$HOME/.local/bin" && wget -c "https://raw.githubusercontent.com/RoboCopGay/clipboard/master/clip" && chmod +x clip && mv clip "$HOME/.local/bin/"
```

Verify if `$HOME/.local/bin` are on `$PATH` environment variable.
