# Co-planar vectors resultant calculator

Calculate the resultant vector from the inputted co-planar vectors

## How to run

```shell
python main.py
```

## Accepted input types

- CSV
- Manual typing in

## Expected formats

- `magnitude` a constant unit, preferably N
- `direction` degrees from the vertical clockwise

### CSV

```csv
[magnitude],[direction]
```

## Example Output

```
Co-planar vectors resultant calculator
--------------------------------------

Choose input format:
  1. CSV
  2. Manual
Enter option number:
> 2

Enter new co-planar vector?
[Y/n]: y

Enter vector details:
--------------------------------------
magnitude: 28
direction (from the vertical): 90

Enter new co-planar vector?
[Y/n]: y

Enter vector details:
--------------------------------------
magnitude: 17
direction (from the vertical): 24

Enter new co-planar vector?
[Y/n]: n

resultant vector:
--------------------------------------
magnitude: 38.21273719858552
direction: 66.02010036417545
x: 34.914522932288605
y: 15.530272779924214
```

## License

Licensed under ```MIT License```