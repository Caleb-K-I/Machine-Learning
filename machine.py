import pandas as pd

def prediction(data,modele,nb):
    import pandas as pd
    Liste = [nb]
    dataessaie=data.iloc[Liste]
    df=dataessaie[["Marque","reseau","Ram","écran","Mémoire","prix"]]
    y = df['prix']
    X= df.drop('prix', axis=1)
    pred = pd.DataFrame.from_dict({'predicted' : modele.predict(X), 'true': y})
    pred.true=pd.to_numeric(pred['true'])
    pred['difference']= pred.predicted - pred.true

    return pred