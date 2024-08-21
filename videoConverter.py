import os
import subprocess
from datetime import datetime
from rich import print
from pathlib import Path
from dotenv import load_dotenv
from envs import getFileName

# Load environment variables
load_dotenv()

def convert_mov_to_mp4(input_path, bitrate='1M'):
    """
    Convierte un archivo QuickTime (.mov) a .mp4 con buena calidad y tamaño reducido, 
    manteniendo el nombre original en la misma carpeta. Si el archivo .mp4 ya existe, 
    crea un nuevo archivo con el sufijo "-copy".
    
    :param input_path: Ruta al archivo .mov de entrada.
    :param bitrate: Tasa de bits para el video de salida. Valores más bajos reducen el tamaño del archivo.
    """
    # Extract the path, name and extension
    dir_name, file_name = os.path.split(input_path)
    base_name, _ = os.path.splitext(file_name)
    
    # Create output Path
    output_path = os.path.join(dir_name, f'{base_name}.mp4')
    
    # if the output file already exists, add the suffix "-copy"
    copy_suffix = 1
    while os.path.exists(output_path):
        output_path = os.path.join(dir_name, f'{base_name}-copy{copy_suffix}.mp4')
        copy_suffix += 1
    
    # Record start time
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
        
        # Record end time and calculate duration
        print(f'[bold green]Hora de finalización: {end_time.strftime("%H:%M:%S")}[/bold green]')
        duration = end_time - start_time
        print(f'[bold green]Duración del proceso: {str(duration)}[/bold green]')
        
        # Calulate output file size in MB
        file_size = os.path.getsize(output_path) / (1024 * 1024)
        print(f'[bold orange]Tamaño del archivo: {file_size:.2f} MB[/bold orange]')
        
    except subprocess.CalledProcessError as e:
        print(f'Error en la conversión: {e}')

# Implementation
base_dir = Path(__file__).resolve().parent
files_dir = base_dir / 'files'
file_name = getFileName('cv')
input_file = files_dir / (file_name)
convert_mov_to_mp4(input_file, bitrate='1M')  # you can adjust the bitrate according to your needs
