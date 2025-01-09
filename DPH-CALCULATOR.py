print("To exit calculator, enter '0' in the menu")

def dph():
#dph function
    unit = float(input("Pounds(1) or kilograms (2)?:  "))
    weight = float(input("Input weight: "))
    if unit == 2:
        weight *= 2.205

    #finding out what format the medication is in.
    med_type = float(input("Pill(1) or syrup(2)?:"))
    if med_type == 2:
        syrup_mg = float(input("What is your syrup Mg value (MG/ml)?:"))
        syrup_ml = float(input("what is your syrup Ml value (mg/ML)"))
        syrup_strength = syrup_mg / syrup_ml

        #calculating dosages for DPH
        threshhold = round(0.866 * weight + 26.3)
        audio = round(1.44 * weight + 86.4)
        mild_audiovisual = round(1.77 * weight + 49.4)
        major_audiovisual = round(2.52 * weight + 138)
        partial_delirium = round(2.92 * weight + 147)
        total_delirium = round(2.5 * weight + 379)
        # calculating the recommended trip dosage
        avg_trip = int((mild_audiovisual + major_audiovisual) / 2)

        def syrup_dose(d):

            dose = d / syrup_strength
            return round(dose)

        # printing the recommended dosages for syrup
        print(f"Threshold effects:------------------{threshhold}mg ({syrup_dose(threshhold)} ml)")
        print(f"Auditory Hallucinations:------------{audio}mg ({syrup_dose(audio)} ml)")
        print(f"Minor audiovisual hallucinations:---{mild_audiovisual}mg ({syrup_dose(mild_audiovisual)} ml)")
        print(f"Average trip dose for you:----------{avg_trip}mg ({syrup_dose(avg_trip)} ml)")
        print(f"Major audiovisual hallucinations:---{major_audiovisual}mg ({syrup_dose(major_audiovisual)} ml)")
        print(f"Mild delirium/Potential psychosis:--{partial_delirium}mg ({syrup_dose(partial_delirium)} ml)")
        print(f"Total delirium/Psychosis:-----------{total_delirium}mg ({syrup_dose(total_delirium)} ml)")
        
    elif med_type == 1:
        pill_type = int(input("Pill type? 50mg(1) or 25mg(2) or 12.5mg(3)"))
        if pill_type == 3:
            pill_type += 1
        threshold = round(0.866 * weight + 26.3)
        audio = round(1.44 * weight + 86.4)
        mild_audiovisual = round(1.77 * weight + 49.4)
        major_audiovisual = round(2.52 * weight + 138)
        partial_delirium = round(2.92 * weight + 147)
        total_delirium = round(2.5 * weight + 379)
        # calculating the recommended trip dosage
        avg_trip = int((mild_audiovisual + major_audiovisual) / 2)

        #rounding the dosages for pills (to figure out how many pills to take)
        def round_pill(balls):
            a = balls / 25
            a = a * pill_type
            a = a / 2
            return round(a)

        # printing the recommended dosages for pill
        print(f"Threshold effects:------------------{threshold}mg ({round_pill(threshold)} pills)")
        print(f"Auditory hallucinations:------------{audio}mg ({round_pill(audio)} pills) ")
        print(f"Minor audiovisual hallucinations:---{mild_audiovisual}mg ({round_pill(mild_audiovisual)} pills) ")
        print(f"Average trip dose for you:----------{avg_trip}mg ({round_pill(avg_trip)} pills) ")
        print(f"Major audiovisual hallucinations:---{major_audiovisual}mg ({round_pill(major_audiovisual)} pills) ")
        print(f"Mild delirium/Potential psychosis:--{partial_delirium}mg ({round_pill(partial_delirium)} pills) ")
        print(f"Total delirium/Psychosis:-----------{total_delirium}mg ({round_pill(total_delirium)} pills) ")
        
def dxm():
#dxm function
    unit = int(input("Pounds(1) or kilograms(2)?: "))
    weight = float(input("Input weight?: "))
    med_type_dxm = int(input("Pill(1) or syrup(2)?: "))
#figuring out weight and dose calculations
    if unit == 1:
        weight *= 0.4536
    first_plateau_min = weight * 1.5
    second_plateau_min = weight * 2.5
    third_plateau_min = weight * 7.5
    fourth_plateau_min = weight * 15
    sigma_plateau = weight * 25
#finding out the min and max of the dxm dosage
    first_plateau_max = second_plateau_min - 1
    second_plateau_max = third_plateau_min - 1
    third_plateau_max = fourth_plateau_min - 1
    fourth_plateau_max = sigma_plateau - 1

    if med_type_dxm == 1:
        pill_type = float(input("Mg per pill?: "))
    elif med_type_dxm == 2:
        syrup_mg = float(input("What is your syrup Mg value (MG/ml)?:"))
        syrup_ml = float(input("what is your syrup Ml value (mg/ML)"))
        syrup_strength = syrup_mg / syrup_ml


    def rounding(balls2):
        dose = balls2 * 25
        dose = dose / 25
        return round(dose)

    if med_type_dxm == 1:

        first_plateau_min_pill = rounding(first_plateau_min / pill_type)
        first_plateau_max_pill = rounding(first_plateau_max / pill_type)
        second_plateau_min_pill = rounding(second_plateau_min / pill_type)
        second_plateau_max_pill = rounding(second_plateau_max / pill_type)
        third_plateau_min_pill = rounding(third_plateau_min / pill_type)
        third_plateau_max_pill = rounding(third_plateau_max / pill_type)
        fourth_plateau_min_pill = rounding(fourth_plateau_min / pill_type)
        fourth_plateau_max_pill = rounding(fourth_plateau_max / pill_type)
        sigma_plateau_pill = rounding(sigma_plateau / pill_type)

        print(f"First plateau:----{rounding(first_plateau_min)}mg ({first_plateau_min_pill} pills) - {rounding(first_plateau_max)}mg ({first_plateau_max_pill} pills)")
        print(f"Second plateau:---{rounding(second_plateau_min)}mg ({second_plateau_min_pill} pills) - {rounding(second_plateau_max)}mg ({rounding(second_plateau_max_pill)}pills)")
        print(f"Third plateau:----{rounding(third_plateau_min)}mg ({third_plateau_min_pill}pills)- {rounding(third_plateau_max)}mg ({third_plateau_max_pill}pills)")
        print(f"Fourth plateau:---{rounding(fourth_plateau_min)}mg ({fourth_plateau_min_pill}pills) - {rounding(fourth_plateau_max)}mg ({fourth_plateau_max_pill}pills)")
        print(f"Plateau Sigma:----{rounding(sigma_plateau)}mg ({sigma_plateau_pill}pills)")
        print("The previous amount surpasses the lethal dose 50. May be deadly")
        
    elif med_type_dxm == 2:

        first_plateau_min_ml = int(first_plateau_min / syrup_strength)
        first_plateau_max_ml = int(first_plateau_max / syrup_strength)
        second_plateau_min_ml = int(second_plateau_min / syrup_strength)
        second_plateau_max_ml = int(second_plateau_max / syrup_strength)
        third_plateau_min_ml = int(third_plateau_min / syrup_strength)
        third_plateau_max_ml = int(third_plateau_max / syrup_strength)
        fourth_plateau_min_ml = int(fourth_plateau_min / syrup_strength)
        fourth_plateau_max_ml = int(fourth_plateau_max / syrup_strength)
        sigma_plateau_ml = int(sigma_plateau / syrup_strength)

        print(f"First plateau:----{rounding(first_plateau_min)}mg ({first_plateau_min_ml}ml) - {rounding(first_plateau_max)}mg ({first_plateau_max_ml}ml)")
        print(f"Second plateau:---{rounding(second_plateau_min)}mg ({second_plateau_min_ml}ml) - {rounding(second_plateau_max)}mg ({second_plateau_max_ml}ml)")
        print(f"Third plateau:----{rounding(third_plateau_min)}mg ({third_plateau_min_ml}ml)- {rounding(third_plateau_max)}mg ({third_plateau_max_ml}ml)")
        print(f"Fourth plateau:---{rounding(fourth_plateau_min)}mg ({fourth_plateau_min_ml}ml) - {rounding(fourth_plateau_max)}mg ({fourth_plateau_max_ml}ml)")
        print(f"Plateau Sigma:----{rounding(sigma_plateau)}mg ({sigma_plateau_ml}ml)")
        print("The previous amount surpasses the lethal dose 50. May be deadly")
        
while True:
    meds = int(input("Are you taking DPH(1) or DXM(2)?: "))
    if meds == 0:
        print("Thank you for using, stay safe :)")
        break
    elif meds == 1:
        dph()
    elif meds == 2:
        dxm()
    else:
        print("Invalid option, more drugs will be supported soon")
