import PyPDF2 
def lector_de_factura_simple(path): 
    filtros = (""," ","\n")
    archivo = open(path,"rb")
    reader = PyPDF2.PdfReader(archivo)
    pagina = reader.pages[0]
    aux1=[]
    aux2=[]
    contador = 0
    usarVisitanteDolar = False
    resultado={
        'Fecha de Emisión:':[],
        'Razón Social:':[],
        'CUIT:':[],
        'Punto de Venta:':[],
        'Comp. Nro:':[],
        'Nombre:':[],
        'Condicion Frente al IVA':[]
    }
    def determinante_de_funcion(text,nn,tm,nnn,nnnn):
        x = tm[4]
        y = tm[5]
        
        if x < 450 and x>490 and y < 200 and y > 330 and text == "USD":
            usarVisitanteDolar = True
        else:
         pass
     
    def visitante(text,nn,tm,nnn,nnnn):
        
        y=tm[5]
        x=tm[4]
        if text not in filtros:
            print([text,x,y])
            if y >175 and y < 295:
                if x<540:
                    aux1.append([text,x,y])
                else:
                    aux2.append([text,x,y])
            if text == "USD":
                print([text,x,y])
            if x > 341  and x <500 and y >=732 and y<=733:
                resultado['Fecha de Emisión:'].append(text)
            elif x < 290  and x>21 and y >=720 and y<=732:
                resultado['Razón Social:'].append(text)
            elif x >341 and x < 380 and y >=709 and y <= 710:
                resultado['CUIT:'].append(text)
            elif x >341 and x <418 and y >=747 and y <= 748:
                resultado['Punto de Venta:'].append(text)
            elif x >462 and x <520 and y >= 747 and y <=748:
                resultado['Comp. Nro:'].append(text)
            elif x >1 and x <82 and y >= 750 and y <= 766:
                resultado["Nombre:"].append(text)
            elif x <290 and x > 22 and y >= 682 and y <= 683:
                resultado["Condicion Frente al IVA"].append(text)
            """elif x < 600 and x >540 and y >= 306 and y <=307:
                if "Importe Neto Gravado: $" in resultado.keys():
                    resultado["Importe Neto Gravado: $"].append(text)
                else:
                    resultado["Importe Neto Gravado: $"]= [text]"""
            
            
    def visitanteDolar(text,nn,tm,nnn,nnnn):
        
        y=tm[5]
        x=tm[4]
        if text not in filtros:
            if y >175 and y < 295:
                if x<540:
                    aux1.append([text,x,y])
                else:
                    aux2.append([text,x,y])
            if x > 341  and x <500 and y >=732 and y<=733:
                resultado['Fecha de Emisión:'].append(text)
            elif x < 290  and x>21 and y >=720 and y<=732:
                resultado['Razón Social:'].append(text)
            elif x >341 and x < 380 and y >=709 and y <= 710:
                resultado['CUIT:'].append(text)
            elif x >341 and x <418 and y >=747 and y <= 748:
                resultado['Punto de Venta:'].append(text)
            elif x >462 and x <520 and y >= 747 and y <=748:
                resultado['Comp. Nro:'].append(text)
            elif x >1 and x <82 and y >= 750 and y <= 766:
                resultado["Nombre:"].append(text)
            elif x <290 and x > 22 and y >= 682 and y <= 683:
                resultado["Condicion Frente al IVA"].append(text)
                """ elif y >= 177 and y <=178:
                    if "Obs" in resultado.keys():
                        resultado["Obs"].append(text)
                    else:
                        resultado["Obs"] = [text] """
                    
            elif x < 600 and x >540 and y >= 294 and y <=295:
                if "IVA 27%: $" in resultado.keys():
                    resultado["IVA 27%: $"].append(text)
                else:
                    resultado["IVA 27%: $"] = [text]
            elif x < 600 and x >540 and y >= 281 and y <=282:
                if "IVA 21%: $" in resultado.keys():
                    resultado["IVA 21%: $"].append(text)
                else:
                    resultado["IVA 21%: $"] = [text]
            elif x < 600 and x >540 and y >= 268 and y <=269:
                if "IVA 10.5%: $" in resultado.keys():
                    resultado["IVA 10.5%: $"].append(text)
                else:
                    resultado["IVA 10.5%: $"] = [text]
            elif x < 600 and x >540 and y >= 255 and y <=256:
                if "IVA 5%: $" in resultado.keys():
                    resultado["IVA 5%: $"].append(text)
                else:
                    resultado["IVA 5%: $"] = [text]
            elif x < 600 and x >540 and y > 242 and y <=243:
                if "IVA 2.5%: $" in resultado.keys():
                    resultado["IVA 2.5%: $"].append(text)
                else:
                    resultado["IVA 2.5%: $"]=[text]
                    
            elif x < 600 and x >540 and y >= 202 and y <=216:
                if "IVA 0%: $" in resultado.keys():
                    resultado["IVA 0%: $"].append(text)
                else:
                    resultado["IVA 0%: $"] = [text]
                    
            elif x < 600 and x >540 and y >= 306 and y <=307:
                if "Importe Neto Gravado: $" in resultado.keys():
                    resultado["Importe Neto Gravado: $"].append(text)
                else:
                    resultado["Importe Neto Gravado: $"]= [text]
                
            elif x < 600 and x >540 and y >= 200 and y <=201:
                if "Importe Total: $" in resultado.keys():
                    resultado["Importe Total: $"].append(text)   
                else:
                    resultado["Importe Total: $"] = [text]
    pagina.extract_text(visitor_text=determinante_de_funcion)
    if usarVisitanteDolar == True:
        try:
            pagina.extract_text(visitor_text=visitante)
        except Exception as e:
            print(e)
    else:
        try:
            pagina.extract_text(visitor_text=visitanteDolar)
        except Exception as e:
            print(e)
    
    contador +=1
    aux1.extend(aux2)
    diccionario = {}
    for elemento in aux1:
        texto = elemento[0]
        x = elemento[1]
        y = elemento[2]

        if y not in diccionario:
            diccionario[y] = [(texto, x)]
        else:
            diccionario[y].append((texto,x))
    resultado2={}
    try:
        resultado2 = {valor[0][0]: diccionario[y][1][0] for y, valor in diccionario.items()}
    except:
        pass
    for e in resultado2:
        resultado[e]=[resultado2[e]]

    for e in resultado:
        
        if len(resultado[e])<contador:
            resultado[e].append(None)
        elif len(resultado[e])>contador:
            resultado[e]= [resultado[e][0]] 
    #print(resultado)
    return resultado 

