from .file_helper_dialog import get_handler
import os
from ifigure.utils.add_sys_path import AddSysPath
from ifigure.widgets.dlg_preference import PrefComponent
from ifigure.utils.setting_parser import iFigureSettingParser as SP
import ifigure.utils.debug as debug
dprint1, dprint2, dprint3 = debug.init_dprints('HelperApp')


class AdvancedConfig(PrefComponent):
    def __init__(self):
        PrefComponent.__init__(self, 'Advanced')
        p = SP()
        self.setting = p.read_setting('pref.advanced_config')

    def save_setting(self):
        p = SP()
        p.write_setting('pref.advanced_config', self.setting)

    def get_dialoglist(self):
        path_txt = '\n'.join(self.setting["user_path"].split(':'))
        list1 = [["Max worker threads number", str(self.setting["max_thread"]), 0, None],
                 ["Text in vector format file", not self.setting["keep_text_as_text"], 3, {
                     "text": "Rasterize Text"}],
                 ["dpi of image in print", str(
                     self.setting["image_dpi"]), 0, None],
                 ["default repository", str(
                     self.setting["hg_default_url"]), 0, None],
                 ["user path", path_txt, 235, {"nlines": 4}],
                 ["file actions",  None, 41,
                  {"label": "Edit...", 'func': get_handler, 'noexpand': True}], ]

        hint1 = ['Maximum number of threads used to run modeling scripts simultaneously',
                 'Non-rasterized text is generated by LaTeX, which may result in longer processing time to generate a PDF/EPS file. Also, text may look differently from what is seen on your screen (requires ghostscript, poppler/xpdf, latex installations)',
                 'dpi (dot per inch) for raster image in EPS/PDF files',
                 'default Mercurial repository',
                 'additinal python path',
                 'edit actions when opening a file']

        return list1, hint1

    def set_dialog_result(self, value):
        self.setting["max_thread"] = int(value[0])
        self.setting["keep_text_as_text"] = not value[1]
        self.setting["image_dpi"] = int(value[2])
        self.setting["hg_default_url"] = str(value[3])
        self.setting["user_path"] = ':'.join(value[4].split('\n'))
        self.add_user_path()

    def add_user_path(self):
        for item in self.setting['user_path'].split(':'):
            AddSysPath(os.path.expanduser(item))
