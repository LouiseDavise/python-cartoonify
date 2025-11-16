# Cartoonify Webcam (OpenCV)

A small fun project made to practice **Git workflow** while experimenting with **Python + OpenCV**.  
The program turns your webcam feed into a cartoon-style video in real time and lets you adjust the effect using sliders.

## Features
- Real-time cartoon effect
- Adjustable sliders (color smoothing, edge thickness, etc.)
- Side-by-side layout (original + cartoon)
- Save output with the `s` key
- Quit with the `q` key

## Project Purpose
This project was created mainly to:
1. Practice using Git and committing multiple versions.
2. Build a simple but fun OpenCV application.
3. Improve understanding of image processing and filters.

## Files Overview
### `cartoonify_1.py`
Basic version — webcam + edge detection only.

### `cartoonify_2.py`
Adds color smoothing and creates the first cartoon effect.

### `cartoonify_3.py`
Adds interactive trackbars so you can adjust all parameters live.

### `cartoonify_4.py`
Adds multi-panel display (original + cartoon + edges).

### `cartoonify_5.py`
Final version:
- Saves the combined image with `s`
- Full layout display
- All features combined

## Requirements
```
pip install opencv-python numpy
```

## Run
```
python cartoonify_5.py
```

Press:
- `q` to quit  
- `s` to save the output image

