    import os
    import glob
    
    # Path de la carpeta raíz
    root_path = 'D:\progra'
    
    # Obtenemos todos los archivos HTML, PHP y SQL de la carpeta raíz y sus subcarpetas
    files = glob.glob(root_path + '/**/*.html', recursive=True)
    files += glob.glob(root_path + '/**/*.php', recursive=True)
    files += glob.glob(root_path + '/**/*.sql', recursive=True)
    files += glob.glob(root_path + '/**/*.py', recursive=True)
    
    # Creamos el archivo de salida en modo escritura
    with open('texto_combinado.txt', 'w') as f_out:
        # Iteramos sobre cada archivo
        for file in files:
            # Abrimos el archivo en modo lectura
            with open(file, 'r') as f_in:
                # Leemos todo el texto del archivo
                text = f_in.read()
                # Escribimos el nombre y la ruta del archivo en el archivo de salida
                f_out.write(f'Nombre del archivo: {os.path.basename(file)}\n')
                f_out.write(f'Ruta del archivo: {os.path.abspath(file)}\n')
                # Escribimos una línea en blanco para separar el nombre y ruta del contenido del archivo
                f_out.write('\n')
                # Escribimos el texto en el archivo de salida
                f_out.write(text)
                # Escribimos otra línea en blanco para separar el contenido de cada archivo
                f_out.write('\n\n')
