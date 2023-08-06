"""This module provides the `Units` class to convert from default units of `py_cea` to user units.

An instance of `Units` is created as `u` and is populated with default units and
most commonly used user units. The user can add additional user units as needed.

Methods
-------
add_default_unit(name, alias_list=[])
    Initialize `self.main_dict` with `py_cea` default units. Don't use.
add_user_units(default_units, user_units, multiplier, offset=0)
    Add user units to `self.main_dict`. Use to add more units.
convert_to_user(default_value, default_units, user_units)
    Convert `default_value` with `default_units` to value with `user_units`.
convert_to_default(user_value, user_units, default_units)
    Convert `user_value` with `user_units` to value with `default_units`.
print_default_units()
    Print all default units.
print_user_units(default_units)
    Print all user units available for some `default_units`.

Notes
-----
TODO: it might be faster to have a units file instead of always building the dictionary.

It is slightly inefficient to handle units always. If the user wants imperial units,
then conversions are pointless and only slow down the code. I guess that is why originally
there was a CEA object with units and a CEA object without units. However for the sake of
clarity and simplicity, CEA will always handle units.

One cannot convert between two user units directly. The user must convert to default units first.

Examples
--------
>>> from pycea.units import u
>>> u.convert_to_user(CEA.get_Isp(), "sec", "N sec/kg")
>>> u.convert_to_default(CEA.get_Isp(), "N sec/kg", "sec")
"""


class Units:
    def __init__(self):
        """This class provides an API to convert from default units of `py_cea` to user units.

        Attributes
        ----------
        main_dictionary : dict
            dictionary of dictionaries of conversion factors and offsets

        Notes
        -----
        SI units are the default units in `pycea` even though imperial units
        are used inside `py_cea` (the original NASA CEA code).

        Offsets are only used in temperature conversions.

        `multiplier` is the conversion factor from default units to user units.

        Examples
        --------
        >>> u = Units()
        >>> u.convert_to_user(1000, "psia", "MPa")
        6.894757293168361
        """
        self.main_dict = {}

    def add_default_unit(self, name, alias_list=[]):
        """Initialize `self.main_dict` with `py_cea` default units.

        Parameters
        ----------
        name : str
            name of the unit being added to `main_dictionary` dictionary
        alias_list : list
            list of alternate names for the same units
        """
        self.main_dict[name] = {}

        # conversion factor to itself is 1.0, offset is 0
        self.main_dict[name].update({name: (1.0, 0)})

        # allow calls with all upper or lower case
        self.main_dict[name].update({name.lower(): (1.0, 0)})
        self.main_dict[name].update({name.upper(): (1.0, 0)})

        # include alternate designations for default units.
        for alias in alias_list:
            self.main_dict[name].update({alias: (1.0, 0)})
            self.main_dict[name].update({alias.lower(): (1.0, 0)})
            self.main_dict[name].update({alias.upper(): (1.0, 0)})

    def add_user_units(self, default_units, user_units, multiplier, offset=0.0):
        """Add user units to `self.main_dict`."""
        self.main_dict[default_units].update({user_units: (multiplier, offset)})
        self.main_dict[default_units].update({user_units.lower(): (multiplier, offset)})
        self.main_dict[default_units].update({user_units.upper(): (multiplier, offset)})

    def get_conversion(self, default_units, user_units):
        """Get multiplier and offset for `user_units`."""
        try:
            multiplier, offset = self.main_dict[default_units][user_units]
        except:
            raise ValueError(f"Units not recognized")

        return multiplier, offset  # multiplier is (user_units / default_units)

    def convert_to_user(self, default_value, default_units, user_units):
        """Convert `default_value` with `default_units` to value with `user_units`.

        Parameters
        ----------
        default_value : float
            value in default `py_cea` units
        default_units : str
            valid name of default `py_cea` units
        user_units : str
            name of user units
        """
        multiplier, offset = self.get_conversion(default_units, user_units)
        return default_value * multiplier + offset

    def convert_to_default(self, user_value, user_units, default_units):
        """Convert `user_value` with `user_units` to value with `default_units`.

        Parameters
        ----------
        user_value : float
            value in user units
        user_units : str
            name of user units
        default_units : str
            valid name of default `py_cea` units
        """
        multiplier, offset = self.get_conversion(default_units, user_units)
        return (user_value - offset) / multiplier

    def print_default_units(self):
        """Print the default units of `py_cea`."""
        for key in self.main_dict.keys():
            print(key)

    def print_user_units(self, default_units):
        """Print the user units of `py_cea`."""
        for key in self.main_dict[default_units].keys():
            print(key)


u = Units()

# the following are the default units for interacting with py_cea
u.add_default_unit("psia")
u.add_default_unit("sec", ["lbf sec/lbm", "lbf-sec/lbm"])  # refers to Isp seconds.
u.add_default_unit("degR", ["R"])
u.add_default_unit("ft/sec", ["fps"])
u.add_default_unit("BTU/lbm")
u.add_default_unit("lbm/cuft")
u.add_default_unit("BTU/lbm degR", ["BTU/lbm-degR", "BTU/lbm R", "BTU/lbm-R"])
u.add_default_unit("millipoise")
u.add_default_unit(
    "mcal/cm-K-s", ["mcal/cm-degK-sec", "mcal/cm-degC-s", "millical/cm-degK-sec"]
)

# add units for pressure
u.add_user_units("psia", "MPa", 0.00689475729)
u.add_user_units("psia", "kPa", 6.89475729)
u.add_user_units("psia", "Pa", 6894.75729)
u.add_user_units("psia", "Bar", 0.0689475729)
u.add_user_units("psia", "Atm", 0.068046)
u.add_user_units("psia", "Torr", 51.7149)

# add units for temperature
u.add_user_units("degR", "degK", 5.0 / 9.0)
u.add_user_units("degR", "K", 5.0 / 9.0)
u.add_user_units("degR", "degC", 5.0 / 9.0, -273.15)
u.add_user_units("degR", "C", 5.0 / 9.0, -273.15)
u.add_user_units("degR", "degF", 1.0, -459.67)
u.add_user_units("degR", "F", 1.0, -459.67)

# add units for Isp
u.add_user_units("sec", "N sec/kg", 9.80665)
u.add_user_units("sec", "N s/kg", 9.80665)
u.add_user_units("sec", "N-sec/kg", 9.80665)
u.add_user_units("sec", "N-s/kg", 9.80665)
u.add_user_units("sec", "m/sec", 9.80665)
u.add_user_units("sec", "m/s", 9.80665)
u.add_user_units("sec", "km/s", 9.80665 / 1000.0)
u.add_user_units("sec", "km/sec", 9.80665 / 1000.0)

# add units for velocity
u.add_user_units("ft/sec", "m/sec", 0.3048)
u.add_user_units("ft/sec", "m/s", 0.3048)

# add units for enthalpy
u.add_user_units("BTU/lbm", "J/g", 2.3244462314030762)
u.add_user_units("BTU/lbm", "kJ/kg", 2.3244462314030762)
u.add_user_units("BTU/lbm", "J/kg", 2324.446231403076)
u.add_user_units("BTU/lbm", "kcal/kg", 0.5555565908154452)
u.add_user_units("BTU/lbm", "cal/g", 0.5555565908154452)
u.add_user_units("BTU/lbm", "ft lbf/lbm", 777.7783085697629)
u.add_user_units("BTU/lbm", "ft-lbf/lbm", 777.7783085697629)

# add units for heat capacity
u.add_user_units("BTU/lbm degR", "kJ/kg degK", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg K", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg degC", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg C", 4.1868)

u.add_user_units("BTU/lbm degR", "J/kg degK", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg K", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg degC", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg C", 4186.8)

u.add_user_units("BTU/lbm degR", "cal/g degK", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g K", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g degC", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g C", 1.0)

u.add_user_units("BTU/lbm degR", "kJ/kg-degK", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg-K", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg-degC", 4.1868)
u.add_user_units("BTU/lbm degR", "kJ/kg-C", 4.1868)

u.add_user_units("BTU/lbm degR", "J/kg-degK", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg-K", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg-degC", 4186.8)
u.add_user_units("BTU/lbm degR", "J/kg-C", 4186.8)

u.add_user_units("BTU/lbm degR", "cal/g-degK", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g-K", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g-degC", 1.0)
u.add_user_units("BTU/lbm degR", "cal/g-C", 1.0)

# add units for density
u.add_user_units("lbm/cuft", "g/cc", 0.016018463)
u.add_user_units("lbm/cuft", "sg", 0.016018463)
u.add_user_units("lbm/cuft", "kg/m^3", 16.018463374)

# add units for dynamic viscosity
u.add_user_units("millipoise", "centipoise", 0.1)
u.add_user_units("millipoise", "poise", 0.001)
u.add_user_units("millipoise", "lbf-sec/sqin", 1.4503773779686e-8)
u.add_user_units("millipoise", "lbf-sec/sqft", 0.0000020885434224573)
u.add_user_units("millipoise", "lbm/ft-sec", 0.0000671968994813)
u.add_user_units("millipoise", "lbm/in-sec", 0.0000671968994813 / 12.0)
u.add_user_units("millipoise", "Pa-s", 0.0001)
u.add_user_units("millipoise", "Pa-sec", 0.0001)

# add units for thermal conductivity
u.add_user_units("mcal/cm-K-s", "BTU/hr-ft-degF", 241.747 / 1000.0)
u.add_user_units("mcal/cm-K-s", "BTU/s-in-degF", 0.005596 / 1000.0)
u.add_user_units("mcal/cm-K-s", "cal/s-cm-degC", 1.0 / 1000.0)
u.add_user_units("mcal/cm-K-s", "cal/s-m-degC", 100.0 / 1000.0)
u.add_user_units("mcal/cm-K-s", "W/cm-degC", 4.184 / 1000.0)
u.add_user_units("mcal/cm-K-s", "W/m-K", 4.184 / 1.0e-5)

if __name__ == "__main__":
    u.convert_to_user(1000, "psia", "bar")
    u.convert_to_default(100, "bar", "psia")
