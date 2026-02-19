Milestone 2 focuses on converting the clean military dataset into an analytics ready framework by using KPIs and preparing the data for interative dashboard development.

**Data Source:**
 **Uses the output of module 1** 
 contains:
 Power Index Rankings
 Manpower data (Active, Reserved, Paramilitary)
 Land, Air and Naval Assets
 Defense Budget
 Economic Indicators (PPP available)
 Population Statistics

 **Methodology:**
 KPI Feature Engineering
 Using python(pandas) new analytics measures were created after cleaning the data
 
 **Total Aircrafts:**
    -To measure air power, all the aircrafts types were summed up
    -It is performed to find out the air strength of the country

 **Total Growund Power:**
    -To measure ground strength, tanks, armored vehicles and artillery is combined.
    -Represents the land warfare capability.
    
 **Overall Military Assets:**
    -Combined indicator for total military strength.
  
 **Air to Grounf Ratio:**
    -This KPI shows whether a country is air dominant or ground dominant.
  
 **Military Ranks:**
    -Countries were ranked based on the overall military assets using dense ranking.
  
 **Artillary Modernization:**
     -To analyzze modernisation the ratio of self propelled artillary to the total artillary is calculated.
       
**Power Index Rank Gap:**
     -Ranking in consistency using rank gap.
  
**Now the dashboard is prepared using the final files containing KPIs**
    **KPI OVERVIEW:**
       **Provides the high level summary of global military strength.**
        - Country Slicer
        - Total Ground Power 
        - Artillary Modernization 
        - Total Aircrafts
        - Average Military Rank
        - Ground Power Share
        - Total Assets
        - Total Assets Chart
        - Ground Power Share (Donut Chart)
    **POWER COMPARISON:**
       **Compares air and the ground strength across countries**
        - Country Slicer
        - Total Ground Power
        - Total Aircraft
        - Air to Ground Ratio (Line Chart)
    **MODERNIZATION AND RANKING:**
       **Focuses on Modernization and Ranking Consistency.**
        - Power index rank gap
        - Artillery Modernization
        - Country Slicer
**Key Insights from Milestone 2**
      - Normalized KPIs significantly change country ranking perspectives.
      - Military structure varies strongly between nations.
      - Modernization metrics provide deeper strategic insight beyond raw totals.
