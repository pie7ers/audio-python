import os
import subprocess
from datetime import datetime
from rich import print

def convert_mov_to_mp4(input_path, bitrate='1M'):
    """
    Convierte un archivo QuickTime (.mov) a .mp4 con buena calidad y tamaño reducido, 
    manteniendo el nombre original en la misma carpeta. Si el archivo .mp4 ya existe, 
    crea un nuevo archivo con el sufijo "-copy".
    
    :param input_path: Ruta al archivo .mov de entrada.
    :param bitrate: Tasa de bits para el video de salida. Valores más bajos reducen el tamaño del archivo.
    """
    # Extraer la ruta, el nombre del archivo y la extensión
    dir_name, file_name = os.path.split(input_path)
    base_name, _ = os.path.splitext(file_name)
    
    # Crear la ruta del archivo de salida .mp4
    output_path = os.path.join(dir_name, f'{base_name}.mp4')
    
    # Si el archivo de salida ya existe, agregar el sufijo "-copy"
    copy_suffix = 1
    while os.path.exists(output_path):
        output_path = os.path.join(dir_name, f'{base_name}-copy{copy_suffix}.mp4')
        copy_suffix += 1
    
    # Registrar la hora de inicio
    start_time = datetime.now()
    print(f'[bold green]Hora de inicio: {start_time.strftime("%H:%M:%S")}[/bold green]')
    
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vcodec', 'libx264',
        '-b:v', bitrate,
        '-acodec', 'aac',
        '-strict', 'experimental',
        '-movflags', '+faststart',
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        end_time = datetime.now()
        print(f'Conversión exitosa: {output_path}')
        
        # Registrar la hora final y calcular la duración
        print(f'[bold green]Hora de finalización: {end_time.strftime("%H:%M:%S")}[/bold green]')
        duration = end_time - start_time
        print(f'[bold green]Duración del proceso: {str(duration)}[/bold green]')
        
        # Calcular el tamaño del archivo resultante en MB
        file_size = os.path.getsize(output_path) / (1024 * 1024)
        print(f'[bold orange]Tamaño del archivo: {file_size:.2f} MB[/bold orange]')
        
    except subprocess.CalledProcessError as e:
        print(f'Error en la conversión: {e}')

# Ejemplo de uso
input_file = 'files/MY_FILE.mov'
convert_mov_to_mp4(input_file, bitrate='1M')  # Puedes ajustar el bitrate según tus necesidades
