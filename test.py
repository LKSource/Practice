import pandas as pd

# Creating the data for the Excel sheet
data = {
    "Room / Area": [
        "Hall-1 (Double Height)", "Hall-1 (Double Height)", "Hall-1 (Double Height)",
        "Hall-2 (Media Lounge)", "Hall-2 (Media Lounge)", "Hall-2 (Media Lounge)",
        "Master Bedroom", "Master Bedroom", "Master Bedroom",
        "Kitchen", "Kitchen", "Kitchen",
        "A. Toilet", "A. Toilet",
        "Pooja Room", "Utility Area"
    ],
    "Component Type": [
        "Fans", "Primary Lighting", "Accent Lighting",
        "Fans", "TV Hub", "Lighting",
        "Fans", "Lighting", "Switch Points",
        "Exhaust/Chimney", "Lighting", "Power Points",
        "Lighting", "Power Points",
        "Lighting", "Power Points"
    ],
    "Positioning & Recommendations": [
        "Wall-mounted fans at 8.5ft height on side walls (Staggered)",
        "Powerful wall-washers/up-lighters at 15ft height pointing up",
        "Grand Chandelier hanging to 10ft level; Wall sconces at 7.5ft",
        "One central ceiling fan with 12-inch down-rod",
        "Pooja outer wall: 4x 6A sockets, 1x 15A, hidden conduit for cables",
        "Dimmable spotlights + LED strip behind TV (Bias lighting)",
        "One central fan (aligned with lower 1/3 of bed)",
        "4x Recessed downlights + 2x Bedside reading lamps",
        "2-Way control (Entrance + Bedside); AC point at 7.5ft height",
        "Exhaust fan at window or Chimney point at 7ft above hob",
        "Moisture-proof LED batten + Under-cabinet LED strips for counter",
        "Dedicated 15A points for Fridge, Microwave, and Mixer",
        "Waterproof LED ceiling light + Mirror light above washbasin",
        "15A Geyser point at 7.5ft height (away from shower)",
        "Low-wattage warm focus light + Socket for electric lamps",
        "15A point for Washing Machine + High visibility LED batten"
    ],
    "Mounting Height (From Floor)": [
        "8.5 Feet", "15 Feet", "7.5 - 10 Feet",
        "10 Feet", "2 - 4 Feet", "Ceiling (11ft)",
        "10 Feet", "Ceiling (11ft)", "1.5 - 4 Feet",
        "7 Feet", "Cabinet level / Ceiling", "3.5 Feet",
        "Ceiling (11ft)", "7.5 Feet",
        "7 Feet", "4 Feet"
    ]
}

df = pd.DataFrame(data)

# Save to Excel with formatting
with pd.ExcelWriter("electrical_design_layout_v1.xlsx", engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Electrical Recommendations')
    
    # Accessing the openpyxl workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Electrical Recommendations']
    
    # Adjusting column widths for readability
    for i, col in enumerate(df.columns):
        column_len = df[col].astype(str).str.len().max()
        column_len = max(column_len, len(col)) + 5
        worksheet.column_dimensions[chr(65+i)].width = column_len