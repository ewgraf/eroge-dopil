﻿# Этот файл публично доступен. Модифицируйте его под свои сообственные экраны.
init python:
    config.thumbnail_width = 318
    config.thumbnail_height = 179
    
    style.file_picker_ss_window.xpos = 0
    style.file_picker_ss_window.ypos = 0
    
    style.file_picker_text = Style(style.default)
    style.file_picker_text.antialias = True
    style.file_picker_text.font  = "../../storage/fonts/calibri.ttf"
    style.file_picker_text.color = "#bdbdbd"
    style.file_picker_text.selected_color = "#ffffff"
    style.file_picker_text.hover_color = "#ffffff"
    style.file_picker_text.size = 24
    style.file_picker_text.drop_shadow=(2, 2)
    style.file_picker_text.drop_shadow_color = "#000"
    
    style.save_load_button = Style(style.button)
    style.save_load_button.background = get_image("../../storage/images/gui/save_load/thumbnail_idle.png")
    style.save_load_button.hover_background = get_image("../../storage/images/gui/save_load/thumbnail_hover.png")
    style.save_load_button.selected_background = get_image("../../storage/images/gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_hover_background = get_image("../../storage/images/gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_idle_background = get_image("../../storage/images/gui/save_load/thumbnail_selected.png")
    
    style.blank_button = Style(style.button)
    style.blank_button.background = "../../storage/images/misc/none.png"
    style.blank_button.hover_background = "../../storage/images/misc/none.png"
    style.blank_button.selected_background = "../../storage/images/misc/none.png"
    style.blank_button.selected_hover_background = "../../storage/images/misc/none.png"
    style.blank_button.selected_idle_background = "../../storage/images/misc/none.png"
    
    style.base_font = Style(style.default)
    style.base_font.font  = "../../storage/fonts/calibri.ttf"
    style.base_font.size = 28
    style.base_font.line_spacing = 2
    
    style.settings_header = Style(style.base_font)
    style.settings_header.font  = "../../storage/fonts/corbel.ttf"
    style.settings_header.size = 50
    style.settings_header.color = "#4d2e19"
    style.settings_header.hover_color = "#a27146"
    
    style.settings_text = Style(style.settings_header)
    style.settings_text.size = 36
    style.settings_text.selected_color = "#4d2e19"
    style.settings_text.hover_color = "#a27146"
    
    style.settings_link = Style(style.base_font)
    style.settings_link.font  = "../../storage/fonts/gothic.ttf"
    style.settings_link.size = 60
    style.settings_link.kerning = 3
    style.settings_link.color = "#909ca3"
    style.settings_link.hover_color = "#ffffff"
    style.settings_link.selected_color = "#909ca3"
    style.settings_link.selected_idle_color = "#909ca3"
    style.settings_link.selected_hover_color = "#ffffff"
    style.settings_link.insensitive_color = "#909ca3"
    
    style.hyperlink_text = Style(style.settings_link)
    style.hyperlink_text.underline = True
    style.hyperlink_text.hover_color = "#0ff"
    style.hyperlink_text.idle_color = "#08f"
    
    style.music_link = Style(style.settings_link)
    style.music_link.insensitive_color = "#4f4f4f"
    style.music_link.selected_color = "#ffffff"
    
    style.sprite_menu = Style(style.settings_text)
    style.sprite_menu.size = 37
    style.sprite_menu.color = "#466123"
    style.sprite_menu.selected_color = "#466123"
    style.sprite_menu.hover_color = "#9dcd55"
    
    style.say_dialogue = Style(style.base_font)
    style.say_label = Style(style.base_font)
    style.say_label.size = 28
    style.say_label.drop_shadow=(2, 2)
    style.say_label.drop_shadow_color = "#000"
    
    style.chapter = Style(style.base_font)
    style.chapter.font  = "../../storage/fonts/corbel.ttf"
    style.chapter.size = 120
    style.chapter.color = "#fff"
    
    style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]
    
    style.daynum = Style(style.chapter)
    style.daynum.font  = "../../storage/fonts/corbel.ttf"
    style.daynum.size = 45
    
    style.normal_day = Style(style.base_font)
    style.normal_day.color = "#ffdd7d"
    style.normal_day.drop_shadow=(2, 2)
    style.normal_day.drop_shadow_color = "#000"
    style.narrator_day = Style(style.normal_day)
    style.narrator_day.italic = False
    style.thoughts_day = Style(style.normal_day)
    style.thoughts_day.bold = False
    
    style.normal_sunset = Style(style.base_font)
    style.normal_sunset.color = "#ffdd7d"
    style.normal_sunset.drop_shadow=(2, 2)
    style.normal_sunset.drop_shadow_color = "#000"
    style.narrator_sunset = Style(style.normal_sunset)
    style.narrator_sunset.italic = False
    style.thoughts_sunset = Style(style.normal_sunset)
    style.thoughts_sunset.bold = False
    
    style.normal_night = Style(style.base_font)
    style.normal_night.color = "#ffdd7d"
    style.normal_night.drop_shadow=(2, 2)
    style.normal_night.drop_shadow_color = "#000"
    style.narrator_night = Style(style.normal_night)
    style.narrator_night.italic = False
    style.thoughts_night = Style(style.normal_night)
    style.thoughts_night.bold = False
    
    style.normal_prolog = Style(style.base_font)
    style.normal_prolog.color = "#ffdd7d"
    style.normal_prolog.drop_shadow=(2, 2)
    style.normal_prolog.drop_shadow_color = "#000"
    style.narrator_prolog = Style(style.normal_prolog)
    style.narrator_prolog.italic = False
    style.thoughts_prolog = Style(style.normal_prolog)
    style.thoughts_prolog.bold = False
    
    style.cards_button = Style(style.button)
    style.cards_button.background = RoundRect("#000", False)
    style.cards_button.hover_background = RoundRect("#555", False)
    style.cards_button.insensitive_background = RoundRect("#404040", False)
    
    style.cards_button_text = Style(style.button_text)
    style.cards_button_text.color = "#FFF"
    style.cards_button_text.selected_color = "#777"
    style.cards_button_text.insensitive_color = "#c8c8c8"
    
    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None
    
    style.log_button_text = Style(style.normal_day)
    style.log_button_text.selected_color = "#115bc0"
    style.log_button_text.hover_color = "#115bc0"
    style.log_button_text.selected_color = "#b6ff00"
    style.log_button_text.hover_color = "#b6ff00"

##############################################################################
# Say
#
# Экран отображения ADV-диалога.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    window:
        background None
        id "window"
        $ timeofday = persistent.timeofday
        imagebutton:
            auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/backward_%s.png")
            xpos 38
            ypos 924
            action ShowMenu("text_history")
        add get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/dialogue_box_large.png"):
            xpos 174
            ypos 866
        imagebutton:
            auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/hide_%s.png")
            xpos 1508
            ypos 883
            action HideInterface()
        imagebutton:
            auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/save_%s.png")
            xpos 1567
            ypos 883
            action ShowMenu('save')
        imagebutton:
            auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/menu_%s.png")
            xpos 1625
            ypos 883
            action ShowMenu('game_menu_selector')
        imagebutton:
            auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/load_%s.png")
            xpos 1682
            ypos 883
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/forward_%s.png")
                xpos 1768
                ypos 924
                action Skip()
        else:
            imagebutton:
                auto get_image("../../storage/images/gui/dialogue_box/"+timeofday+"/fast_forward_%s.png")
                xpos 1768
                ypos 924
                action Skip()
        text what:
            id "what"
            xpos 194
            ypos 914
            xmaximum 1541
            size 35
            line_spacing 1
        if who:
            text who:
                id "who"
                xpos 194
                ypos 877
                size 35
                line_spacing 1
    
##############################################################################
# Choice
#
# Экран для отображения внутриигровых меню.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Экран для отображения renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Экран для NVL-диалога и меню.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Отображать диалог.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Отображать меню, если есть.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Экран для отображения главного меню при запуске Ren'Py.
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # Это заменяет другие меню.
    tag menu

    # Фон главного меню.
    window:
        style "mm_root"

    # Кнопки главного меню.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Начать игру") action Start()
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Справка") action Help()
        textbutton _("Выход") action Quit(confirm=False)

init -2 python:

    # Сделать все кнопки главного меню одноразмерными.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Экран, включаемый в другие экраны для отображения навигации и фона.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Фон игрового меню.
    window:
        style "gm_root"

    # Кнопки.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Справка") action Help()
        textbutton _("Выход") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load
#
# Экраны для сохранения и загрузки игры.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ибо сохранение и загрузка очень похожи, мы совмещаем их в один экран,
# file_picker. Потом мы используем его из экранов
# загрузки и сохранения.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # Кнопки сверху для выбора страницы.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Пред"):
                action FilePagePrevious()

            textbutton _("Авто"):
                action FilePage("auto")

            textbutton _("Быстро"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("След"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Отобразить сетку файловых слотов.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Отобразить 10 слотов, с номерами от 1 до 10.
            for i in range(1, columns * rows + 1):

                # Каждый из них - кнопка.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Добавить скриншот.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

screen load:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
# Экран, позволяющий пользователю изменять настройки.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Включить навигацию.
    use navigation

    # Разместить навигационные колонки в сетку шириной 3.
    grid 3 1:
        style_group "prefs"
        xfill True

        # Левая колонка.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Отображение")
                textbutton _("Окно") action Preference("display", "window")
                textbutton _("Полный экран") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Переходы")
                textbutton _("Все") action Preference("transitions", "all")
                textbutton _("Никаких") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Скорость текста")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Джойстик...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Пропуск")
                textbutton _("Прочтенных сообщений") action Preference("skip", "seen")
                textbutton _("Всех сообщений") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Начать пропуск") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("После выборов")
                textbutton _("Остановить пропуск") action Preference("after choices", "stop")
                textbutton _("Продолжить пропуск") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Ускорить время")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Ждать голос") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Громкость музыки")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Громкость звука")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Тест"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Громкость голоса")
                    bar value Preference("voice volume")

                    textbutton _("Оставлять голос") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Тест"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Экран, спрашивающий у пользователя вопрос да/нет.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action

    # Правый щелчок и escape отвечают "нет".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Quick Menu
#
# Экран, входящий в экран save и дающий некоторые полезные функции
screen quick_menu:

    # Быстрое внутриигровое меню.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Назад") action Rollback()
        textbutton _("Сохранить") action ShowMenu('save')
        textbutton _("Б.Сохр") action QuickSave()
        textbutton _("Б.Загр") action QuickLoad()
        textbutton _("Пропуск") action Skip()
        textbutton _("Б.Пропуск") action Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настр") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
