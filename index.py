read_file  = open('PresupuestoCodigo.csv', 'r')
write_file = open('out2024.csv', 'w'); 
write_file.write(':Clase;:Subclase;:Producto;Codigo;Fecha;Concepto;Valor;x; \n')

_list_month   = ['2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30', '2024-05-31', '2024-06-30', '2024-07-31', '2024-08-31', '2024-09-30', '2024-10-31', '2024-11-30', '2024-12-31']
_list_concept = ['Kilos', 'Imp Cont (sin com/S rappel)', 'Margen Contri', 'eur/kg', '']
_clase    = ''
_subclase = ''
_producto = ''
_codigo   = ''

for lineInit in read_file:
    lineArray = lineInit.split(';')
    if len(str(lineArray[3])) < 7 : continue

    _clase    = str(lineArray[0]) 
    _subclase = str(lineArray[1])
    _producto = str(lineArray[2])
    _codigo   = str(lineArray[3])

    _concept_counter = 3
    for _fecha in _list_month:
        
        for _concept in _list_concept:
            _concept_counter = _concept_counter + 1
            if _concept == '': continue
            _value = str(lineArray[_concept_counter]).replace('.', '')
            write_file.write(_clase+';'+_subclase+';'+_producto+';'+_codigo+';'+_fecha+';'+_concept+';'+_value+';x \n')

        
       

    

    