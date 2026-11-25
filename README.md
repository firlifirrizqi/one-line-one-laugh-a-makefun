# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/firlifirrizqi/one-line-one-laugh-a-makefun/rank.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/firlifirrizqi/one-line-one-laugh-a-makefun/reward.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

A single funny line for the [One Line, One Laugh](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a) bounty on make.fun.

## The line

> I proved I'm not a robot by clicking every traffic light, and now the robots think I'm one of them.

99 characters, one line, self-contained. The CAPTCHA exists to prove you are
human — the twist is that passing it so thoroughly makes the robots claim you
as one of their own.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`, then verifies it against the competition gate: UTF-8,
1–140 characters, not only whitespace, single line, and byte-identical on
read-back.

```sh
python3 main.py
```
