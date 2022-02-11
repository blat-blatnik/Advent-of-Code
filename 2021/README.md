# 2021

These are my solutions for the [2021 Advent of Code](https://adventofcode.com/2021). Each problem was solved in python, and I tried to solve it in a generic way, so all of the solutions should work with any possible input for that day.

## How to run

```bash
$ python3 dayXX.py
# Replace XX by the number of the day you want to run.
```

There is one python file for every challange-day, which will read input from the correspondingly named `.txt` file. For example, `day4.py` will read input from `day4.txt`. If you want to use the solutions with your personal inputs, you can just replace the contents of the input file.

## Takeaways

This was my first year participating. This was really fun!

I tried completing each day as it appeared - but I didn't really have time always so sometimes I did 2 or 3 days worth of challenges at once. In the end I managed to complete each day by the 25th :)

[Day 23](./day23.md) was the hardest for me by far. I just hate it when there's many rules to a game like this. I forgot to implement some rules, then I interpretted them wrongly, then I implemented them wrongly.. It took me almost 8 hours to get it working. And it's the last day I finished in the end.

[Day 24](./day24.md) was strange. It was a reverse engineering puzzle or sorts, but I didn't want to solve it like that because I always tried to not look at the input at all and solve each day just based on what the instructions say. It turns out that it's possible to solve this day like that, but it takes an incredibly long time to run. I got sick of waiting for my python solution to finish (it takes more than 4 hours!) so I translated the code to C and it ran in only 5 minutes. This is the only day where I have both a python and a C solution.
