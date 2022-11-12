import json

with open('vela_data.json') as f:
        df = json.load(f)


for k in df['tema'].keys():
    df['tema'][k] = df['tema'][k].replace('\n','')


with open('vela_data.json', 'w') as file:
    json.dump(df, file, indent=1)



# 1-Vero, 2-Falso


# Funzioni di salvataggio
def salvataggio(lista):
    with open('saved.json', 'r') as file:
        list_wrong_questions = json.load(file)
    new = []
    for q in list_wrong_questions:
        if q in data['domande_salvate_base']:
            pass
        else:
            new.append(q)
    data['domande_salvate_base'].extend(new)

    with open('saved.json', 'w') as file:
        json.dump(data, file)


def cancella_memoria():
    warning = mb.askyesno("Attenzione",
                          "Attenzione!\nTutti i dati salvati andranno persi.\nSei sicuro di voler continuare?")
    if warning == True:
        with open('saved.json', 'w') as f:
            data = {}
            data['domande_salvate'] = list()
            json.dump(data, f)
        mb.showinfo('formattazione', 'Tutti i dati sono stati cancellati!')

    else:
        pass
