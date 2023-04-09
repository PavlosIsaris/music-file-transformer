# Music File Transformer
A simple python script that recursively searches for files and transforms them to mp3, using ffmpeg.

## About the app

This is a simple Python script that, given an audio file extensions, searches for files of this extensions and transforms them to .mp3

## Features

- Customizable extension filter (.wma, .ogg, .wav)
- Customizable output options (frequency, bitrate)

## Prerequisites

This application uses ffmpeg, in order to transform the audio files. Make sure that you have a running instance of ffmpeg in your machine, and that can be accessible globally using the `ffmpeg` command.

## Installation / Setup

Just clone the repository to your machine, and run the python script!

## Arguments explanation

`root` - **required**

Defines the root directory that will be scanned. All of the subdirectories of this root directory will be scanned recursively.

Example: `--root="C:\Users\Paul\MUSIC"`

<hr>

`extensions` - **optional**

Defines the extension of the files that will be transformed to mp3.
Should be given as a comma-separated string of extensions, **with the preceding dot (.)**. Default: `[".wma"]`

Example: `--extensions=.wma,.ogg,.wav`

<hr>

`keep` - **optional**

Whether or not the old file will be removed. Default: `1`.

Example: `--keep=1`

<hr>

`frequency` - **optional**

The desired output frequency, as integer (eg 44100 or 48000). Default: `44100`.

Example: `--frequency=48000`

<hr>

`bitrate` - **optional**

The desired output bitrate, as integer (eg 192 or 320). Default: `320`.

Example: `--bitrate=320`

<hr>

## Usage examples

```bash
python .\music-file-transformer.py --root="C:\Users\Paul\MUSIC" --extensions=.wma,.ogg --keep=0 --frequency=48000 --bitrate=320
```

## License

The Apache Licence. Please see the [Licence File](LICENCE.md) for more information.
