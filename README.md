# Inkscape CLI short actions
&emsp;Inkscape CLI combined short actions.

## Requirements
- [**Inkscape 1.1 or higher**](https://inkscape.org/release/)
- [**Python 3.9 or higher**](https://www.python.org/downloads/)

## Usage
&emsp;Clone this repository by the command below.

```git
git clone -b inkscape-cli-short-actions https://github.com/lunatic-fox/programs.git
```

> If you have a Python version under `3.11.0`, then use `python` instead of `py` in command line.

### Input and output
- `-i` - input path to SVG file.
- `-o` - output path to SVG file.

**Example**
```bash
py . -i src/img-i.svg -o out/img-o.svg
```
&emsp;In the example above `img-i.svg` is inside `src` folder and the processed SVG will be saved on `out` folder as `img-o.svg`.

## Actions
&emsp;It is possible to combine some actions.

**Example**
```bash
py . -i src/img-i.svg -o out/img-o.svg ungroup unify fitbox
```


### ungroup
&emsp;Ungroup all paths recursively.
```bash
py . -i src/img-i.svg -o out/img-o.svg ungroup
```

### unify
&emsp;Unify all paths.
```bash
py . -i src/img-i.svg -o out/img-o.svg unify
```

### center
&emsp;Align all paths as a group vertically and horizontally to the page.
```bash
py . -i src/img-i.svg -o out/img-o.svg center
```

### resize
&emsp;Resize all paths as a group to defined size.
```bash
py . -i src/img-i.svg -o out/img-o.svg resize=256
```

### fitBox
&emsp;Resize all paths as a group to fit the page size.
```bash
py . -i src/img-i.svg -o out/img-o.svg fitBox
```