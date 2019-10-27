# Warnsdorff's Algorithm

<div align="center">
    <img src="./.github/visualizer.gif" alt="visualizer"/>
    <p align="center"><strong>Fig.1 Algorithm Visualization</strong></p>
</div>

## Build

```
$ pip install -r requirements.txt
```

## Intro

A **knight's tour** is a sequence of moves of a knight on a chessboard such that the knight visits every square only once. If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed, otherwise it is open.

We can solve the **knight's tour** problem using warnsdorff's algorithm, which states that:- 

- We can start from any initial position of the knight on the board.
- We can always move to an adjacent, unvisited square with minimal degree(minimum number of unvisited adjacent).

## Sample Run

`Fig.1` demonstrates a sample run of the visualizer when knight is placed at `0, 0`, you can find other samples [here]().

| Symbol                       | Meaning           |
|:----------------------------:|-------------------|
| <font color="black">0</font> | Unvisited Cell    | 
| <font color="green">1</font> | Visited Cell      |
| <font color="red">2</font>   | Knight's Position | 

## Fun Fact

On an *8 × 8 board*, there are exactly *26,534,728,821,064 directed closed tours* (i.e. two tours along the same path that travel in opposite directions are counted separately, as are rotations and reflections). The number of *undirected closed tours is half this number*, since every tour can be traced in reverse!

## Facing a Issue

If you are in this situation _first and foremost_ Don't panic :cry: I'm here to help you get over it. Simply click [this](https://github.com/muj-programmer/warnsdorff-algorithm-visualizer/issues) and properly state your issue (be as verbose as you can be), After that sit tight and watch :movie_camera: the movie you have been postponing for so long while I :construction_worker: fix the issue.

## Want to Contribute

I will be glad :smiley: to work with you on a new idea or fixing a invisible bug :bug: or if you have already done the work :hammer: just create a pull request and I will merge it asap.

Well that's all for now but before you close this browser tab hit the star :star: button (it motivates me to make new stuff).

Have a great day :sunglasses:.
