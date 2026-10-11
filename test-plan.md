# Test Plan - CargoLink Docker Lab

All tests run only inside this local lab.

## Tests

| # | Test | Steps | Expected Result |
|---|------|-------|-----------------|
| 1 | Container builds | Run `docker compose up --build` | Build finishes with no errors |
| 2 | App is reachable | Open http://localhost:5000 | Page loads |
| 3 | Data displays | Check the table on the page | All 10 assets show with 6 columns |
| 4 | Lab stops cleanly | Run `docker compose down` | Containers stop and are removed |
| 5 | Lab resets | Run `docker compose down -v` then `docker compose up --build` | Lab rebuilds and the page loads again |

## Results

- Tests 1-3: passed on October 9, 2026
- Tests 4-5: passed on October 11,2026
