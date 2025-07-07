# calculator.py

HUMM_TABLE = [
    {"fortnights": 6, "fee_pct": 4.45, "est_fee": 0, "monthly_fee": 9.95},
    {"fortnights": 13, "fee_pct": 4.69, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 26, "fee_pct": 5.04, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 39, "fee_pct": 9.39, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 52, "fee_pct": 9.99, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 65, "fee_pct": 12.37, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 86, "fee_pct": 15.59, "est_fee": 60, "monthly_fee": 9.95},
    {"fortnights": 104, "fee_pct": 18.57, "est_fee": 60, "monthly_fee": 9.95},
]

ZIP_TABLE = [
    {"months": 6, "fee_pct": 3.025},
    {"months": 12, "fee_pct": 5.225},
    {"months": 18, "fee_pct": 8.8},
    {"months": 24, "fee_pct": 7.425},
    {"months": 36, "fee_pct": 9.625},
    {"months": 48, "fee_pct": 11.825},
]

def get_zip_est_fee(loan_amount):
    if loan_amount <= 1000: return 0
    elif loan_amount <= 2000: return 25
    elif loan_amount <= 3000: return 49
    elif loan_amount <= 4000: return 75
    else: return 99

def calculate(provider, loan_amount, fortnights):
    if provider.lower() == "humm":
        plan = next((p for p in HUMM_TABLE if p["fortnights"] == fortnights), None)
        if not plan:
            return {"error": f"No HUMM plan for {fortnights} fortnights"}
        fee_pct = plan["fee_pct"]
        est_fee = plan["est_fee"]
        monthly_fee = plan["monthly_fee"]
        months = round(fortnights / 2.17)
    elif provider.lower() == "zip":
        months = round(fortnights / 2.17)
        plan = next((p for p in ZIP_TABLE if p["months"] == months), None)
        if not plan:
            return {"error": f"No ZIP plan for {months} months"}
        fee_pct = plan["fee_pct"]
        est_fee = get_zip_est_fee(loan_amount)
        monthly_fee = 9.95
    else:
        return {"error": "Unknown provider"}

    merchant_fee = loan_amount * (fee_pct / 100)
    total_monthly_fees = monthly_fee * months
    total_cost = loan_amount + merchant_fee + est_fee + total_monthly_fees
    fortnightly_repayment = total_cost / fortnights

    return {
        "Provider": provider.upper(),
        "Merchant Fee %": fee_pct,
        "Merchant Fee $": round(merchant_fee, 2),
        "Establishment Fee $": est_fee,
        "Monthly Loan Fee $": monthly_fee,
        "Number of Months": months,
        "Total Monthly Fees $": round(total_monthly_fees, 2),
        "Total Cost to Patient $": round(total_cost, 2),
        "Fortnightly Repayment $": round(fortnightly_repayment, 2),
    }
