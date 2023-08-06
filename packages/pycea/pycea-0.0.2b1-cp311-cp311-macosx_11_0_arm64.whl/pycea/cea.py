from pycea.wrapper import Wrapper
from pycea.units import u


class CEA(object):
    def __init__(
        self,
        propName="",
        oxName="",
        fuelName="",
        units="default",
        isp_units="sec",
        cstar_units="ft/sec",
        pressure_units="psia",
        temperature_units="degR",
        sonic_velocity_units="ft/sec",
        enthalpy_units="BTU/lbm",
        density_units="lbm/cuft",
        specific_heat_units="BTU/lbm degR",
        viscosity_units="millipoise",
        thermal_cond_units="mcal/cm-K-s",
        fac_CR=None,
        make_debug_prints=False,
        makeOutput=0,
    ):
        """This object wraps the Wrapper class to enable user units and other functionality.

        Parameters
        ----------
        propName : str
            Name of the propellant. If propName is empty, then the propellant is assumed
            to be a blend of oxName and fuelName.
        oxName : str
            Name of the oxidizer.
        fuelName : str
            Name of the fuel.
        units : str
            Units to be used. Options are 'default', 'metric' or 'custom'. Either
            select a set of units or define your own by changing the units strings.
        isp_units : str
            Units for Isp. Options are 'sec', 'N-s/kg', 'm/s', 'km/s'.
        cstar_units : str
            Units for cstar. Options are 'ft/sec', 'm/s'.
        pressure_units : str
            Units for pressure. Options are 'psia', 'MPa', 'KPa', 'Pa', 'Bar', 'Atm', 'Torr'.
        temperature_units : str
            Units for temperature. Options are 'degR', 'K', 'C', 'F'.
        sonic_velocity_units : str
            Units for sonic velocity. Options are 'ft/sec', 'm/s'.
        enthalpy_units : str
            Units for enthalpy. Options are 'BTU/lbm', 'J/g', 'kJ/kg', 'J/kg', 'kcal/kg', 'cal/g'.
        density_units : str
            Units for density. Options are 'lbm/cuft', 'g/cc', 'sg', 'kg/m^3'.
        specific_heat_units : str
            Units for specific heat. Options are 'BTU/lbm degR', 'kJ/kg-K', 'cal/g-C', 'J/kg-K'.
        viscosity_units : str
            Units for viscosity. Options are 'millipoise', 'lbf-sec/sqin', 'lbf-sec/sqft',
            'lbm/ft-sec', 'poise', 'centipoise', 'Pa-s'.
        thermal_cond_units : str
            Units for thermal conductivity. Options are 'mcal/cm-K-s', 'millical/cm-degK-sec',
            'BTU/hr-ft-degF', 'BTU/s-in-degF', 'cal/s-cm-degC', 'W/cm-degC'.
        fac_CR : float
            Contraction Ratio of finite area combustor (None=infinite).
        make_debug_prints : bool
            If make_debug_prints is True, print debugging info to terminal.
        makeOutput : int
            If makeOutput is 1, then the CEA output file is written to file.

        Notes
        -----
        `pycea` wraps the NASA Fortran CEA code to calculate Isp, Tcomb etc.

        Examples
        --------
        >>> from pycea import CEA
        >>> CEA(oxName='LOX', fuelName='Ethanol', units='metric').get_Isp(Pc=40e5)
        308.20391303009785
        """

        self.units = units

        if self.units == ("default" or "custom" or "freedom"):  # :)
            self.isp_units = isp_units
            self.cstar_units = cstar_units
            self.pressure_units = pressure_units
            self.temperature_units = temperature_units
            self.sonic_velocity_units = sonic_velocity_units
            self.enthalpy_units = enthalpy_units
            self.density_units = density_units
            self.specific_heat_units = specific_heat_units
            self.viscosity_units = viscosity_units
            self.thermal_cond_units = thermal_cond_units
        elif self.units == "metric":
            self.isp_units = "sec"
            self.cstar_units = "m/s"
            self.pressure_units = "Pa"
            self.temperature_units = "K"
            self.sonic_velocity_units = "m/s"
            self.enthalpy_units = "J/kg"
            self.density_units = "kg/m^3"
            self.specific_heat_units = "J/kg-K"
            self.viscosity_units = "Pa-s"
            self.thermal_cond_units = "W/m-K"
        else:
            raise ValueError("CEA units must be 'default', 'metric', or 'custom'.")

        self.fac_CR = fac_CR

        self.wrapper = Wrapper(
            propName=propName,
            oxName=oxName,
            fuelName=fuelName,
            fac_CR=fac_CR,
            make_debug_prints=make_debug_prints,
            makeOutput=makeOutput,
        )
        self.desc = self.wrapper.desc

    def __call__(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        return self.get_Isp(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

    def get_IvacCstrTc(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspVac, Cstar, Tcomb = self.wrapper.get_IvacCstrTc(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        IspVac = u.convert_to_user(IspVac, "sec", self.isp_units)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return IspVac, Cstar, Tcomb

    def get_Frozen_IvacCstrTc(self, Pc=100.0, MR=1.0, eps=40.0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspFrozen, Cstar, Tcomb = self.wrapper.get_Frozen_IvacCstrTc(
            Pc=Pc, MR=MR, eps=eps, frozenAtThroat=frozenAtThroat
        )

        IspFrozen = u.convert_to_user(IspFrozen, "sec", self.isp_units)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return IspFrozen, Cstar, Tcomb

    def get_IvacCstrTc_exitMwGam(
        self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspVac, Cstar, Tcomb, mw, gam = self.wrapper.get_IvacCstrTc_exitMwGam(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        IspVac = u.convert_to_user(IspVac, "sec", self.isp_units)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return IspVac, Cstar, Tcomb, mw, gam

    def get_IvacCstrTc_ChmMwGam(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspVac, Cstar, Tcomb, mw, gam = self.wrapper.get_IvacCstrTc_ChmMwGam(
            Pc=Pc, MR=MR, eps=eps
        )

        IspVac = u.convert_to_user(IspVac, "sec", self.isp_units)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return IspVac, Cstar, Tcomb, mw, gam

    def get_IvacCstrTc_ThtMwGam(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspVac, Cstar, Tcomb, mw, gam = self.wrapper.get_IvacCstrTc_ThtMwGam(
            Pc=Pc, MR=MR, eps=eps
        )

        IspVac = u.convert_to_user(IspVac, "sec", self.isp_units)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return IspVac, Cstar, Tcomb, mw, gam

    def get_Isp(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        IspVac = self.wrapper.get_Isp(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )
        IspVac = u.convert_to_user(IspVac, "sec", self.isp_units)

        return IspVac

    def get_Cstar(self, Pc=100.0, MR=1.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Cstar = self.wrapper.get_Cstar(Pc=Pc, MR=MR)
        Cstar = u.convert_to_user(Cstar, "ft/sec", self.cstar_units)

        return Cstar

    def get_Tcomb(self, Pc=100.0, MR=1.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Tcomb = self.wrapper.get_Tcomb(Pc=Pc, MR=MR)
        Tcomb = u.convert_to_user(Tcomb, "degR", self.temperature_units)

        return Tcomb

    def get_PcOvPe(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        return self.wrapper.get_PcOvPe(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

    def get_eps_at_PcOvPe(
        self, Pc=100.0, MR=1.0, PcOvPe=1000.0, frozen=0, frozenAtThroat=0
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        return self.wrapper.get_eps_at_PcOvPe(
            Pc=Pc, MR=MR, PcOvPe=PcOvPe, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

    def get_Throat_PcOvPe(self, Pc=100.0, MR=1.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        return self.wrapper.get_Throat_PcOvPe(Pc=Pc, MR=MR)

    def get_MachNumber(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        return self.wrapper.get_MachNumber(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

    def get_Temperatures(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        tempList = self.wrapper.get_Temperatures(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        for i, T in enumerate(tempList):
            tempList[i] = u.convert_to_user(T, "degR", self.temperature_units)

        return tempList  # Tc, Tthroat, Texit

    def get_SonicVelocities(
        self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        sonicList = self.wrapper.get_SonicVelocities(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        for i, S in enumerate(sonicList):
            sonicList[i] = u.convert_to_user(S, "ft/sec", self.sonic_velocity_units)

        return sonicList  # Chamber, Throat, Exit

    def get_Chamber_SonicVel(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        sonicVel = self.wrapper.get_Chamber_SonicVel(Pc=Pc, MR=MR, eps=eps)

        sonicVel = u.convert_to_user(sonicVel, "ft/sec", self.sonic_velocity_units)
        return sonicVel

    def get_Enthalpies(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        hList = self.wrapper.get_Enthalpies(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        for i, H in enumerate(hList):
            hList[i] = u.convert_to_user(H, "BTU/lbm", self.enthalpy_units)

        return hList

    def get_SpeciesMassFractions(
        self,
        Pc=100.0,
        MR=1.0,
        eps=40.0,
        frozen=0,
        frozenAtThroat=0,
        min_fraction=0.000005,
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        molWtD, massFracD = self.wrapper.get_SpeciesMassFractions(
            Pc=Pc,
            MR=MR,
            eps=eps,
            frozenAtThroat=frozenAtThroat,
            min_fraction=min_fraction,
        )

        return molWtD, massFracD

    def get_SpeciesMoleFractions(
        self,
        Pc=100.0,
        MR=1.0,
        eps=40.0,
        frozen=0,
        frozenAtThroat=0,
        min_fraction=0.000005,
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")

        molWtD, moleFracD = self.wrapper.get_SpeciesMoleFractions(
            Pc=Pc,
            MR=MR,
            eps=eps,
            frozenAtThroat=frozenAtThroat,
            min_fraction=min_fraction,
        )

        return molWtD, moleFracD

    def get_Chamber_H(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        H = self.wrapper.get_Chamber_H(Pc=Pc, MR=MR, eps=eps)

        return u.convert_to_user(H, "BTU/lbm", self.enthalpy_units)

    def get_Densities(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        dList = self.wrapper.get_Densities(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        for i, d in enumerate(dList):
            dList[i] = u.convert_to_user(d, "lbm/cuft", self.density_units)

        return dList

    def get_Chamber_Density(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        H = self.wrapper.get_Chamber_Density(Pc=Pc, MR=MR, eps=eps)

        return u.convert_to_user(H, "lbm/cuft", self.density_units)

    def get_HeatCapacities(
        self, Pc=100.0, MR=1.0, eps=40.0, frozen=0, frozenAtThroat=0
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        cpList = self.wrapper.get_HeatCapacities(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen, frozenAtThroat=frozenAtThroat
        )

        for i, cp in enumerate(cpList):
            cpList[i] = u.convert_to_user(cp, "BTU/lbm degR", self.specific_heat_units)

        return cpList

    def get_Chamber_Cp(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Cp = self.wrapper.get_Chamber_Cp(Pc=Pc, MR=MR, eps=eps)

        return u.convert_to_user(Cp, "BTU/lbm degR", self.specific_heat_units)

    def get_Throat_Isp(self, Pc=100.0, MR=1.0, frozen=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Isp = self.wrapper.get_Throat_Isp(Pc=Pc, MR=MR, frozen=frozen)
        Isp = u.convert_to_user(Isp, "sec", self.isp_units)

        return Isp

    def get_Chamber_MolWt_gamma(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        return self.wrapper.get_Chamber_MolWt_gamma(Pc=Pc, MR=MR, eps=eps)

    def get_Throat_MolWt_gamma(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        return self.wrapper.get_Throat_MolWt_gamma(Pc=Pc, MR=MR, eps=eps, frozen=frozen)

    def get_exit_MolWt_gamma(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        return self.wrapper.get_exit_MolWt_gamma(Pc=Pc, MR=MR, eps=eps)

    def get_eqratio(self, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        return self.wrapper.get_eqratio(Pc=Pc, MR=MR, eps=eps)

    def get_MRforER(self, ERphi=None, ERr=None):
        return self.wrapper.get_MRforER(ERphi=ERphi, ERr=ERr)

    def get_description(self):
        return self.wrapper.get_description()

    def estimate_Ambient_Isp(
        self, Pc=100.0, MR=1.0, eps=40.0, Pamb=14.7, frozen=0, frozenAtThroat=0
    ):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Pamb = u.convert_to_default(Pamb, self.pressure_units, "psia")
        IspAmb, mode = self.wrapper.estimate_Ambient_Isp(
            Pc=Pc,
            MR=MR,
            eps=eps,
            Pamb=Pamb,
            frozen=frozen,
            frozenAtThroat=frozenAtThroat,
        )

        IspAmb = u.convert_to_user(IspAmb, "sec", self.isp_units)

        return IspAmb, mode

    def get_PambCf(self, Pamb=14.7, Pc=100.0, MR=1.0, eps=40.0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Pamb = u.convert_to_default(Pamb, self.pressure_units, "psia")

        CFcea, CF, mode = self.wrapper.get_PambCf(Pamb=Pamb, Pc=Pc, MR=MR, eps=eps)

        return CFcea, CF, mode

    def get_Frozen_PambCf(self, Pamb=0.0, Pc=100.0, MR=1.0, eps=40.0, frozenAtThroat=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Pamb = u.convert_to_default(Pamb, self.pressure_units, "psia")

        CFcea, CFfrozen, mode = self.wrapper.get_Frozen_PambCf(
            Pamb=Pamb, Pc=Pc, MR=MR, eps=eps, frozenAtThroat=frozenAtThroat
        )

        return CFcea, CFfrozen, mode

    def get_Chamber_Transport(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Cp, visc, cond, Prandtl = self.wrapper.get_Chamber_Transport(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen
        )

        Cp = u.convert_to_user(Cp, "BTU/lbm degR", self.specific_heat_units)
        visc = u.convert_to_user(visc, "millipoise", self.viscosity_units)
        cond = u.convert_to_user(cond, "mcal/cm-K-s", self.thermal_cond_units)

        return Cp, visc, cond, Prandtl

    def get_Throat_Transport(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Cp, visc, cond, Prandtl = self.wrapper.get_Throat_Transport(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen
        )

        Cp = u.convert_to_user(Cp, "BTU/lbm degR", self.specific_heat_units)
        visc = u.convert_to_user(visc, "millipoise", self.viscosity_units)
        cond = u.convert_to_user(cond, "mcal/cm-K-s", self.thermal_cond_units)

        return Cp, visc, cond, Prandtl

    def get_Exit_Transport(self, Pc=100.0, MR=1.0, eps=40.0, frozen=0):
        Pc = u.convert_to_default(Pc, self.pressure_units, "psia")
        Cp, visc, cond, Prandtl = self.wrapper.get_Exit_Transport(
            Pc=Pc, MR=MR, eps=eps, frozen=frozen
        )

        Cp = u.convert_to_user(Cp, "BTU/lbm degR", self.specific_heat_units)
        visc = u.convert_to_user(visc, "millipoise", self.viscosity_units)
        cond = u.convert_to_user(cond, "mcal/cm-K-s", self.thermal_cond_units)

        return Cp, visc, cond, Prandtl


def test():
    print(CEA(oxName="N2O", fuelName="Isopropanol", units="metric").get_Isp(Pc=25e5))

if __name__ == "__main__":
    test()
