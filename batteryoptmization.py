import os, csv;

def calc_energy_density(capacity, weight, voltage) :
    # BATTERY OPTIMIZATION
    print("Energy Density")
    
def calc_power(capacity, voltage, efficiency):
    #TEST
    print("Calculate Power")
    
    
def optimize_battery(capacity, weight, voltage, temperature, efficiency):

    density = energy_density()
    power = power_output()

    if temperature<-10 or temperature>60:
        capacity = capacity - 10 
    if density<200:
        voltage = voltage + 0.1
        weight = weight - 10
    if output>200:
        efficieny = efficieny - 10
    
    
    # WHAT ARE ACCEPTABLE RANGES 
    battery_specifications=[capacity, voltage, weight, efficieny]
    optimized_dict = [optimized_capacity, optimized_weight, optimized_voltage, optimized_efficiency]
    
    optimized_energy_density = calc_energy_density 
    optimized_power = calc_power
    
    
def csvInputLoop():
    
    unoptimized_csv = osc.cv
    
    for x in data_csv: 