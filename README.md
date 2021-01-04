# instructions for macos

## Introduction

When setting up 2FA codes some websites only show you the QR code and don't show you the secret key text that's very useful for backup purposes.

These scripts let you decode those QR codes from your clipboard. (use macos shortcut - shift+cmd+4) and generate a QR code from an otpauth url for convenience.

![alt text](https://support.apple.com/library/content/dam/edam/applecare/images/en_US/accessories/Keyboards/mac-key-combo-diagram-shift-command-4.png "shift cmd 4")

NB: https://github.com/google/google-authenticator/wiki/Key-Uri-Format

```
brew install pipenv
brew install libjpeg
brew install zbar
```

## Launch the virtualenv

`pipenv shell`

## How to run

Create an alias in your .zshrc file

`alias prp='pipenv run python'`

then run:

`pipenv shell`

`prp generate-qr.py # then paste the otpauth url`
`pipenv run python generate-qr.py # if you don't want to use the alias`
