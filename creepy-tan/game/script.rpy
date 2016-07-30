# Наша родина - Революция, лагерь, юность и любовь
# Персонажи
define e   = Character('Эйлин',            color="#c8ffc8")
define mt  = Character('Ольга Дмитриевна', color="#00ff00")
define dv  = Character('Алиса',            color="#ff8000")
define us  = Character('Ульяна',           color="#ff0000")
define me  = Character('Семен',            color="#ffffff")
define kr  = Character('Криппи-тян?',      color="#0000ff")
# члены литературного кружка?
define pi1 = Character('Левый Пионер',     color="#BB0000") # угрюмый
define pi2 = Character('Правый Пионер',    color="#DD0000")

label start:

    #================================#
    #= Сцена 1    ===================#
    #= Библиотека ===================#
    $ persistent.sprite_time = "night"
    play ambience ambiences_library_day
    play music music_timid_girl
    show bg int_library_night2

    ">Собрание пионеров в библиотеке."
    
    show us smile pioneer at cright with dissolve
    
    us "Ольга Дмитриевна, я Вас категорически приветствую!"
    us "Ольга Дмитриевна, чем мы займёмся этим вечером?"

    show mt smile pioneer with dissolve
    ">{Описание как Вожатая входит библиотеку, подходит к доске/трибуне}"

    mt "Пионеры! Коммунистическая партия учит нас чтить и бдеть наследие предков."
    mt "Сегоднешний литературный вечер посвещён славянскому фольклёру."

    ">Здесь ОД что-то расскарывает"

    scene black with dissolve
    $ renpy.pause(1.0)
    show bg int_library_night2

    #show dv sad pioneer with dissolve
    ">Мероприятие завершается."
    #hide dv
    
    show us normal pioneer at cright with dissolve
    
    us "Семён, а Семён, кам цу мир, майн либен."
    me "? ? ?"
    "Обернувшись на голос Вожатой, я нашел её машущей мне рукой, а также стоявших рядом Алису и Ульяну."
    
    show us normal pioneer at right with dissolve
    show mt smile pioneer at left with dissolve
    show dv normal pioneer at center with dissolve
    
    ""
    mt ". . . Шкаф ? А что с ним ?"
    dv "Так вышло, что Ульянка закинула за него мой бюз^Wгалстук."
    dv "О, Семён, привет."

    show dv laugh pioneer at center
    dv "Пришлось отодвигать."
    
    show us laugh2 pioneer    
    us "Посреди комнаты лежит. Здоровенный. Фиг сдвинешь!"
    
    show mt surprise pioneer at left
    show us normal pioneer
    mt "Как же вы его уронили?"

    show dv guilty pioneer at center
    dv "Опрокинуть оказалось не сложно . . ."
    
    show us laugh2 pioneer with dissolve
    us "Ей просто очень надо было!"

    stop music
    play music music_awakening_power
    show mt surprise pioneer at fleft
    show us surp1 pioneer at fright
    show dv rage pioneer
    dv "Ульяна!"
    
    show mt grin pioneer with dissolve
    us "Ольга Дмитриевна, она меня в шкафу закрыть хотела, чес-слово!"
    dv "Ну заяц . . ."
    us "Врёшь! Не возьмёшь!"

    show us laugh2 pioneer at running_left
    $ renpy.pause(0.75)

    "С воплем Ульяна пытается пробежать мимо Вожатой, но та ловко хватает её за шиворот."
    
    show dv scared pioneer
    $ renpy.pause(0.5)
    show us dontlike pioneer at running_left_back
    show mt rage pioneer at cleft with dissolve
    $ renpy.pause(0.5)
    mt "Стоять бояться!"
    
    show mt grin pioneer
    mt "Юзернейм, спасай отечество."
    mt "Помоги Двачевской со шкафом."    
    me "Так точно !"
    me "Всмысле , хорошо . Почему бы и нет ."

    stop music
    mt "Вот и славно, идите, скоро отбой."
    
    hide dv
    play music music_heather
    show mt normal at cright with dissolve
    show us at cleft with dissolve
    mt "А Вас, Советова, я попрошу остаться . . ."
    stop music
    show us scared pioneer with dissolve



    #================================#
    #= Сцена 2               ========#
    #= Дорога к домику Алисы ========#
    play ambience ambience_oyez_crickets
    play sound sfx_close_door_campus_1
    play music music_raindrops
    scene black with dissolve
    show bg ext_library_night with dissolve
    show dv normal pioneer at center with dissolve
    dv "Ну потопали;"
    show dv laugh pioneer at center with dissolve
    dv "Пешком по шпалам на юга."
    hide dv

    
    ">ГГ и Алиса идут по тёмному лагерю."
    ">здесь бы вставить звук двух шагов по асфальту"
    stop music
    show bg ext_houses_night with dissolve
    "Оставив Советову в душных застенках гестапо, меня терзало смутное сомнение."
    "В задумчивости, рассматривая белый блин луны и проплывающие мимо деревья, я слушал звук наших шагов."
    "\"Тишину шагами меря ты как будущность войдешь\""
    dv "Ась?"
    me "Удивительно тихо, ни гомона людей, ни машин."

    show dv smile pioneer with dissolve
    dv "Ты ведь недавно приехал."

    show dv laugh pioneer with dissolve
    play sound sfx_punch_medium
    dv "Сразу видно - парень городской."
    "Алиса ткнула меня пальцем в грудь."

    show dv smile pioneer with dissolve
    dv "Это нормальное состояние мира, вне вашего, движимого бензином и электричеством, муравейника."
    dv "Хотя деревня не панацея."
    dv "Деревня прекрасна, однако современные достижения - в науке, промышленности и вообще - без массового переселения в города - невозможны."
    #">хотелось бы задумчивый спрайт алисы"
    me "Безусловно, муравейник."
    me "Более того, современное общество, защищая человека от дикого мира, делает его беззащитнее в широком смысле."
    dv "Такое вот меньшее зло."

    stop ambience fadeout 2.0   # постепенное затихание
    dv "We never asked for this, huh?"
    me "Indeed. Однако, прислушайся, даже цикад не слышно."
    ">ГГ и Алиса остановились."

    show dv laugh pioneer with dissolve
    dv "И правда, таки затишье перед бурей."

    show dv smile pioneer with dissolve
    dv "Не боись, волки́ здесь не водятся, только неко-девочки, да и те - не те."
    dv "К тому же человек - царь природы, негоже нам зверей бояться."
    dv "Ты чего такой напряжёнынй-то?"
    me "Скорее не царь, а тиран пироды. Кстати об Ольге Дмитриевне . . ."

    show dv laugh pioneer with dissolve
    dv "Семён-кун, ты такой заботливый."

    show dv smile pioneer with dissolve
    dv "Не беспокойся за Ульянку. Они с вожатой сёстры по разуму. Ольга, говорят, была чудовищным шкедом совсем недавно." # а ещё у Ульянки под кроватью запрятан третий том Капитала
    dv "Есть мнение, и не только моё, она видит в ней себя. Не может долго на неё злиться."

    play sound sfx_foliage_leaves_rustle
    show dv surprise pioneer with dissolve
    "Внезапный шорох раздался неподалёку"
    "*rustle-rustle-rustle*"
    "Мы с Алисой повернулись на звук, за кустами ничего небыло видно."

    stop sound
    play music music_sunny_day fadein 0.3
    me "Неко-девочки говоришь?"
    dv ". . ."
    dv "Знаешь, я слышала такую фразу, если долго всматриваться в лицо Ленина - "

    play sound sfx_thunder # внезапный хруст ветки и гром
    play ambience ambience_cold_wind_loop
    show dv shocked pioneer with dissolve
    #stop music_sunny_day fadeout 2.0 # на этом месте очень смешное исключение выпадает
    stop music fadeout 2.0
    stop sound fadeout 2.0
    play music music_revenga    # отличная композиция
    hide dv with dissolve
    #быстрый топот
    "Я наблюдал несущщуюся в даль Алису."
    dv "WRYYYYY~"
    me "Погоди!"
    "Не заставив себя ждать, я перешел на галоп."
    # Как будто сердцем я воскрес, и волю дал слезам, и, задыхаясь, в темный лес, бегу по вечерам

    stop music fadeout 1.0
    scene black
    $ renpy.pause(2.0)

    #=================================#
    #= Сцена 3    ====================#
    #= На месте убегающих ГГ и Алисы =#
    show bg ext_houses_night
    play sound sfx_bush_leaves
    $ renpy.pause(2.5)
    show pi1 with dissolve
    $ renpy.pause(0.5)
    # Некоторые догадываются, но многие не знают
    pi1 ". . . Хмм~ . . ."
    pi1 ". . . сегодня . . ."
    pi1 ". . . ветер воет, словно зверь . . ."
    
    play sound sfx_steps_gravel
    hide pi1 with dissolve
    show pi1 at cleft with dissolve
    show pi2_far at cright with dissolve
    pi2 ". . . И я припомнить не могу такого за ним . . ."
    pi1 ". . . чует сердце моё, будто недоброе что-то в наш лагерь ветер принёс . . ."
    pi2 ". . . Так идём же, пока сильны его порывы . . ."
    
    scene black with dissolve
    play sound sfx_steps_gravel
    play sound2 sfx_bush_leaves
    $ renpy.pause(2.0)

    #=========================================#
    #= Сцена 4 ===============================#
    #= Домик Алисы и Ульяны ==================#
    show bg ext_house_of_dv_night with dissolve
    
    pi1 "Хм."
    show bg ext_house_of_mt_night_without_light
    
    show bg ext_houses_sunset
    
    show bg int_house_of_mt_night2
    
    pi1 "Хм."

    dv "Добро пожаловать, снова."
    me "Я тут впервые."
    dv "И то верно. Проходи."    
    dv "Спасибо что согласился помочь, Сёма-кун."
    dv "Мы не много общались, и в довольно смецифических обстоятельствах "

    me ">Здесь что-нибудь про электроника, мол 'Надеюсь электроник до свадьбы заживёт' или что-то в этом духе"

    "Безуслово. Так вот, боюсь у тебя могло солжиться неверное мнение обо мне."
    # Держись козёл за стул, щас как вылезу
    
    kr "Ну чего закопался как врытый?"
    play music music_everlasting_summer_op_edition

    
    "Заметки на полях"

    "В сцене про водку или совместное распитие Алкоголя"
    "Я сразу смазал карту будня *gulp-gulp-gulp* плеснувши краски из стакана."
    "Студня нет, но есть хлеб. Не выпендривайся - зажуй. Хоть водка и бесцветна, не налегай, пионер."

    "На мероприятии Ульяна рассказывает историю - в день праздника Первомая (в тот же день Вальпургиева ночь - 1го мая например)"
    "в пионерлагере случилось страшное. Образцовая пионерка лет десяти убиралась в своём домике."

    "Призрак мёртвой пионерки. Кантузия шкафом это не шутки. Инфаркт микарда. Её призрак оккупировал зеркало шкафа."
    "Но на самом девока выжила. А еще этой девочкой была Алиса."
    "Что за прелесть эти саги, руны зиги и зигзаги"
    "Криппи-тян рисует пенктаграммы? Криппи-тян не наваждение а просто поехавшая (безусловно, в хорошем, правильном смысле) пионерка?"

    return