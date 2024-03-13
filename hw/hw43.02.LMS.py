# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении. Определите 2 метода: для прослушивания музыки, и для просмотра видео. При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%. Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон разряжен). Также предусмотрите возможность заряжания батареи.

class MobilePhone:
    def __init__(self, imei, os_info):
        self.imei = imei
        self.battery = 100  
        self.os_info = os_info
          
    def play_music(self):
        if self.battery <= 0:
            raise ValueError('Телефон разряжен!')
        self._consume_battery(5)
        return 'Проигрывается музыка.'
    
    def play_video(self):
        if self.battery <= 0:
            raise ValueError('Телефон разряжен!')
        if self.battery <= 10:
            raise ValueError('Слишком мало заряда батареи для просмотра видео!')
        self._consume_battery(7)
        return 'Проигрывается видео.'
    
    def _consume_battery(self, percentage):
        self.battery -= percentage
        if self.battery <= 0:
            self.battery = 0
            raise ValueError('Телефон разряжен!')
    
    def get_battery_level(self):
        self._consume_battery(0.5) 
        return self.battery
    
    def charge_battery(self, percentage):
        if percentage <= 0:
            raise ValueError('Заряд должен быть положительным числом!')
        self.battery = min(100, self.battery + percentage)  

    def are_methods_available(self):
        if self.battery <= 0:
            raise ValueError('Телефон разряжен!')
        elif self.battery == 100:
            raise ValueError('Телефон полностью заряжен!')
        else:
            return True
