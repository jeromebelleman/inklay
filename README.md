# NAME

inklay – Show layers and export PNGs or PDFs

# SYNOPSIS

inklay [--help] [-dryrun] *CFG* *INKSCAPE* *OUTDIR* [*LAYERSET* [*LAYERSET* ...]]

# CONFIG FILE

Inklay expects a config file looking like:

```
laysets:

    - foo: # Only show all layers called 'gazonk' and 'bop'
        - gazonk
        - bop

    - bar: # Only show all layers called 'bar'
      useprevious: # Use previous slide number (overlays)

    - baz: # Only show all layers called 'quux'
        - quux

cfg:
    format: png # Or pdf
    common:
        - fg
        - bg
    number: true # Number file names according to their ordering

    dpi: 300 # Only used for exporting PNGs (Inkscape default is 90)
    # width: 1024 # Overrides dpi option, only used for exporting PNGs

    # text-to-path: true # Only used for exporting PDFs
    # export-area-drawing: true # Only used for exporting PDFs, default is false
```

Inklay works on a temporary copy of the SVG file and leaves the
original untouched.  It first hides all layers. Then, for each layer
set (**foo**, **bar**, **baz**, here), it creates a file into *OUTDIR*
(e.g. *OUTDIR*/foo.pdf) with the corresponding layers (e.g. **gazonk**,
**bop**) shown.

Note that it shows all the layers with a matching name. Also, common layers
may be listed under **common** to be shown for all layer sets. E.g. **fg**
and **bg** will be shown for **foo**, **bar** and **baz**.

# SLIDE NUMBERS

If inklay finds the **$number** place holder in the Inkscape file,
it will replace it with the slide number.
