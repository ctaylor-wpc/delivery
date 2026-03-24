# pricing_engine.py
# Edit the values in this file to adjust cost inputs and profit margin.
# The calculated rates feed directly into delivery_config.py.

# ── Fuel ─────────────────────────────────────────────────────────────────────
cpg_gas = 3.74
cpg_diesel = 5.03

# ── Speed assumption (used to convert hourly labor → per-mile labor) ──────────
avg_mph = 45

# ── Vehicle 1: 2021 Ford Transit Van (gas) ───────────────────────────────────
v1_mpg = 17
v1_replacement_cost = 51000
v1_lifespan_miles = 200000

v1_wear_per_mile = v1_replacement_cost / v1_lifespan_miles
v1_fuel_per_mile = cpg_gas / v1_mpg

# ── Vehicle 2: 2025 Ford F-350 Dump Bed (diesel) ─────────────────────────────
v2_mpg = 13
v2_replacement_cost = 90000
v2_lifespan_miles = 300000

v2_wear_per_mile = v2_replacement_cost / v2_lifespan_miles
v2_fuel_per_mile = cpg_diesel / v2_mpg

# ── Hourly labor rates ────────────────────────────────────────────────────────
hourly_t = 46.15
hourly_h = 29.81
hourly_o = 15.00
hourly_e = 29.81  # same rate as H

# ── Labor per mile (driving time only) ───────────────────────────────────────
labor_per_mile_t = hourly_t / avg_mph
labor_per_mile_h = hourly_h / avg_mph
labor_per_mile_o = hourly_o / avg_mph
labor_per_mile_e = hourly_e / avg_mph

# ── Load times (in hours) ─────────────────────────────────────────────────────
load_time_simple    = 10 / 60
load_time_single    = 15 / 60
load_time_double    = 15 / 60
load_time_bulk      = 15 / 60
load_time_bulk_plus = 25 / 60

# ── Profit margin ─────────────────────────────────────────────────────────────
profit_margin = 0.22

# ── Cost calculations per delivery type ───────────────────────────────────────
# Each type: wear + fuel + driving labor (per mile) + loading labor (flat, spread per mile isn't
# meaningful here — loading cost is added to the minimum instead, see notes below)
#
# Loading labor is a fixed cost per job, not per mile. It's factored into the minimum price
# rather than the per-mile rate so short deliveries still cover the load cost.

def _charge(cost_per_mile):
    return round(cost_per_mile * (1 + profit_margin), 4)

def _load_cost(load_time_hours, *hourly_rates):
    """Total labor cost for loading, across all people present."""
    return sum(r * load_time_hours for r in hourly_rates)

# Simple: Person T + Vehicle 1
simple_cost_per_mile = v1_wear_per_mile + v1_fuel_per_mile + labor_per_mile_t
simple_load_cost     = _load_cost(load_time_simple, hourly_t)
SIMPLE_RATE          = _charge(simple_cost_per_mile)
SIMPLE_LOAD_COST     = round(simple_load_cost * (1 + profit_margin), 2)

# Single: Person H + Vehicle 2
single_cost_per_mile = v2_wear_per_mile + v2_fuel_per_mile + labor_per_mile_h
single_load_cost     = _load_cost(load_time_single, hourly_h)
SINGLE_RATE          = _charge(single_cost_per_mile)
SINGLE_LOAD_COST     = round(single_load_cost * (1 + profit_margin), 2)

# Double: Person H + Person E + Vehicle 2
double_cost_per_mile = v2_wear_per_mile + v2_fuel_per_mile + labor_per_mile_h + labor_per_mile_e
double_load_cost     = _load_cost(load_time_double, hourly_h, hourly_e)
DOUBLE_RATE          = _charge(double_cost_per_mile)
DOUBLE_LOAD_COST     = round(double_load_cost * (1 + profit_margin), 2)

# Bulk: Person T + Vehicle 2
bulk_cost_per_mile = v2_wear_per_mile + v2_fuel_per_mile + labor_per_mile_t
bulk_load_cost     = _load_cost(load_time_bulk, hourly_t)
BULK_RATE          = _charge(bulk_cost_per_mile)
BULK_LOAD_COST     = round(bulk_load_cost * (1 + profit_margin), 2)

# Bulk Plus: Person T + Person O + Vehicle 2
bulk_plus_cost_per_mile = v2_wear_per_mile + v2_fuel_per_mile + labor_per_mile_t + labor_per_mile_o
bulk_plus_load_cost     = _load_cost(load_time_bulk_plus, hourly_t, hourly_o)
BULK_PLUS_RATE          = _charge(bulk_plus_cost_per_mile)
BULK_PLUS_LOAD_COST     = round(bulk_plus_load_cost * (1 + profit_margin), 2)
