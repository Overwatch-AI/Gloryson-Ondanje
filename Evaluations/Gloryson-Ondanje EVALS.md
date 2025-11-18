## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: models/gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 55.0%
- **Page-reference accuracy**: 18.0%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: Based on the information provided in the excerpts, the specific climb limit weight for a 2,000 feet pressure altitude and 50°C OAT cannot be determined.

The excerpts describe the procedure for finding this value but do not contain the required data tables. According to the manual (Excerpt 1, Page 104), to find the Climb Limit Weight, you must:

1.  Enter the appropriate "Field and Climb Limit Weight Table" for the given pressure altitude and runway condition.
2.  Use the airport OAT to read the Climb Limit Weight from that table.

While the Table of Contents excerpts (Pages 78 and 79) show that "Takeoff Field & Climb Limit Weights - Dry Runway" tables exist (e.g., on pages PD.20.2 and PD.40.2), the tables themselves are not included in the provided text.
- **Labelled pages**: 83
- **Returned pages**: 78, 79, 104, 107
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: Based on the provided excerpts, for a Flaps 15 takeoff, the first flap selection during retraction is **Flaps 5**, made at **V2 + 15** (Page 41).

According to the "Takeoff Flap Retraction Speed Schedule" on Page 41, the procedure is as follows:
*   **T/O FLAPS:** 15
*   **SELECT FLAPS AT:** "5" at V2 + 15

The manual also notes to "Limit bank angle to 15 degrees until reaching V2 + 15" (Page 41).
- **Labelled pages**: 41
- **Returned pages**: 41, 44, 51, 53, 54
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the information provided in the manual excerpts, the answer cannot be determined.

The procedure to find the Landing Field Limit Weight is described on Page 107. It states to "enter the Field Limit Weight table with wind corrected field length and pressure altitude to read field limit weight for the expected runway condition."

However, the excerpts do not contain the actual "Field Limit Weight table" needed to find the specific weight value for a 1,600-meter wind-corrected field length and a 1,000-foot pressure altitude.
- **Labelled pages**: 99
- **Returned pages**: 78, 79, 104, 106, 107
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the manual excerpts, when a positive rate of climb is indicated, the first action is to call “GEAR UP”. The landing gear lever is then positioned to UP. (Page 39)
- **Labelled pages**: 39, 51
- **Returned pages**: 26, 39, 46, 75, 79
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the provided excerpts, when the aircraft is not moving under its own power, responsibility for the forward aisle stand is split between the Captain and the First Officer.

According to the "Panel Scan Diagram" in Excerpt 1 (Page 6), the Captain is responsible for the left side of the forward aisle stand, and the First Officer is responsible for the right side. This division of duties is part of the "area of responsibility concept" for pre/post flight duties mentioned in Excerpt 3 (Page 4).
- **Labelled pages**: 6
- **Returned pages**: 4, 6, 7, 21
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 2.50
### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the "Visual Traffic Pattern" procedures on Page 56, the three actions to be completed prior to turning base are:

*   Gear down
*   Flaps 15 (landing flaps for 1 engine)
*   Arm speedbrake
- **Labelled pages**: 56
- **Returned pages**: 21, 55, 56, 67, 132
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: Based on the provided excerpts, when the Pilot Not Flying (PNF) makes CDU entries during flight, the entries must be **verified by the pilot flying prior to execution** (Page 5).
- **Labelled pages**: 5
- **Returned pages**: 4, 5, 38, 67
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.50
### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: Based on the provided excerpts, the illuminated amber STAIRS Operating (OPER) Light indicates that the airstair is in transit (Page 126).
- **Labelled pages**: 126
- **Returned pages**: 126, 133, 134, 135, 138
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: Based on the provided excerpts from the Boeing 737 Operations Manual, the correct configuration for the ISOLATION VALVE switch during the After Start Procedure is not mentioned.

The excerpts detail parts of the Engine Start Procedure (Page 33, 34), pre-start checks (Page 23), fuel transfer (Page 59), and adverse weather operations (Page 71), but do not contain information regarding the ISOLATION VALVE switch or the After Start Procedure.
- **Labelled pages**: 35
- **Returned pages**: 23, 33, 34, 59, 71
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: Based on the manual excerpts provided:

*   **Descent and Approach Procedure:** The action taken is to "Set AUTO BRAKE select switch to desired brake setting" (Page 43).

*   **Landing Roll Procedure:** The final action regarding the autobrake system is to "disarm the autobrake and continue manual braking as required" prior to reaching taxi speed (Page 47). The provided excerpts do not specify if this action is performed by the Pilot Flying.
- **Labelled pages**: 43, 47
- **Returned pages**: 22, 43, 45, 47
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 5.00
### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: Based on the provided excerpts, the specific total fuel flow value for holding at 10,000 feet and 60,000 kg is not available.

The manual indicates that this information can be found in a "Holding Planning" table (Excerpt 1, Page 105; Excerpt 2, Page 77; Excerpt 5, Page 78).

According to Excerpt 1 (Page 105), the data in this table is based on:
*   Flaps up holding.
*   The FMC holding speed schedule.
*   Flight in a racetrack holding pattern.

For holding in straight and level flight, the table values should be reduced by 5% (Excerpt 1, Page 105).
- **Labelled pages**: 93
- **Returned pages**: 77, 78, 105, 106
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: Based on the provided excerpts, the function of the TAXI Light switch is as follows:

The TAXI Light switch, located on the Forward Overhead Panel, controls the taxi light mounted on the nose wheel strut (Page 112, Page 131). The switch has two positions:

*   **ON:** The nose wheel well taxi light is illuminated.
*   **OFF:** The nose wheel well taxi light is extinguished.

(Page 112)

The taxi light points in the same direction as the nose wheel (Page 131).
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 113, 115, 131, 134
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 4.00
### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: Based on the provided excerpts, the Logo Lights are located on the top of each horizontal stabilizer surface. Their purpose is to point light on both sides of the vertical stabilizer (Page 131).

Diagrams on pages 132 and 133 visually confirm this location, labeling the white "LOGO LIGHT" on the horizontal stabilizer.

The LOGO light switch is located on the forward overhead panel and has ON and OFF positions (Page 113).
- **Labelled pages**: 131
- **Returned pages**: 113, 130, 131, 132, 133
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the information provided in the manual excerpts, the specific gradient adjustment value for speed is not available.

Excerpt 1 (Page 107) states that to determine the final go-around gradient, you must "adjust the reference gradient for airplane weight and speed using the tables provided to determine the weight and speed adjusted go-around gradient." However, the excerpts do not include these specific tables.

The procedure for a missed approach, which would involve a go-around, is outlined in Excerpt 5 (Page 53) and includes selecting "Flaps 15 (flaps 1, 1 engine)" after pushing the TO/GA switch.
- **Labelled pages**: 101
- **Returned pages**: 41, 44, 51, 53, 107
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: Based on the provided manual excerpts, after removing the ringed safety pin, the action required to discharge the BCF (Halon) fire extinguisher is to **press the top lever** (Page 146).
- **Labelled pages**: 146
- **Returned pages**: 11, 12, 145, 146
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.50
### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Based on the information provided in the manual excerpts, the procedure to determine the slope and wind-corrected field length is as follows:

1.  Enter the appropriate table with the available field length (2,000 meters) and runway slope (1.0% uphill) to determine the slope corrected field length.
2.  Next, enter the appropriate table with the resulting slope corrected field length and the wind component (10-knot tailwind) to determine the final slope and wind corrected field length.

This procedure is described on Page 103.

The excerpts do not contain the specific "Slope and Wind Corrections" tables required to calculate the final numerical value for your given conditions.
- **Labelled pages**: 81
- **Returned pages**: 61, 78, 79, 103, 107
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: Based on the provided excerpts, the minimum required pressure for the 114 Cu. Ft. crew oxygen cylinder is 690 PSI.

This value is found in the "Enroute Crew Oxygen Requirements" table for a "114/115 Cu. Ft. Cylinder" on Page 94. The pressure is determined by cross-referencing the row for a bottle temperature of 30°C with the column for 3 crew members using oxygen.

According to Page 141, the oxygen pressure is displayed on the Oxygen Pressure indicator on the aft overhead panel when the battery switch is ON.
- **Labelled pages**: 94
- **Returned pages**: 94, 105, 141, 144
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.50
### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: Based on the provided manual excerpts, when the glideslope comes alive on an ILS approach, you should initiate the following three actions:

1.  **Gear down**
2.  **Flaps 15** (noted as the final flap for a 1-engine approach)
3.  **Arm speedbrake**

This information is found in the ILS Approach flight pattern diagram (Excerpt 4, Page 52).
- **Labelled pages**: 45, 52
- **Returned pages**: 39, 40, 45, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00
### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided excerpts, the three available settings on the POSITION light switch are (Page 1.30.6):

*   **STROBE & STEADY:** Illuminates the red and green wing-tip position lights, white trailing edge wing-tip lights, and the wing-tip and tail strobe lights.
*   **OFF:** Extinguishes the red and green wing-tip position lights, white trailing edge wing-tip lights, and the wing-tip and tail strobe lights.
*   **STEADY:** Illuminates the red and green wing-tip position lights and the white trailing edge wing-tip lights.
- **Labelled pages**: 113
- **Returned pages**: 21, 29, 108, 113, 131
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the provided excerpts from the Boeing 737 Operations Manual, the name of the bar that secures the emergency escape slide to the aircraft floor is not mentioned. The excerpts discuss emergency lighting, including escape slide lighting (Page 138), and various door controls, but do not detail the mechanical components of the emergency escape slide itself.
- **Labelled pages**: 123
- **Returned pages**: 115, 116, 119, 135, 138
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00
