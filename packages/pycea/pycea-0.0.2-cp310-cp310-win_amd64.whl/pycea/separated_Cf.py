import pycea.isp as isp


def ambientCf(gam=1.25, epsTot=20.0, Pc=200.0, Pamb=14.7):
    PcOvPe = isp.CalcPCoPE(gam, epsTot)

    if Pamb > 0.0:
        (
            CfOvCfvacAtEsep,
            CfOvCfvac,
            Cfsep,
            CfiVac,
            CfiAmbSimple,
            CfVac,
            epsSep,
            Psep,
        ) = sepNozzleCf(gam, epsTot, Pc, Pamb)
    else:
        CfVac = isp.CalcCFvac(gam, PcOvPe)
        Psep = 0.0

    Pexit = Pc / PcOvPe

    if Pexit > Psep:
        # print(  'Not Separated, Cfsep =',Cfsep)
        # print(  'CfVac - Pamb*epsTot/Pc = ',CfVac - Pamb*epsTot/Pc)
        Cf = CfVac - Pamb * epsTot / Pc

        if Pexit > Pamb:
            mode = f"UnderExpanded Pe={Pexit:g}"
        else:
            mode = f"OverExpanded Pe={Pexit:g}"
    else:
        # print(  'separated, Cfsep =',Cfsep)
        # print(  'Simplified Cfsep =',CfiAmbSimple)
        Cf = Cfsep
        mode = f"Separated Psep={Psep:g}, epsSep={epsSep:.1f}"
    CfOverCfvac = Cf / CfVac

    return Cf, CfOverCfvac, mode


def sepNozzleCf(gam=1.25, epsTot=20.0, Pc=200.0, Pamb=14.7):
    """Uses approach of Sherwin Kalt and David Badal as in:
    "Conical Rocket Nozzle Performance under Flow Separated Conditions"

    This routine calculates an efficiency factor to apply to the
    Ispvac or Cfvac of the nozzle

    IspAmb = CfOvCfvac * IspVac

    or to the vacuum performance of the nozzle at the separation point

    IspAmb = CfOvCfvacAtEsep * IspVac(at epsSep)
    """

    PcOvPe = isp.CalcPCoPE(gam, epsTot)
    CfVac = isp.CalcCFvac(gam, PcOvPe)

    # this is Kalt&Badal correlation for Pi (incipient separation pressure)
    PiOvPa = (2.0 / 3.0) * (Pc / Pamb) ** (-0.2)
    Pi = PiOvPa * Pamb
    Psep = Pi

    # area ratio and Cfvac that correspond to the point of Pi
    epsSep = isp.CalcEps(gam, Pc / Pi)
    epsSep = epsSep

    PcOvPesep = isp.CalcPCoPE(gam, epsSep)
    CfiVac = isp.CalcCFvac(gam, PcOvPesep)

    CfiAmbSimple = CfiVac - Pamb * epsSep / Pc

    # eps95 is the area ratio at which the internal pressure = 0.95 * Pamb
    # c = result of simultaneous solution of eps95 = epsSep + (epsSep-1)/2.4 = epsSep + (epsTot-epsSep)/1.45
    c = 2.4 / 1.45
    if epsSep <= epsTot * c / (1.0 + c) + 1.0 / (1.0 + c):
        eps95 = epsSep + (epsSep - 1) / 2.4
    else:
        eps95 = epsSep + (epsTot - epsSep)

    P95 = 0.95 * Pamb

    cf_integral_iTo95 = 0.55 * (Pi + P95) * (eps95 - epsSep) / Pc
    cf_integral_95ToExit = (0.975 * eps95 + 0.025 * epsTot) * Pamb / Pc

    Cf = CfiVac + cf_integral_iTo95 - cf_integral_95ToExit

    CfOvCfvac = Cf / CfVac
    CfOvCfvacAtEsep = Cf / CfiVac
    return CfOvCfvacAtEsep, CfOvCfvac, Cf, CfiVac, CfiAmbSimple, CfVac, epsSep, Psep


if __name__ == "__main__":
    import csv

    csvfilename = "separated_nozzle.csv"
    print("Saving data to CSV file", csvfilename)
    csv_writer = csv.writer(open(csvfilename, "w"), dialect="excel")
    csv_writer.writerow(
        [
            "gam",
            "EpsTot",
            "Pc",
            "Pamb",
            "IspVac_AtEpsTot",
            "IspAmb_Separated",
            "IspAmb_Simple",
            "Cf/Cfvac_AtEpsTot",
            "Cf/Cfvac_AtEpsSep",
            "Cf",
            "CfiVac",
            "CfiAmbSimple",
            "CfVac",
            "EpsSep",
        ]
    )

    gam, epsTot, Pc, Pamb = 1.25, 25.0, 200.0, 14.7
    IspVac = 316.0

    (
        CfOvCfvacAtEsep,
        CfOvCfvac,
        Cfsep,
        CfiVac,
        CfiAmbSimple,
        CfVac,
        epsSep,
        Psep,
    ) = sepNozzleCf(gam=gam, epsTot=epsTot, Pc=Pc, Pamb=Pamb)
    IspAmb = IspVac * CfOvCfvac
    IspSimpleAtEsep = IspVac * CfiAmbSimple / CfVac

    csv_writer.writerow(
        [
            gam,
            epsTot,
            Pc,
            Pamb,
            IspVac,
            IspAmb,
            IspSimpleAtEsep,
            CfOvCfvac,
            CfOvCfvacAtEsep,
            Cfsep,
            CfiVac,
            CfiAmbSimple,
            CfVac,
            epsSep,
        ]
    )
    print(f"gam={gam:g}, epsTot={epsTot:g}, Pc={Pc:g}, Pamb={Pamb:g}")
    print("CfOvCfvacAtEsep, CfOvCfvac", CfOvCfvacAtEsep, CfOvCfvac)
    print("Cfsep, CfiAmbSimple", Cfsep, CfiAmbSimple)
    print("CfiVac CfVac", CfiVac, CfVac)
    print("epsSep", epsSep)
    print()

    Pc = 250.0
    epsTot = 20.45
    IspVac = 321.3
    (
        CfOvCfvacAtEsep,
        CfOvCfvac,
        Cfsep,
        CfiVac,
        CfiAmbSimple,
        CfVac,
        epsSep,
        Psep,
    ) = sepNozzleCf(gam=gam, epsTot=epsTot, Pc=Pc, Pamb=Pamb)
    IspAmb = IspVac * CfOvCfvac
    IspSimpleAtEsep = IspVac * CfiAmbSimple / CfVac

    csv_writer.writerow(
        [
            gam,
            epsTot,
            Pc,
            Pamb,
            IspVac,
            IspAmb,
            IspSimpleAtEsep,
            CfOvCfvac,
            CfOvCfvacAtEsep,
            Cfsep,
            CfiVac,
            CfiAmbSimple,
            CfVac,
            epsSep,
        ]
    )
    print(f"gam={gam:g}, epsTot={epsTot:g}, Pc={Pc:g}, Pamb={Pamb:g}")
    print("CfOvCfvacAtEsep, CfOvCfvac", CfOvCfvacAtEsep, CfOvCfvac)
    print("Cfsep, CfiAmbSimple", Cfsep, CfiAmbSimple)
    print("CfiVac CfVac", CfiVac, CfVac)
    print("epsSep", epsSep)
    print()

    ambientCf(gam=1.25, epsTot=20.0, Pc=200.0, Pamb=14.7)
