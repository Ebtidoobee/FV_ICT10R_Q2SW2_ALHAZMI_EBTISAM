from pyscript import document, display

subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']

def general_weighted_average(e):
    # Step 1: Clear previous outputs
    document.getElementById('student_info').innerText = ''
    document.getElementById('summary').innerText = ''
    document.getElementById('output').innerText = ''

    try:
        # Step 2: inputs
        first_name = document.getElementById('first_name').value
        last_name = document.getElementById('last_name').value

        science = float(document.getElementById('science_grade').value)
        math = float(document.getElementById('math_grade').value)
        english = float(document.getElementById('english_grade').value)
        filipino = float(document.getElementById('filipino_grade').value)
        ict = float(document.getElementById('ict_grade').value)
        pe = float(document.getElementById('pe_grade').value)

        # Step 3: Compute weighted average
        weighted_sum = (
            science * 5 +
            math * 5 +
            english * 5 +
            filipino * 3 +
            ict * 2 +
            pe * 1
        )

        total_units = 5 * 3 + 3 + 2 + 1  # = 21
        gwa = weighted_sum / total_units

        # Step 4: summary
        summary = f"""
{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
"""

        # Step 5: results
        display(f"Name: {first_name} {last_name}", target="student_info")
        display(summary.strip(), target="summary")
        display(f"{gwa:.2f}", target="output")

    except Exception as err:
        display(f"Error: Please enter valid numeric grades. ({err})", target="output")