# Gabiel Macias
# Parcial Fila B

# Punto 1:
valor_kg = int(input('Digite el valor del Kg de manzanas: '))    
cant_manzanas = int(input('Digite la cantidad de Kg comprados: '))
if cant_manzanas <= 1:
    total = valor_kg * cant_manzanas
    print(f'El valor a pagar es de: $ {total} ')
elif cant_manzanas >=2 and  cant_manzanas < 5:
    valort = valor_kg * cant_manzanas
    descuento = valort * 0.10
    total = valort - descuento
    print(f'El valor del descuento es: $ {total} ')
elif cant_manzanas >=5 and  cant_manzanas <10:
    valort = valor_kg * cant_manzanas
    descuento = valort * 0.15
    total = valort - descuento
    print(f'El valor del descuento es: $ {total} ')
else:
    valort = valor_kg * cant_manzanas
    descuento = valort * 0.20
    total = valort - descuento
    print(f'El valor del descuento es: $ {total} ')

# Punto 2:
valor_abanico = int(input('Digite el valor del abanico: '))
cantidad_abanicos = int(input('Digite la cantida de abanicos: '))   
clave = str(input('Digite la clave: '))  
if  clave == '010':
    total = valor_abanico * cantidad_abanicos
    descuento = total * 0.20
    total = total - descuento
    print(f'El valor a pagar es de: $ {total} ')
elif clave == '020':
    total = valor_abanico * cantidad_abanicos
    descuento = total * 0.40
    total = total - descuento
    print(f'El valor a pagar es de: $ {total} ')
elif clave == '030':
    total = valor_abanico * cantidad_abanicos
    descuento = total * 0.55
    total = total - descuento
    print(f'El valor a pagar es de: $ {total} ')
elif clave == '040':
    total = valor_abanico * cantidad_abanicos
    descuento = total * 0.70
    total = total - descuento
    print(f'El valor a pagar es de: $ {total} ')
else:
    print('La clave es incorrecta')

# Punto 3:
preciop = float(input('Digite el precio del producto a comprar: '))
marca = str(input('Digite la marca del producto: '))
if preciop >= 4000:
    descuento = preciop * 0.20
    total = preciop - descuento 
    if marca == "NOSY":
        descuento_dos = preciop * 0.1
        total_dos = total - descuento_dos
        iva = preciop * 0.30
        tpagar = total_dos + iva
        print(f'El precio con descuento de marca e iva es: $ {tpagar}')
    else:
        iva = preciop * 0.30
        tpagar = total + iva
        print(f'El precio sin descuento de marca e iva es: $ {tpagar}')
else:
    if marca == "NOSY":
        descuento_dos = preciop * 0.1
        total_dos = preciop - descuento_dos
        iva = preciop * 0.30
        tpagar = total_dos + iva
        print(f'El precio con descuento de marca e iva es: $ {tpagar}')
    else:
        iva = preciop * 0.30
        tpagar = preciop + iva
        print(f'El precio sin descuento de marca e iva es: $ {tpagar}') 
        
# Punto 4: 
num_hect = float(input('Digite el numero de hectáreas: ')) 
if num_hect > 5:
    pino = num_hect * 0.8
    oyamel = num_hect * 0.15
    cedro = num_hect * 0.05
    print(f'El cantidad correspondiente a pino es: {pino} hectáreas')
    print(f'El cantidad correspondiente a oyamel es: {oyamel} hectáreas')
    print(f'El cantidad correspondiente a pino es: {cedro} hectáreas')
else: 
    pino = num_hect * 0.45
    oyamel = num_hect * 0.25
    cedro = num_hect * 0.30
    print(f'El cantidad correspondiente a pino es: {pino} hectáreas')
    print(f'El cantidad correspondiente a oyamel es: {oyamel} hectáreas')
    print(f'El cantidad correspondiente a pino es: {cedro} hectáreas')   

# Punto 5:
pri_numero = float(input('Digite el primer numero: '))
seg_numero = float(input('Digite el segundo numero: '))
ter_numero = float(input('Digite el tercer numero: '))
if pri_numero > seg_numero:
    if pri_numero > ter_numero:
        print(f'El mayor es el numero: {pri_numero}')
    else:
        print(f'El mayor es el numero: {ter_numero}')
else:
    if seg_numero > ter_numero:
        print(f'El mayor es el numero: {seg_numero}')
    else:
        print(f'El mayor es el numero: {ter_numero}')      
        
    