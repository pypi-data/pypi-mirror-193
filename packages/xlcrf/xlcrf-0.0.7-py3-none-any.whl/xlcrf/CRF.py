import numpy as np
import pandas as pd
import xlsxwriter

debug = False

# numero di righe per cui è possibile inserire dati. Le altre son bloccate
n_fillable_rows = 10000 
protection_pw = 'asd'

def import_validate(x):
    if (pd.isna(x)):
        return x
    elif (x == 'intero'):
        return "integer"
    elif (x == 'decimale'):
        return "decimal"
    elif (x == 'elenco'):
        return "list"
    elif (x == 'data'):
        return "date"
    elif (x == 'ora'):
        return "time"
    elif (x == 'testo'):
        return "any"

def import_criteria(x):
    if (pd.isna(x)):
        return x
    elif (x == 'tra'):
        return 'between'
    elif (x == 'non compreso tra'):
        return 'not between'
    else:
        return x

# def import_sino(x):
#     if (pd.isna(x)):
#         return x
#     else:
#         return x == 'Sì'

def select_modalita(x, modalita, variabile, sheetname):
    # ottieni modalità per elenchi: se specificato
    # prendile da modalita (se disponibile) se no imposta a np.nan
    if (pd.isna(x)):
        return x
    else:
        if (x in modalita):
            return modalita[x]
        else:
            raise LookupError("l'id_elenco '" +x + "' non è specificato nella scheda 'modalita_output' ma viene richiesto per la variabile '" + variabile +"' (foglio '"+ sheetname + "'). Rettificare.")
    
class Column:
    def __init__(self, prog, struct, modalita, sheetname, debug = debug):
        # posizione, nome variabile e descrizione
        self.index         = prog
        self.variable      = struct['variabile']
        # self.description   = struct['descrizione_e_unita_misura']
        # debug info
        if (debug):
            print("importing " + self.variable)
        self.validation = {
            'validate'      : import_validate(struct['tipo']),
            'source'        : select_modalita(struct['id_elenco'],
                                              modalita,
                                              struct['variabile'],
                                              sheetname),
            'criteria'      : import_criteria(struct['criterio']),
            'value'         : struct['valore'],
            'minimum'       : struct['minimo'],
            'maximum'       : struct['massimo'],
            # ---------------------------------------
            'ignore_blank'  : True,
            'dropdown'      : True,
            'show_input'    : True,
            # 'ignore_blank'  : import_sino(struct['ignora_celle_vuote']),
            # 'dropdown'      : import_sino(struct['elenco_nella_cella']),
            # 'show_input'    : import_sino(struct['input_mostra']),
            # ---------------------------------------
            'input_title'   : (struct['input_titolo'])[:32],
            'input_message' : struct['input_messaggio'],
            # ---------------------------------------
            'show_error'    : True,
            # 'show_error'    : import_sino(struct['errore_mostra']),
            # ---------------------------------------
            'error_type'    : "stop",
            # 'error_type'    : struct['errore_tipo'],
            # ---------------------------------------
            'error_title'   : "Inserimento erroneo",
            # 'error_title'   : struct['errore_titolo'],
            'error_message' : struct['errore_messaggio']
        }

    def export(self, ws, debug = debug):
        prog_col = self.index
        # title
        ws.write(0, prog_col, self.variable)
        if (debug):
            print("exporting " + self.variable)
        # data validation from 1 to fillable_rows
        validation_dict = {
            # tieni se è una lista (per le modalità) o se non è NA
            d:v for d,v in self.validation.items()
            if isinstance(v, list) or not pd.isna(v)
        }
        # debug info
        if (debug):
            print(validation_dict)
        ws.data_validation(1, prog_col, n_fillable_rows, prog_col,
                           validation_dict)

        
class Sheet:
    def __init__(self, xl, sheetname, modalita, debug = debug):
        sheet = xl.parse(sheetname).dropna(how = 'all')
        sheet = sheet.reset_index()
        if (debug):
            print(sheet)
        self.sheetname = sheetname
        # estrai i dati delle colonne dell'output
        # ciclando sulle righe del data.frame di input
        self.columns = []
        for index, row in sheet.iterrows():
            self.columns.append(Column(index, row, modalita, sheetname))

    def export(self, ws, formats, debug = debug):
        # Data
        for c in self.columns:
            c.export(ws)
        # formatting the worksheet
        ws.set_row(0, cell_format = formats['title'])
        # blocca riquadri
        ws.freeze_panes('A2')
        # protezione della prima riga da modifiche
        for r in range(1, n_fillable_rows):
            ws.set_row(row = r, cell_format = formats['unlocked'])
        # Meglio farlo a mano se no non si riescono a fare modifiche alla
        # larghezza colonne
        # ws.protect(password = protection_pw)


def parse_modalita(df):
    grouped = df.groupby('id_elenco')
    modalita = {}
    for name, group in grouped:
        modalita[name] = list(group['modalita'])
    return modalita
        
        
class CRF:
    def __init__(self):
        # a CRF is a dict of sheets (each called by its name)
        self.sheets = {}
        
    def read_structure(self, f, debug = debug):
        """
        Import a dataset structure
        """
        print("Reading structure file: " + f)
        xl = pd.ExcelFile(f)

        # importa le modalità impiegate
        modalita = parse_modalita(df = xl.parse('modalita_output'))
        
        # importa gli sheet e dai le modalita come dict
        data_sheets = [s for s in xl.sheet_names if s not in
                       ['modalita_output', 'modalita_struttura']]
        for s in data_sheets:
            self.sheets[s] = Sheet(xl, s, modalita)

    def create(self, f, debug = debug):
        """
        Create an xlsx template according to the structure
        """
        print("Creating CRF file: " + f)
        wb = xlsxwriter.Workbook(f)
        formats = {
            'title' : wb.add_format({'bold': True}),
            'unlocked' : wb.add_format({'locked': False})
        }
        # raw data
        for k, s in self.sheets.items():
            ws = wb.add_worksheet(k)
            s.export(ws, formats)
        wb.close()
