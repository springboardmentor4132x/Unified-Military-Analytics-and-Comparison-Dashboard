"""
KPI Feature Engineering -  military analytics KPIs from cleaned data.
"""

import json
import pandas as pd
import numpy as np

INPUT_FILE = 'data/military_cleaned.csv'
OUTPUT_EXCEL = 'data/military_final.xlsx'
OUTPUT_CSV = 'data/military_final.csv'
OUTPUT_LONG = 'data/military_long_format.csv'
CONFIG_DIR = 'config'

def load_json(filename):
    """Load JSON config file"""
    with open(f"{CONFIG_DIR}/{filename}", 'r', encoding='utf-8') as f:
        return json.load(f)

def get_column(df, name, default=0):
    """Get column as numeric, with fallback default"""
    if name in df.columns:
        return pd.to_numeric(df[name], errors='coerce').fillna(default)
    return pd.Series([default] * len(df), index=df.index)

def create_long_format(df):
    """Create long-format version for Tableau visualizations"""
    id_vars = ['country', 'region', 'continent', 'alliances']
    value_vars = [
        'total_population_by_country', 'active_military_manpower', 'aircraft_total',
        'armor_tanks_total', 'navy_ships', 'defense_spending_budget',
        'kpi_power_index_rank_gap', 'kpi_assets_per_capita', 'kpi_budget_to_gdp_ratio',
        'kpi_air_power_score', 'kpi_naval_power_score', 'kpi_land_power_score'
    ]
    value_vars = [col for col in value_vars if col in df.columns]
    return df.melt(id_vars=id_vars, value_vars=value_vars, var_name='metric', value_name='value')


# KPI CALCULATIONS


def calculate_kpis(df):
    """Calculate all KPIs and add geographic/alliance metadata"""
    result = df.copy()
    
    # Load config
    regions = load_json('regions.json')
    alliances = load_json('alliances.json')
    
    # Extract columns
    population = get_column(result, 'total_population_by_country')
    active_personnel = get_column(result, 'active_military_manpower')
    total_aircraft = get_column(result, 'aircraft_total')
    fighter_aircraft = get_column(result, 'aircraft_total_fighters')
    attack_aircraft = get_column(result, 'aircraft_total_attack_types')
    helicopters = get_column(result, 'aircraft_helicopters_total')
    attack_helicopters = get_column(result, 'aircraft_helicopters_attack')
    tanks = get_column(result, 'armor_tanks_total')
    afvs = get_column(result, 'armor_apc_total')
    artillery = get_column(result, 'armor_towed_artillery_total') + get_column(result, 'armor_self_propelled_guns_total')
    naval_fleet = get_column(result, 'navy_ships')
    submarines = get_column(result, 'navy_submarines')
    carriers = get_column(result, 'navy_aircraft_carriers')
    destroyers = get_column(result, 'navy_destroyers')
    frigates = get_column(result, 'navy_frigates')
    defense_budget = get_column(result, 'defense_spending_budget')
    ppp = get_column(result, 'purchasing_power_parity')
    
  
    power_rankings = load_json('power_rankings.json')
    power_rank = result['country'].map(lambda x: power_rankings.get(x, 999))
    
   
    result['kpi_power_index_rank_gap'] = power_rank - 1
    
   
    total_assets = total_aircraft + tanks + afvs + naval_fleet + submarines
    result['kpi_assets_per_capita'] = (total_assets / population * 100000).replace([np.inf, -np.inf], 0).fillna(0).round(2)
    
    
    result['kpi_budget_to_gdp_ratio'] = (defense_budget / ppp * 100).replace([np.inf, -np.inf], 0).fillna(0).round(4)
    
    
    result['kpi_personnel_ratio'] = (active_personnel / population * 100).replace([np.inf, -np.inf], 0).fillna(0).round(4)
    
    
    result['kpi_air_power_score'] = (
        fighter_aircraft * 3 + attack_aircraft * 2.5 + attack_helicopters * 2 +
        total_aircraft * 0.5 + helicopters * 0.5
    ).round(0)
    
    
    result['kpi_naval_power_score'] = (
        carriers * 50 + submarines * 10 + destroyers * 5 + frigates * 3 + naval_fleet * 0.5
    ).round(0)
    
   
    result['kpi_land_power_score'] = (
        tanks * 2 + afvs * 1 + artillery * 1.5 + active_personnel * 0.001
    ).round(0)
    
    # Normalized scores (0-100 scale) for better chart comparison
    max_air = result['kpi_air_power_score'].max()
    max_naval = result['kpi_naval_power_score'].max()
    max_land = result['kpi_land_power_score'].max()
    
    result['kpi_air_power_normalized'] = (result['kpi_air_power_score'] / max_air * 100).round(1) if max_air > 0 else 0
    result['kpi_naval_power_normalized'] = (result['kpi_naval_power_score'] / max_naval * 100).round(1) if max_naval > 0 else 0
    result['kpi_land_power_normalized'] = (result['kpi_land_power_score'] / max_land * 100).round(1) if max_land > 0 else 0
    
    # Adding geographical data
    result['region'] = result['country'].map(lambda x: regions.get(x, ['Unknown', 'Unknown'])[0])
    result['continent'] = result['country'].map(lambda x: regions.get(x, ['Unknown', 'Unknown'])[1])
    
    # Add alliance flags
    for alliance_name, members in alliances.items():
        result[f'alliance_{alliance_name.lower()}'] = result['country'].isin(members).astype(int)
    
    # Combined alliance string
    alliance_cols = [col for col in result.columns if col.startswith('alliance_')]
    result['alliances'] = result.apply(
        lambda row: ', '.join([col.replace('alliance_', '').upper() for col in alliance_cols if row[col] == 1]) or 'None',
        axis=1
    )
    
    return result


def main():
    """Main execution"""
    df = pd.read_csv(INPUT_FILE)
    df_final = calculate_kpis(df)
    
    # Save wide format
    df_final.to_excel(OUTPUT_EXCEL, index=False, engine='openpyxl')
    df_final.to_csv(OUTPUT_CSV, index=False)
    
    # Save long format
    df_long = create_long_format(df_final)
    df_long.to_csv(OUTPUT_LONG, index=False)
    
    return df_final

if __name__ == "__main__":
    main()

