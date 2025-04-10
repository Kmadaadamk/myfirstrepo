import pandas as pd


def excel_parser(path_of_excel):
    ds=pd.read_excel(path_of_excel,engine="odf")
    ds=ds.fillna("")
    return ds[["Modell","Anzahl_Netzteile","Leistung","Standard","Eff_active","P_idle "]]





#print(excel_parser("blauerEngSimList.ods"))