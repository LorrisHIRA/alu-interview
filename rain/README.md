# Rain

## Description

This project solves the classic **Rainwater Trapping** problem. Given a list of non-negative integers representing wall heights, it calculates how many square units of water will be retained after it rains.

## Requirements

- Python 3 (version 3.4.3)
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)
- No module imports allowed

## File Structure

| File | Description |
|------|-------------|
| `0-rain.py` | Function that calculates total rainwater retained |
| `README.md` | Project documentation |

## Function Prototype

```python
def rain(walls)
```

### Parameters
- `walls` — a list of non-negative integers representing wall heights (unit width = 1)

### Returns
- An integer representing the total square units of rainwater retained
- Returns `0` if the list is empty

### Notes
- The ends of the list are not considered walls and will not retain water

## Algorithm

The solution uses a **two-pass approach**:

1. **Left pass** — for each position, record the tallest wall to its left (including itself)
2. **Right pass** — for each position, record the tallest wall to its right (including itself)
3. **Water calculation** — water at each position = `min(left_max, right_max) - wall_height`

**Time complexity:** O(n)  
**Space complexity:** O(n)

## Example Usage

```python
#!/usr/bin/python3
rain = __import__('0-rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
```

## Visual Example

For `[0, 1, 0, 2, 0, 3, 0, 4]`:

```
        #
      # #
    # # #
  # # # #
0 1 0 2 0 3 0 4

Water retained: 1 + 2 + 3 = 6 units
```

For `[2, 0, 0, 4, 0, 0, 1, 0]`:

```
      #
#     #
#     #   #
#  #  # # #
2 0 0 4 0 0 1 0

Water retained: 2 + 2 + 2 = 6 units
```

## Repository

- **GitHub repository:** `alu-interview`
- **Directory:** `rain`
- **File:** `0-rain.py`

## Author

Hira