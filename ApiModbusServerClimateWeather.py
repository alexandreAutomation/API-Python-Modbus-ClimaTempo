from pyModbusTCP.server import ModbusServer, DataBank
from requests import request
from json import loads
from time import sleep
from datetime import datetime
from os import system
from sys import exit

# declares arrives globals
system('cls')
select_token = 0
index_and_value = []
current_weather_response = {}
forecast_15_days_response = {}
forecast_72_hours_response = {}
register_city_response = {}
current_weather = False
forecast_15_days = False
forecast_72_hours = False
register_city = False
server = ModbusServer(host="localhost", port=502, no_block=True)
token_list = []
parameters_token = []
lists = [['temperature', 'wind_velocity', 'humidity', 'pressure', 'sensation'],
         ['temperature', 'humidity', 'thermal_sensation'],
         ['temperature', 'humidity'],
         ['dawn', 'morning', 'afternoon', 'night'],
         ['min', 'max'],
         ['velocity_min', 'velocity_max', 'velocity_avg', 'gust_max', 'direction_degrees'],
         ['velocity_max', 'velocity_avg', 'gust_max', 'direction_degrees'],
         ['low', 'mid', 'high']]
parameters_token_api = [{'id': 'None', 'name': 'None', 'state': 'None', 'country': 'None', 'token': 'None'}]
dict_values_api = ['current_temperature                               ',
                   'current_wind_velocity                             ',
                   'current_humidity                                  ',
                   'current_pressure                                  ',
                   'current_sensation                                 ',
                   'forecast_temperature_min                          ',
                   'forecast_humidity_min                             ',
                   'forecast_thermal_sensation_min                    ',
                   'forecast_temperature_max                          ',
                   'forecast_humidity_max                             ',
                   'forecast_thermal_sensation_max                    ',
                   'forecast_temperature_dawn_min                     ',
                   'forecast_temperature_dawn_max                     ',
                   'forecast_humidity_dawn_min                        ',
                   'forecast_humidity_dawn_max                        ',
                   'forecast_temperature_morning_min                  ',
                   'forecast_temperature_morning_max                  ',
                   'forecast_humidity_morning_min                     ',
                   'forecast_humidity_morning_max                     ',
                   'forecast_temperature_afternoon_min                ',
                   'forecast_temperature_afternoon_max                ',
                   'forecast_humidity_afternoon_min                   ',
                   'forecast_humidity_afternoon_max                   ',
                   'forecast_temperature_night_min                    ',
                   'forecast_temperature_night_max                    ',
                   'forecast_humidity_night_min                       ',
                   'forecast_humidity_night_max                       ',
                   'forecast_wind_velocity_min                        ',
                   'forecast_wind_velocity_max                        ',
                   'forecast_wind_velocity_avg                        ',
                   'forecast_wind_gust_max                            ',
                   'forecast_wind_direction_degrees                   ',
                   'forecast_wind_velocity_max_dawn                   ',
                   'forecast_wind_velocity_avg_dawn                   ',
                   'forecast_wind_gust_max_dawn                       ',
                   'forecast_wind_direction_degrees_dawn              ',
                   'forecast_wind_velocity_max_morning                ',
                   'forecast_wind_velocity_avg_morning                ',
                   'forecast_wind_gust_max_morning                    ',
                   'forecast_wind_direction_degrees_morning           ',
                   'forecast_wind_velocity_max_afternoon              ',
                   'forecast_wind_velocity_avg_afternoon              ',
                   'forecast_wind_gust_max_afternoon                  ',
                   'forecast_wind_direction_degrees_afternoon         ',
                   'forecast_wind_velocity_max_night                  ',
                   'forecast_wind_velocity_avg_night                  ',
                   'forecast_wind_gust_max_night                      ',
                   'forecast_wind_direction_degrees_night             ',
                   'forecast_rain_probability                         ',
                   'forecast_rain_precipitation                       ',
                   'forecast_ultraviolet_max                          ',
                   'forecast_pressure                                 ',
                   'next_day_forecast_temperature_min                 ',
                   'next_day_forecast_humidity_min                    ',
                   'next_day_forecast_thermal_sensation_min           ',
                   'next_day_forecast_temperature_max                 ',
                   'next_day_forecast_humidity_max                    ',
                   'next_day_forecast_thermal_sensation_max           ',
                   'next_day_forecast_temperature_dawn_min            ',
                   'next_day_forecast_temperature_dawn_max            ',
                   'next_day_forecast_humidity_dawn_min               ',
                   'next_day_forecast_humidity_dawn_max               ',
                   'next_day_forecast_temperature_morning_min         ',
                   'next_day_forecast_temperature_morning_max         ',
                   'next_day_forecast_humidity_morning_min            ',
                   'next_day_forecast_humidity_morning_max            ',
                   'next_day_forecast_temperature_afternoon_min       ',
                   'next_day_forecast_temperature_afternoon_max       ',
                   'next_day_forecast_humidity_afternoon_min          ',
                   'next_day_forecast_humidity_afternoon_max          ',
                   'next_day_forecast_temperature_night_min           ',
                   'next_day_forecast_temperature_night_max           ',
                   'next_day_forecast_humidity_night_min              ',
                   'next_day_forecast_humidity_night_max              ',
                   'next_day_forecast_wind_velocity_min               ',
                   'next_day_forecast_wind_velocity_max               ',
                   'next_day_forecast_wind_velocity_avg               ',
                   'next_day_forecast_wind_gust_max                   ',
                   'next_day_forecast_wind_direction_degrees          ',
                   'next_day_forecast_wind_velocity_max_dawn          ',
                   'next_day_forecast_wind_velocity_avg_dawn          ',
                   'next_day_forecast_wind_gust_max_dawn              ',
                   'next_day_forecast_wind_direction_degrees_dawn     ',
                   'next_day_forecast_wind_velocity_max_morning       ',
                   'next_day_forecast_wind_velocity_avg_morning       ',
                   'next_day_forecast_wind_gust_max_morning           ',
                   'next_day_forecast_wind_direction_degrees_morning  ',
                   'next_day_forecast_wind_velocity_max_afternoon     ',
                   'next_day_forecast_wind_velocity_avg_afternoon     ',
                   'next_day_forecast_wind_gust_max_afternoon         ',
                   'next_day_forecast_wind_direction_degrees_afternoon',
                   'next_day_forecast_wind_velocity_max_night         ',
                   'next_day_forecast_wind_velocity_avg_night         ',
                   'next_day_forecast_wind_gust_max_night             ',
                   'next_day_forecast_wind_direction_degrees_night    ',
                   'next_day_forecast_rain_probability                ',
                   'next_day_forecast_rain_precipitation              ',
                   'next_day_forecast_ultraviolet_max                 ',
                   'next_day_forecast_pressure                        '
                   ]
signal_values_api = ['°C', 'km/h', '% Rh', 'hPa', '°C',
                     '°C', '% Rh', '°C',
                     '°C', '% Rh', '°C',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     'km/h', 'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     '%', 'mm', 'UV', 'hPa',
                     '°C', '% Rh', '°C',
                     '°C', '% Rh', '°C',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     '°C', '°C', '% Rh', '% Rh',
                     'km/h', 'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     'km/h', 'km/h', 'km/h', '°',
                     '%', 'mm', 'UV', 'hPa'
                     ]


def api_clima_tempo(api_parameters_token, api_select_token=0, api_current_weather=None, api_forecast_15_days=None,
                    api_forecast_72_hours=None, api_register_city=None):
    api_current_weather_response = {}
    api_forecast_15_days_response = {}
    api_forecast_72_hours_response = {}
    api_register_city_response = {}
    parameters_token_response = {}
    try:
        # Bus climatempo actual
        if api_current_weather:
            api_current_weather = request("GET", 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/'
                                          + str(api_parameters_token[api_select_token]['id']) + '/current?token='
                                          + str(api_parameters_token[api_select_token]['token']), timeout=5)
            api_current_weather_response = loads(api_current_weather.text)
        # Busca previsão de 15 dias
        if api_forecast_15_days:
            api_forecast_15_days = request("GET", "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"
                                           + str(api_parameters_token[api_select_token]['id']) + "/days/15?token="
                                           + str(api_parameters_token[api_select_token]['token']), timeout=5)
            api_forecast_15_days_response = loads(api_forecast_15_days.text)
        # Busca previsão de 72 horas
        if api_forecast_72_hours:
            api_forecast_72_hours = request("GET", "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"
                                            + str(api_parameters_token[api_select_token]['id']) + "/hours/72?token="
                                            + str(api_parameters_token[api_select_token]['token']), timeout=5)
            api_forecast_72_hours_response = loads(api_forecast_72_hours.text)
        # Registra cidade no token
        if api_register_city:
            search_city = request("GET", "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" +
                                  api_parameters_token[api_select_token]['name'] + "&state=" +
                                  api_parameters_token[api_select_token]['state'] + "&country=" +
                                  api_parameters_token[api_select_token]['country'] + "&token=" +
                                  str(api_parameters_token[api_select_token]['token']), timeout=5)
            search_city_response = loads(search_city.text)
            if 'error' in search_city_response:
                if search_city_response['error']:
                    api_register_city_response = search_city_response
            else:
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                payload = "localeId[]=" + str(search_city_response[0]['id'])
                api_register_city = request("PUT", "http://apiadvisor.climatempo.com.br/api-manager/user-token/"
                                            + api_parameters_token[api_select_token]['token'] + "/locales",
                                            headers=headers,
                                            data=payload)
                api_register_city_response = loads(api_register_city.text)
                if api_register_city_response['status']:
                    search_city_response[0]['token'] = api_parameters_token[api_select_token]['token']
                    parameters_token_response = search_city_response
    except Exception as error_api_2:
        if 'list index out of range' in str(error_api_2):
            api_current_weather_response = api_forecast_15_days_response = api_forecast_72_hours_response \
                = api_register_city_response = parameters_token_response = {'error': True, 'detail': str(error_api_2)}
        elif 'line 1 column 1 (char 0)' in str(error_api_2):
            api_current_weather_response = api_forecast_15_days_response = api_forecast_72_hours_response \
                = api_register_city_response = parameters_token_response = {'error': True, 'detail': str(error_api_2)}
        elif 'HTTPConnectionPool' in str(error_api_2):
            api_current_weather_response = api_forecast_15_days_response = api_forecast_72_hours_response \
                = api_register_city_response = parameters_token_response = {'error': True, 'detail': str(error_api_2)}

    return api_current_weather_response, api_forecast_15_days_response, api_forecast_72_hours_response, \
           api_register_city_response, parameters_token_response


def sendDataModbus(forecast, current, config_ip_door, parameters_token_run, select_token_run):
    # Informaçoes de clima tempo atual
    for key in lists[0]:
        index_and_value.append(int(current['data'][key]))
    for days in [0, 1]:
        # Previsão minima e maxima da temperatura, umidade, Sensação Termica
        for min_and_max in lists[4]:
            for key in lists[1]:
                index_and_value.append(int(forecast['data'][days][key][min_and_max]))
        # Previsão minima e maxima de umidade e temperatura por periodo
        for period_unique in lists[3]:
            for key in lists[2]:
                index_and_value.append(int(forecast['data'][days][key][period_unique]['min']))
                index_and_value.append(int(forecast['data'][days][key][period_unique]['max']))
        # Previsão parametros do vento
        for key in lists[5]:
            index_and_value.append(int(forecast['data'][days]['wind'][key]))
        # Previsão parametros do vento por perido
        for period_unique in lists[3]:
            for key in lists[6]:
                index_and_value.append(int(forecast['data'][days]['wind'][period_unique][key]))
        # Previsão de probabilidade de chuva
        index_and_value.append(int(forecast['data'][days]['rain']['probability']))
        # Previsão da precipitação da chuva
        index_and_value.append(int(forecast['data'][days]['rain']['precipitation']))
        # Previsão raio ultra violeta do sol
        index_and_value.append(int(forecast['data'][days]['uv']['max']))
        # Previsão da Pressão
        index_and_value.append(int(forecast['data'][days]['pressure']['pressure']))
        # Envia valores para servidor modbus
    for index_value, value in enumerate(index_and_value, start=0):
        DataBank.set_words(index_value, [int(value)])
    system("cls")
    print(f"""
            --------------------Selected Token------------------
            Name City: {parameters_token_run[select_token_run]['name']}
            ID City: {parameters_token_run[select_token_run]['id']}
            State City: {parameters_token_run[select_token_run]['state']}
            Country City: {parameters_token_run[select_token_run]['country']}
            Number Token: {select_token_run + 1}
            Token: {parameters_token_run[select_token_run]['token']}
            --------------------Defined Network-----------------
            IP: {config_ip_door[0]}
            Door: {config_ip_door[1]}
            Time Request: Every {config_ip_door[2]} minutes.
            Data-Time-Now: {datetime.now()}
            """)
    print(f"END.MODBUS | NAME POINT MODBUS                                  | VALUE POINT ACTUAL")
    for index_value, value in enumerate(index_and_value, start=0):
        if index_value < 10:
            index_value_alter = '0' + str(index_value)
        else:
            index_value_alter = index_value
        print(f"{index_value_alter}         | {dict_values_api[index_value]} | {value}{signal_values_api[index_value]}")
    del index_and_value[0:99]


def arq_txt(write_token=None, read_token=None, token_true=None, write_config=None, read_config=None, config_true=None,
            token_txt=None, config_txt=None):
    if token_true:
        try:
            archive = open('parametersTokenCity.txt', 'r')
            archive.close()
        except:
            archive = open('parametersTokenCity.txt', 'w')
            archive.close()
        archive = open('parametersTokenCity.txt', 'r')
        parameters_token_verified = archive.read()
        archive.close()
        if write_token:
            if str(token_txt[0]['token']) not in parameters_token_verified:
                archive = open('parametersTokenCity.txt', 'w')
                archive.write(parameters_token_verified + str(token_txt) + ";")
                archive.close()
        if read_token:
            archive = open('parametersTokenCity.txt', 'r')
            archive_str = archive.read()
            archive.close()
            archive_str = ((archive_str.replace("[", "")).replace("]", "")).split(';')
            parameters_token_txt = []
            for a in archive_str:
                if a != "":
                    b = eval(a)
                    parameters_token_txt.append(b)
            return parameters_token_txt
    if config_true:
        try:
            archive = open('config.txt', 'r')
            archive.close()
        except:
            archive = open('config.txt', 'w')
            archive.close()
        if write_config:
            archive = open('config.txt', 'w')
            archive.write(config_txt)
            archive.close()
        if read_config:
            archive = open('config.txt', 'r')
            archive_str = archive.readline()
            archive.close()
            return archive_str.split(";")


def run_api(parameters_token_run, select_token_run):
    # Armazenar parametros da API
    # noinspection PyGlobalUndefined
    global error_api
    parameters_token_run = arq_txt(token_txt=parameters_token_run, token_true=True, read_token=True,
                                   write_token=False)
    # Armazenar parametros de configuração
    config_ip_door = arq_txt(config_true=True, read_config=True, write_config=False)
    if len(config_ip_door) == 1:
        config_ip_door = arq_txt(config_true=True, read_config=True, write_config=True, config_txt='localhost;2001;10')
    # Configuração rede modbus
    server_run = ModbusServer(host=config_ip_door[0], port=int(config_ip_door[1]), no_block=True)
    # Preparação do tempo de requesição dos dados em minutos
    time_request = [int(config_ip_door[2])]
    time_request_list = 0
    while time_request_list != 60:
        time_request_list += time_request[0]
        time_request.append(time_request_list)
    time_request[0] = 0
    time_fist = 1
    # Inicia Servidor Modbus
    server_run.start()
    while True:
        application_time = 60
        datetime_now = datetime.now()
        datetime_min = datetime_now.minute
        datatime_hor = datetime_now.hour
        if datatime_hor == 0 and select_token_run != 0:
            select_token_run = 0
        if (datetime_min in time_request) or time_fist == 1:
            time_fist = 0
            # Solicicação para API clima tempo
            current_weather_run, forecast_15_days_run, forecast_72_hours_run, \
            register_city_run, parameters_api_token = api_clima_tempo(api_parameters_token=parameters_token_run,
                                                                      api_select_token=select_token_run,
                                                                      api_current_weather=True,
                                                                      api_forecast_15_days=True,
                                                                      api_forecast_72_hours=False,
                                                                      api_register_city=False)
            # Verifica erro e Chama função para separar os dados
            error_api_list = [current_weather_run, forecast_15_days_run, forecast_72_hours_response,
                              register_city_run, parameters_token]
            for error_api in error_api_list:
                if 'error' in error_api:
                    system("cls")
                    break
            # noinspection PyTypeChecker
            if 'error' not in error_api:
                sendDataModbus(forecast_15_days_run, current_weather_run, config_ip_door, parameters_token_run,
                               select_token_run)
                sleep(int(config_ip_door[2]))
            elif error_api['detail'] == 'You have reached your limit of 10 requests per minute.':
                print(str(datetime.now()) + ' - Wait for a while ' + error_api['retry-after'])
                time = int(''.join(filter(lambda i: i if i.isdigit() else None, error_api['retry-after'])))
                application_time = 1
                time_fist = 1
                sleep(time)
            elif error_api['detail'] == 'You have reached your limit of 300 requests per day.':
                print(str(datetime.now()) + " - Token exchange")
                application_time = 1
                time_fist = 1
                select_token_run += 1
            elif 'ConnectionError' in error_api['detail']:
                print(str(datetime.now()) + " - Waiting for internet connection")
                a = ''
                while a != '<Response [200]>':
                    try:
                        a = str(request('GET', 'https://www.google.com.br'))
                        application_time = 1
                    except:
                        application_time = 1
                        pass
            elif 'line 1 column 1 (char 0)' in error_api['detail'] or 'it was not possible to handle your request' \
                    in error_api['detail'] or 'Unable to resolve service' in error_api['detail']:
                print(str(datetime.now()) + ' - API Weather weather without service')
                application_time = 1
                time_fist = 1
            elif error_api['detail'] == 'list index out of range':
                print(str(datetime.now()) +
                      ' - No Token. Waiting for the turn of the day or enter another token and restart the application')
                datitime_now_ref = True
                datetime_now = datetime.now()
                datetime_ref = datetime_now.fromordinal(datetime_now.toordinal() + 1)
                while datitime_now_ref:
                    sleep(1)
                    if datetime_ref >= datetime.now():
                        datitime_now_ref = True
                    else:
                        select_token_run = 0
                        datitime_now_ref = False
            elif 'None' in parameters_token_run[0]['token']:
                print(str(datetime.now()) + ' - ' + 'You have no token')
                arquivo = open('parametersTokenCity.txt', 'w')
                arquivo.close()
            elif 'timeout' in error_api['detail']:
                print(str(datetime.now()) + ' - Read timed out')
                application_time = 1
                time_fist = 1
            else:
                print(str(datetime.now()) + '- error no registry ' + str(error_api))
                exit()
            sleep(application_time)
        else:
            sleep(application_time)


if __name__ == '__main__':
    run_api(parameters_token_api, select_token)
