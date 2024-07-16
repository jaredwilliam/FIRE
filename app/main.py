def calc_final_value(initial_value, interest_rate, compounds_per_year, years):
    return initial_value * (1 + interest_rate / compounds_per_year) ** (
        compounds_per_year * years
    )


def calc_total_value(assests: dict):
    return sum([values["Current Value"] for _, values in assests.items()])


def calc_monthly_contribution(assets: dict):
    return sum([values["Monthly Contribution"] for _, values in assets.items()])


def calc_years_to_retirement(
    initial_value, target_value, interest_rate, compounds_per_year
):

    years = 0
    step = 0.1
    while (
        calc_final_value(initial_value, interest_rate, compounds_per_year, years)
        < target_value
    ):
        years += step

    return years


assets = {
    "CC 403b": {"Current Value": 206843.16, "Monthly Contribution": 1037.18},
    "CC IPP": {"Current Value": 57721.54, "Monthly Contribution": 328.36},
    "Individual": {"Current Value": 679.54, "Monthly Contribution": 216.67},
    "Simple IRA": {"Current Value": 23947.42, "Monthly Contribution": 0},
    "PGR 401k": {"Current Value": 37047.85, "Monthly Contribution": 1042.36},
    "HSA": {"Current Value": 10528.19, "Monthly Contribution": 0},
    "Roth IRA": {"Current Value": 66457.05, "Monthly Contribution": 583.33},
    "Crypto": {"Current Value": 6778.28, "Monthly Contribution": 216.67},
}

interest_rate = 0.08
years = 10
compounds_per_year = 12
target_value = 2_500_000
initial_value = calc_total_value(assets)


print(
    calc_years_to_retirement(
        initial_value, target_value, interest_rate, compounds_per_year
    )
    + 34
    + 5 / 12
)
