import sublime
import sublime_plugin
import sys
import os

sys.path.append(os.path.dirname(__file__))
print(__file__)
import sqlparse

def plugin_loaded():
    global settings
    settings = sublime.load_settings('sql-prettify.sublime-settings')

class SqlPrettifyCommand(sublime_plugin.TextCommand):
    def prettify(self, edit, region):
        try:
            txt_old = self.view.substr(region)
            txt_new = sqlparse.format(txt_old,
                keyword_case               = settings.get("keyword_case"),
                identifier_case            = settings.get("identifier_case"),
                strip_comments             = settings.get("strip_comments"),
                use_space_around_operators = settings.get("use_space_around_operators"),
                strip_whitespace           = settings.get("strip_whitespace"),
                truncate_strings           = settings.get("truncate_strings"),
                truncate_char              = settings.get("truncate_char"),
                indent_columns             = settings.get("indent_columns"),
                reindent                   = settings.get("reindent"),
                reindent_algined           = settings.get("reindent_algined"),
                indent_after_first         = settings.get("indent_after_first"),
                indent_tabs                = settings.get("indent_tabs"),
                indent_width               = settings.get("indent_width"),
                wrap_after                 = settings.get("wrap_after"),
                comma_first                = settings.get("comma_first"),
                right_margin               = settings.get("right_margin")
            )
            if self.view.settings().get('ensure_newline_at_eof_on_save'):
                txt_new = txt_new + "\n"
            self.view.replace(edit, region, txt_new)
        except Exception as e:
            print(e)
            return None

    def run(self, edit):
        window = self.view.window()
        view = window.active_view()
        for region in self.view.sel():
            if region.empty():
                selection = sublime.Region(0, self.view.size())
                self.prettify(edit, selection)
            else:
                self.prettify(edit, region)
