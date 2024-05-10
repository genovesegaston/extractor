import PyPDF2 as pdf 
from exportador_a_excel import exportar_excel
import os

def lector_de_transferencia2(paths):
        
    filtros = (""," ","\n","null")
    result={}
    for path in paths:
        archivo = open(path,"rb")
        lector = pdf.PdfReader(archivo)
        pagina = lector.pages[0]
        
        def divisor_texto(texto:str,posicion:int):
            
            return  texto.replace("\n", " ").split(":")[posicion]
        
        def visitante(text,_,tm,__,___):
            x=tm[4]
            y=tm[5]
            if text not in filtros:
                
                
                if y > 620 and y < 650:                     
                    if "info" not in result.keys():
                        result["info"]={}
                    if str(divisor_texto(text,0)) not in result["info"].keys():
                        result["info"][divisor_texto(text,0)]=[divisor_texto(text,1)]
                    else:
                        result["info"][divisor_texto(text,0)].append(divisor_texto(text,1))
                if y > 650 and y < 720 and x >200:
                    if "info" not in result.keys():
                        result["info"] = {}
                    if divisor_texto(text,0) not in result["info"].keys():
                        result["info"][divisor_texto(text,0)]=[divisor_texto(text,1)]
                    else:
                        result["info"][divisor_texto(text,0)].append(divisor_texto(text,1))
                        
                        
                        
                if y < 560 and y > 520 and x < 200:
                    if "depositario" not in result.keys():
                        result["depositario"]={}
                    if divisor_texto(text,0) not in result["depositario"].keys():
                        result["depositario"][divisor_texto(text,0)]=[divisor_texto(text,1)]
                    else:
                        result["depositario"][divisor_texto(text,0)].append(divisor_texto(text,1))
                if y > 500 and y < 520 and x <200:
                        if "depositario" not in result.keys():
                            result["depositario"]={}
                        if text.split("Planta")[0] not in result["depositario"].keys():
                            result["depositario"][text.split("Planta")[0]]=[text.split("Planta")[1]]
                        else:
                            result["depositario"][text.split("Planta")[0]].append(text.split("Planta")[1])
                        
                
                
                if y < 560 and y > 520 and x > 200:
                    if "depositante" not in result.keys():
                        result["depositante"]={}
                    if divisor_texto(text,0) not in result["depositante"].keys():
                        result["depositante"][divisor_texto(text,0)]=[divisor_texto(text,1)]
                    else:
                        result["depositante"][divisor_texto(text,0)].append(divisor_texto(text,1))            
                if y > 500 and y < 520 and x > 200:
                        if "depositante" not in result.keys():
                            result["depositante"]={}
                        if text.split("Nº")[0] not in result["depositante"].keys():
                            result["depositante"][text.split("Nº")[0]]=[text.split("Nº")[1]]
                        else:
                            result["depositante"][text.split("Nº")[0]].append(text.split("Nº")[1])
                            
                            
                            
                if y > 435 and y <480:
                    #print(f"{text}   x: {x}    y:{y}")
                    if "detalle" not in result.keys():
                        result["detalle"] = {}
                        
                    elif x < 100 and  y >448 and y < 455:
                        if "N° CERTIFICADO DE DEPOSITO" not in result["detalle"].keys():
                            result["detalle"]["N° CERTIFICADO DE DEPOSITO"]=[text]
                        else:
                            result["detalle"]["N° CERTIFICADO DE DEPOSITO"].append(text)
                            
                    elif x < 400 and x > 345 and y >448 and y < 455:
                        if "N° CARTA DE PORTE" not in result["detalle"].keys():
                            result["detalle"]["N° CARTA DE PORTE"]=[text]
                        else:
                            result["detalle"]["N° CARTA DE PORTE"].append(text)
                            
                    elif  x < 200 and x > 150 and y >448 and y < 455:
                        if  "N° CTG"  not in result["detalle"].keys():
                            result["detalle"]["N° CTG"]=[text]
                        else:
                            result["detalle"]["N° CTG"].append(text)
                    elif x < 450 and x > 440 and y >448 and y < 455   : 
                        if "Kilos" not in result["detalle"].keys():
                            result["detalle"]["Kilos"]=[text]
                        else: 
                            result["detalle"]["Kilos"].append(text)
                              
                        
                        
                
                             
        pagina.extract_text(visitor_text=visitante)
    print(result)
    return result
def lector_de_transferencia(paths):
        
    filtros = (""," ","\n","null")
    result={}
    for path in paths:
        archivo = open(path,"rb")
        lector = pdf.PdfReader(archivo)
        pagina = lector.pages[0]
        
        def divisor_texto(texto:str,posicion:int):
            
            return  texto.replace("\n", " ").split(":")[posicion]
        
        def visitante(text,_,tm,__,___):
            x=tm[4]
            y=tm[5]
            if text not in filtros:
                
                
                if y > 620 and y < 650:                     
                    if divisor_texto(text,0) not in result.keys():
                        result[divisor_texto(text,0)]=[divisor_texto(text,1)]
                    else:
                        result[divisor_texto(text,0)].append(divisor_texto(text,1))
                        
                if y > 650 and y < 720 and x >200:
                    if f"{divisor_texto(text,0)}" not in result.keys():
                        result[f"{divisor_texto(text,0)}"]=[divisor_texto(text,1)]
                    else:
                        result[f"{divisor_texto(text,0)}"].append(divisor_texto(text,1))
                        
                        
                        
                if y < 580 and y > 520 and x < 200:
                    if f"{divisor_texto(text,0)} depositario" not in result.keys():
                        result [f"{divisor_texto(text,0)} depositario"]=[divisor_texto(text,1)]
                    else:
                        result[f"{divisor_texto(text,0)} depositario"].append(divisor_texto(text,1))
                        
                
                
                if y < 580 and y > 520 and x > 200:
                    if f"{divisor_texto(text,0)} depositante" not in result.keys():
                        result[f"{divisor_texto(text,0)} depositante"]=[divisor_texto(text,1)]
                    else:
                        result[f"{divisor_texto(text,0)} depositante"].append(divisor_texto(text,1))            
                                            
                            
                if y > 435 and y <480:     
                    if x < 100 and  y >448 and y < 455:
                        if "N° CERTIFICADO DE DEPOSITO" not in result.keys():
                            result["N° CERTIFICADO DE DEPOSITO"]=[text]
                        else:
                            result["N° CERTIFICADO DE DEPOSITO"].append(text)
                            
                    elif x < 400 and x > 345 and y >448 and y < 455:
                        if "N° CARTA DE PORTE" not in result.keys():
                            result["N° CARTA DE PORTE"]=[text]
                        else:
                            result["N° CARTA DE PORTE"].append(text)
                            
                    elif  x < 200 and x > 150 and y >448 and y < 455:
                        if  "N° CTG"  not in result.keys():
                            result["N° CTG"]=[text]
                        else:
                            result["N° CTG"].append(text)
                    elif x < 450 and x > 440 and y >448 and y < 455   : 
                        if "Kilos" not in result.keys():
                            result["Kilos"]=[float(text.split(" ")[0])]
                        else: 
                            result["Kilos"].append(float(text.split(" ")[0]))
                              
                        
                        
                
                             
        pagina.extract_text(visitor_text=visitante)
    #print(result)
    return result
#exportar_excel(lector_de_transferencia2([r"c:\Users\franc\Downloads\RT TRANSFERENCIA BARRACON-MACONDO\certificacionElectronicaGranosRetiroTranf (8).pdf",r"c:\Users\franc\Downloads\RT TRANSFERENCIA BARRACON-MACONDO\certificacionElectronicaGranosRetiroTranf (4).pdf"]))
