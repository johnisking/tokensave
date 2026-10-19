---
name: html-canvas-games
description: Conventions for building small browser games as a single HTML file with a canvas. Use when asked to make a browser game, arcade game or canvas demo.
---

# Single-file HTML canvas games

Follow these conventions when you build a browser game in one HTML file.

## Structure
- One `index.html` with inline `<style>` and one inline `<script>`; no external libraries or assets.
- A single `<canvas>` sized with CSS to fit the window while keeping its aspect ratio; draw at a fixed logical resolution (for example 800x600) and scale.
- Keep the code in this order: constants, state, input, update, draw, game loop, start.

## Game loop
- Drive the loop with `requestAnimationFrame` and a delta time in seconds, clamped to 1/30 s so a background tab does not make objects jump.
- Keep `update(dt)` and `draw()` separate; never draw inside update.
- Use a small state machine: `title`, `playing`, `levelClear`, `gameOver`, `win`.

## Input
- Keyboard: arrow keys and A/D to move, Space or Enter to start, launch and restart. Track pressed keys in a set on `keydown`/`keyup` and call `preventDefault()` for the arrow keys and Space.
- Mouse: move the paddle or player with `mousemove` using the canvas bounding rectangle; click to start or launch.
- Touch: mirror the mouse handlers with `touchstart`/`touchmove` and `{ passive: false }`.

## Gameplay details
- Store levels as arrays of strings, one character per brick or tile, so a level is easy to read and edit.
- Show score, lives and level in a HUD drawn on the canvas.
- Give the player a short pause and a message between levels and after losing a life.
- Make collisions robust: move in small steps or resolve along the axis of least penetration so fast objects do not tunnel.

## Finish
- Check that the file opens without console errors and that every state can be reached.
- Keep the file under about 600 lines.
