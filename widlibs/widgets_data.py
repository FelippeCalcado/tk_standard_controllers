class WidgetsData:
    def __init__(self, ui_style='dark'):
        self.ui_style = ui_style

    # Fonts
    font_xsl = ('Segoe UI', 6)
    font_sml = ('Segoe UI', 8)
    font_reg = ('Segoe UI', 12)
    font_lrg = ('Segoe UI', 14)
    font_xlr = ('Segoe UI', 16)

    # Colors
    def colors(self):
        if self.ui_style == 'dark':
            dict_colors = {'generic_background': '#1d2025',
                           'light_fg_color': '#1d2025',
                           'generic_buttons_background': '#1f2933',
                           'light_btn_bg': '#edc298'}

            return dict_colors

        if self.ui_style == 'white':
            dict_colors = {'generic_background': '#ffffff',
                           'light_fg_color': '#edc298',
                           'generic_buttons_background': '#1f2933',
                           'light_btn_bg': '#1f2933'}

            return dict_colors
