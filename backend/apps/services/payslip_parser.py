+
SALARY_COMPONENTS = {
    "Basic": r"Basic\s+(\d+)",
    "HRA": r"HRA\s+(\d+)",
    "PF": r"PF\s+(\d+)",
    "Professional Tax": r"Professional Tax\s+(\d+)",
    "Net Salary": r"Net Salary\s+(\d+)"
}


def parse_payslip(text: str):
    data = {}
    for key, pattern in SALARY_COMPONENTS.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data[key] = int(match.group(1))
    return data