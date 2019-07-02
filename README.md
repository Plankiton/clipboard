# Clipboard tools

Copy and paste from clipboard of the system in your terminal.

## Copy

### With arguments

```sh
ctrlC "Thing to copy"

ctrlC 'Thing to copy'

ctrlC Thing to copy
```

### With pipe (`|`)

```sh
echo "
Thing
to
copy" | ctrlC

whois google.com | ctrlC

cat txt.txt| grep name | ctrlC
```

## Paste

```sh
ctrlV

echo "\"$(ctrlV)\" did pasted!"

ctrlV | grep VAR=
```
