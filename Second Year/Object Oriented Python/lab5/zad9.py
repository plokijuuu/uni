import random
import math


def estimate_pi(seed=None, batch=1):
    if seed is not None:
        random.seed(seed)

    inside = 0
    total = 0

    while True:
        for _ in range(batch):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            total += 1
            if x * x + y * y <= 1:
                inside += 1

        yield 4 * inside / total

gen = estimate_pi(seed=123, batch=1000)
for _ in range(5):
    print(next(gen))

def run_until_pi(eps, seed=None, batch=1000):
    gen = estimate_pi(seed=seed, batch=batch)
    total_samples = 0

    for pi_hat in gen:
        total_samples += batch
        if abs(pi_hat - math.pi) < eps:
            return pi_hat, total_samples

pi_est, samples = run_until_pi(1e-4, seed=42, batch=5000)
print(pi_est, samples)
