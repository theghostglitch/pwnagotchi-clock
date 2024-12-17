from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime

class PwnClock(plugins.Plugin):
    __author__ = 'https://github.com/LoganMD'
    __version__ = '1.0.3'
    __license__ = 'GPL3'
    __description__ = 'Clock/Calendar for pwnagotchi'

    def on_loaded(self):
        logging.info("Pwnagotchi Clock Plugin loaded.")

    def on_ui_setup(self, ui):
        ui.add_element('date', LabeledValue(color=BLACK, label='', value='',
                                                position=(int(self.options["date_x_coord"]),
                                                            int(self.options["date_y_coord"])),
                                                label_font=fonts.Small, text_font=fonts.Small))
        ui.add_element('time', LabeledValue(color=BLACK, label='', value='',
                                                position=(int(self.options["time_x_coord"]),
                                                            int(self.options["time_y_coord"])),
                                                label_font=fonts.Small, text_font=fonts.Small))

    def on_ui_update(self, ui):
        now = datetime.datetime.today()
        datenow = now.strftime(self.options["date_format"])
        timenow = now.strftime(self.options["time_format"])
        ui.set('date', datenow)
        ui.set('time', timenow)
