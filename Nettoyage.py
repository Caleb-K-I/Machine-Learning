def nettoyage_marque(fichier):
    fichier['Marque'] = fichier['Marque'].str.extract(r'(Samsung|Apple|Huawei|TWS|Xiaomi|Sony|JBL|Beats|SAMSUNG|Jbl|HUAWEI|AKG|APPLE|Lenovo|LIVOO|Redmi|AUKEY|Google|Sony|Asus|Cubot|Nokia|Alcatel|Oneplus|Honor|Nubia|BlackBerry|Oukitel|ASUS|REALME|OPPO|Realme|LG|Nubia|OUKITEL|Nokia| BlackBerry| Realme| APPLE| Alcatel| Asus| Samsung| Apple| OPPO| Google| Sony| ASUS| LG| HUAWEI| Huawei| Honor| Xiaomi|OnePlus|)')
    for i in range(len(fichier)):
        if len(fichier['Marque'][i])==0:
            fichier['Marque'][i]="Inconnu"
    fichier['Marque'] = [x.lower() for x in fichier['Marque']]
    

    
    
def nettoyage_ecran(fichier):
    for i in range(len(fichier)):
        obool=True
        if fichier['écran'][i][:3]!="['E" or fichier['reseau'][i][:4]!="['Ré":
            fichier.drop(i,0,inplace=True)
    fichier['écran'] = [x.replace( "['Ecran ","") for x in fichier['écran']]
    fichier['écran'] = fichier['écran'].str[:-3]
    fichier=fichier.reset_index()
    
    
    
def nettoyage_reseau(fichier):
    fichier.loc[fichier["reseau"] == "['Réseau 5G']","reseau"] ="5G"
    fichier.loc[fichier["reseau"] == "['Réseau 4G']","reseau"] = "4G"
    fichier.loc[fichier["reseau"] == "['Réseau 3G']","reseau"] = "3G"

    
def nettoyage_prix(fichier):
    fichier['prix'] = [x.replace( "['","") for x in fichier['prix']]
    fichier['prix'] = [x.replace( " €']","") for x in fichier['prix']]
    fichier['prix'] = [x.replace(',', '.') for x in fichier['prix']]
    fichier['prix'] = [x.replace( " ","") for x in fichier['prix']]
    fichier['prix'] = [x.strip() for x in fichier['prix']]
    fichier['prix'] = [x.replace( "nan","100") for x in fichier['prix']]
    try:
        fichier['prix']=pd.to_numeric(fichier['prix'])
    except:
        print()
    
    
    
    
def nettoyage_exploit(fichier):
    fichier['exploit'] = [x.replace( "['","") for x in fichier['exploit']]
    fichier['exploit'] = [x.replace( "']","") for x in fichier['exploit']]
    
    
    
    
def col_Ram(fichier):
    Ram=[]
    for i in range(len(fichier.exploit)):
        try :
            head, sep, tail = fichier.exploit.iloc[i].partition('/')
            if tail=="":
                carac="Inconnu"
            else:
                carac=tail
        except:
            print()
        Ram.append(carac)

    fichier['Ram']=Ram 
    fichier['Ram'] = [x.replace( "Series 60 v5.0","Inconnu") for x in fichier['Ram']]
    fichier['Ram'] = [x.replace( "Series 60 3.1 Edition","Inconnu") for x in fichier['Ram']]
    

    
def cor_exploit(fichier):
    exploit=[]
    for i in range(len(fichier.exploit)):
        try :
            head, sep, tail = fichier.exploit.iloc[i].partition('/')
            carac=head
        except:
            print()
        exploit.append(carac)

    fichier['exploit']=exploit 
    
    
    
def col_memoire(fichier):
    memoire=[]
    for i in range(len(fichier.exploit)):
        try :
            head, sep, tail = fichier.exploit.iloc[i].partition('Mémoire')
            if tail=="":
                carac="Inconnu"
            else:
                carac=tail
        except:
            print()
        memoire.append(carac)

    fichier['Mémoire']=memoire
    fichier['Mémoire'] = [x.replace( "Go","") for x in fichier['Mémoire']]
    
    

 