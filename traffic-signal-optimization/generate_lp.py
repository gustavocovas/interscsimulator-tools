n = 13  # Number of signals
cycle_seconds = 150.0

# Red times for inbound and outbound streams.
# In the example below, all signals have the same red time
inbound_r_seconds = 13 * [cycle_seconds/2]
outbound_r_seconds = 13 * [cycle_seconds/2]

# Travel time between each node of inbound and outbound streams:
inbound_t_seconds = [
  9.36,
  8.64,
  22.32,
  9.72,
  12.96,
  20.16,
  14.76,
  14.40,
  18.00,
  15.84,
  8.28,
  21.60,
]
outbound_t_seconds = [
  9.36,
  8.64,
  22.32,
  9.72,
  12.96,
  20.16,
  14.76,
  14.40,
  18.00,
  15.84,
  8.28,
  21.60,
]

assert len(inbound_r_seconds) == n
assert len(outbound_r_seconds) == n
assert len(inbound_t_seconds) == n - 1
assert len(outbound_t_seconds) == n - 1

# Convert times to cycle units:
sec_to_cycle = lambda t: float(t)/cycle_seconds
r = list(map(sec_to_cycle, inbound_r_seconds))
rl = list(map(sec_to_cycle, outbound_r_seconds))

t = list(map(sec_to_cycle, inbound_t_seconds))
tl = list(map(sec_to_cycle, outbound_t_seconds))

# Print the input for lp_solve:
print('max: b;')
print('bl = b;')
for i in range(n):
  print(f'w{i} + b <= {1-r[i]};')

for i in range(n):
  print(f'wl{i} + bl <= {1-rl[i]};')

for i in range(n-1):
  print(f'w{i} + wl{i} - w{i+1} - wl{i+1} + {t[i]+tl[i]:.2f} = {-0.5*(r[i]+rl[i])+0.5*(r[i+1]+rl[i+1]):.2f} + m{i};')

print('b >= 0;')
print('bl >= 0;')
for i in range(n):
  print(f'w{i} >= 0;')
  print(f'wl{i} >= 0;')

integer_cons = 'int m0'
for i in range(1, n):
  integer_cons += f', m{i}'
integer_cons += ';'

print(integer_cons)
