Traffic signal optimization
===

`generate_lp.py`: Script that generates a input file for [lp_solve](http://web.mit.edu/lpsolve/doc/) to optimize a set of traffic signals on an arterial way, as presented in [MAXBAND: A Program for Setting Signals on Arteries and Triangular Networks](https://www.researchgate.net/publication/5175552_MAXBAND_A_Program_for_Setting_Signals_on_Arteries_and_Triangular_Networks).

The notation is the same as the paper linked above, with the `l` in the variable names (as in `bl`) marking that the variable is related to the outbound stream.
After editing the number of signals, cycle time, inbound and outbound red times, and inbound and outbound travel times, run with:
```
python3 generate_lp.py
```
