# Expense Tracker (Python)

A small terminal program for keeping track of income and expenses. Everything is saved in a CSV file, so your transactions are still there the next time you open it.

This was my first project where I used file handling in Python, so I kept it simple and used only the standard library.

## Features

- Add income or expenses with a description, amount and date
- View all transactions in a table (sorted by date)
- Summary of total income, total expenses and remaining balance
- Shows your biggest expense and warns you if you spent more than you earned
- Checks input: bad menu choices, text instead of numbers, negative amounts and wrong dates are all rejected
- Data is saved in `transactions_anu.csv` after every new transaction

## How to run

You need Python 3 (no extra libraries, so there is no `requirements.txt`).

```
cd expense-tracker-python-anu
python expense_tracker_anu.py
```

On Mac/Linux you might need to type `python3` instead of `python`.

The folder comes with a few sample transactions in `transactions_anu.csv`. Delete the file if you want to start with an empty tracker, the program will make a new one.

## Menu

```
1. Add transaction
2. View all transactions
3. Show summary
4. Exit
```

## Example output

Option 2:

```
No.  Date        Type     Description                Amount
------------------------------------------------------------
1    2026-11-01  income   Part-time job pay          420.00
2    2026-11-02  expense  Rent share                 250.00
3    2026-11-03  expense  Groceries                   48.75
4    2026-11-05  expense  Bus pass                    30.00
5    2026-11-08  income   Tutoring                    60.00
6    2026-11-10  expense  Textbook                    64.99
7    2026-11-12  expense  Pizza with friends          18.50
```

Option 3:

```
Total income:   $480.00
Total expenses: $412.24
Balance:        $67.76
Biggest expense: Rent share ($250.00)
```

## Project files

```
expense-tracker-python-anu/
├── expense_tracker_anu.py   # the program
├── transactions_anu.csv     # saved data (sample data included)
└── README_anu.md
```

## What I learned

- How to read and write CSV files with the `csv` module
- Why user input needs checking. If the program just called `float()` on whatever was typed, a letter would crash it, so I used loops that keep asking until the input is valid
- Splitting the program into small functions makes it much easier to fix one thing without breaking the rest
- Storing each transaction as a dictionary was easier to work with than a list of lists
- Dates in `YYYY-MM-DD` format sort correctly as plain text, so I didn't need anything fancy to sort them

## Possible improvements

- Delete or edit a transaction
- Categories (food, transport, etc.)
- Filter by month
