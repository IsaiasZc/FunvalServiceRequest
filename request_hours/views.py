from django.shortcuts import render
import pandas as pd
# Create your views here.

EXCEL = "1_sN9SdRO5G0xrrisgpB-MkXI0-nOtcZsfFhrCnvikwM"
ID = "0"

URL = f'https://docs.google.com/spreadsheets/d/{EXCEL}/gviz/tq?tqx=out:csv&gid={ID}'

def home(request):
    return render(request, 'html/home.html')

def result(request):

    # leer el archivo CSV desde DRIVE
    file = pd.read_csv(URL, header=0)

    # Obtener correo del usuario
    email = request.GET.get('correo')

    user_info = file[file['Correo'] == email]

    # info as list
    try:
        # retornaremos una respuesta valida si el correo indicado si existe
        user_info = list(user_info['Notas'])
        return render(request, 'html/result.html', {'hours': f'Actualmente tienes {user_info[0]} hora(s) de servicio registradas.'})
    except:
        # En caso el correo no exista, indicaremos que escriba nuevamente el correo

        # user_info = ['El correo no existe, intentalo nuevamente']

        return render(request, 'html/no_valid.html')
