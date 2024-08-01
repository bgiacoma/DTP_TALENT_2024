from xkn import MKN, MKNConfig

# initialize MKNConfig object from the config file
config_path = "examples/kn_config.ini"
mkn_config = MKNConfig(config_path)

# Uncomment to print a list of inputs and their explantions
# mkn_config.get_info()

# initialize MKN object from the read parameters
mkn = MKN(*mkn_config.get_params(), log_level="WARNING")

if __name__ == "__main__":

    inputs = {
        "view_angle": ,                 # viewing angle in rad [0-pi/2]
        "distance": ,                   # distance in Mpc
        "m_ej_dynamics": ,              # dynamical ejecta mass in solar masses
        "vel_dynamics": ,               # average speed of dynamical ejecta in unit of c
        "high_lat_op_dynamics": ,       # polar opacity in cm2/g for dynamical ejecta
        "low_lat_op_dynamics": ,        # equatorial opacity in cm2/g for dynamical ejecta
        "m_ej_secular": ,               # mass of secular ejecta in solar masses
        "vel_secular": ,                # average speed of dynamical ejecta in unit of c
        "op_secular": ,                 # opacity of secular ejecta in cm2/g
        "m_ej_wind": ,                  # mass of disk winds in solar masses
        "vel_wind": ,                   # average speed of wind ejecta [c]
        "high_lat_op_wind": ,           # polar opacity in cm2/g for wind ejecta
        "low_lat_op_wind": ,            # equatorial opacity in cm2/g for wind ejecta
    }

    print("\nComputing and plotting magnitudes...")
    mkn.plot_magnitudes(mkn_config.get_vars(inputs), filename="examples/magnitudes.pdf")
